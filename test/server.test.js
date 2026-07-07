/** HTTP smoke tests — run with `npm test`. No framework, exits non-zero on failure. */

const assert = require('node:assert');
const { server } = require('../server');

async function main() {
  await new Promise((resolve) => server.listen(0, resolve));
  const base = `http://localhost:${server.address().port}`;
  const get = (p) => fetch(base + p);
  const json = async (p, opts) => (await fetch(base + p, opts)).json();

  // Static shell
  const home = await get('/');
  assert.equal(home.status, 200);
  assert.match(await home.text(), /Agentic OS/);

  // Health
  const health = await json('/api/health');
  assert.equal(health.ok, true);
  assert.equal(typeof health.modules.youtube, 'boolean');

  // Metrics (demo mode without env vars)
  const metrics = await json('/api/metrics/youtube');
  assert.equal(typeof metrics.channel.subscribers, 'number');
  assert.ok(Array.isArray(metrics.recentVideos) && metrics.recentVideos.length > 0);

  // Hermes chat (demo mode)
  const chat = await json('/api/hermes/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: 'status report' }),
  });
  assert.ok(chat.reply.includes('status report'));

  const badChat = await get('/api/hermes/chat').then((r) => r.status);
  assert.equal(badChat, 404); // GET not routed

  // Knowledge
  const docs = await json('/api/knowledge/docs');
  assert.ok(docs.length >= 3);
  const search = await json('/api/knowledge/search?q=railway');
  assert.ok(search.results.length > 0);
  assert.ok(search.results[0].snippet.length > 0);
  const emptySearch = await get('/api/knowledge/search').then((r) => r.status);
  assert.equal(emptySearch, 400);

  // Workflows CRUD
  const created = await json('/api/workflows', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: 'smoke-test workflow' }),
  });
  assert.equal(created.status, 'todo');
  const updated = await json(`/api/workflows/${created.id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status: 'active' }),
  });
  assert.equal(updated.status, 'active');
  const list = await json('/api/workflows');
  assert.ok(list.some((w) => w.id === created.id && w.status === 'active'));
  const badStatus = await fetch(`${base}/api/workflows/${created.id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status: 'bogus' }),
  });
  assert.equal(badStatus.status, 400);

  // Path traversal is blocked (never escapes public/)
  const traversal = await get('/..%2f..%2fserver.js');
  assert.match(await traversal.text(), /Agentic OS/); // falls back to the shell

  server.close();
  console.log('All smoke tests passed.');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
