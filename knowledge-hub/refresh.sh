#!/usr/bin/env bash
# Rebuild the cross-project knowledge graph from the latest code.
# Requires: graphify CLI (uv tool install graphifyy), git.
set -euo pipefail

HUB_DIR="$(cd "$(dirname "$0")" && pwd)"
WORK_DIR="${GRAPHIFY_WORK_DIR:-$HUB_DIR/.repos}"
OWNER="ajay062002"
REPOS=(
  career-command-center
  attendance-management-system
  f1-app
  resume-builder
)

mkdir -p "$WORK_DIR"

GRAPHS=()
for repo in "${REPOS[@]}"; do
  dir="$WORK_DIR/$repo"
  if [ -d "$dir/.git" ]; then
    git -C "$dir" pull --ff-only
  else
    git clone --depth 1 "https://github.com/$OWNER/$repo" "$dir"
  fi
  graphify update "$dir"
  GRAPHS+=("$dir/graphify-out/graph.json")
done

# SasarkSambhavam ships its project as a zip inside the repo.
sasark="$WORK_DIR/SasarkSambhavam"
if [ -d "$sasark/.git" ]; then
  git -C "$sasark" pull --ff-only
else
  git clone --depth 1 "https://github.com/$OWNER/SasarkSambhavam" "$sasark"
fi
zipfile="$(find "$sasark" -maxdepth 1 -name '*.zip' | head -1)"
if [ -n "$zipfile" ]; then
  unzip -q -o "$zipfile" -x "*/.venv/*" -d "$sasark/extracted"
  project_dir="$(dirname "$(find "$sasark/extracted" -name requirements.txt | head -1)")"
  graphify update "$project_dir"
  GRAPHS+=("$project_dir/graphify-out/graph.json")
fi

graphify merge-graphs "${GRAPHS[@]}" --out "$HUB_DIR/graphs/all-projects-graph.json"
graphify cluster-only "$HUB_DIR" --graph "$HUB_DIR/graphs/all-projects-graph.json" --no-label

for repo in "${REPOS[@]}"; do
  cp "$WORK_DIR/$repo/graphify-out/GRAPH_REPORT.md" "$HUB_DIR/reports/$repo.md"
done

echo "Done. Merged graph: $HUB_DIR/graphs/all-projects-graph.json"
graphify benchmark "$HUB_DIR/graphs/all-projects-graph.json"
