# ACE — Your Personal PC Assistant

ACE is a voice + text personal assistant for your Windows PC. Talk to it or
type to it, and it handles everyday tasks: opening apps, finding files,
controlling volume, taking screenshots, searching the web, taking notes,
setting timers, and more.

It works fully offline with built-in commands, and can optionally use the
Claude API to understand free-form requests it doesn't have a rule for.

## Quick start

```bash
# 1. Install Python 3.10+ from python.org (check "Add to PATH")

# 2. Install ACE's dependencies
pip install -r requirements.txt

# 3. Run ACE in text mode
python -m ace

# 3b. Or run with voice (needs a microphone)
python -m ace --voice
```

Type (or say) things like:

| You say | ACE does |
|---|---|
| `open chrome` | Launches Chrome |
| `find file report.pdf` | Searches your home folder for it |
| `volume up` / `mute` | Adjusts system volume |
| `take a screenshot` | Saves a screenshot to your Pictures folder |
| `search cheap flights to goa` | Opens a web search |
| `note buy milk tomorrow` | Saves a note |
| `set timer 10 minutes` | Starts a countdown timer |
| `what time is it` | Tells you the time |
| `lock my pc` | Locks the workstation |
| `system info` | CPU, RAM and disk usage |
| `help` | Lists everything ACE can do |
| `exit` | Quits |

## Optional: give ACE a real brain (Claude API)

Without a key, ACE only understands its built-in commands. With a key, any
request that doesn't match a built-in command is sent to Claude, so you can
ask ACE anything in natural language.

1. Get an API key from https://console.anthropic.com
2. Set it (either works):
   - Environment variable: `setx ANTHROPIC_API_KEY "sk-ant-..."`
   - Or put `api_key = sk-ant-...` in `%USERPROFILE%\.ace\config.ini`

## Voice mode

```bash
python -m ace --voice
```

- Uses your microphone for speech recognition (Google's free recognizer via
  the `SpeechRecognition` package) and speaks replies out loud (offline, via
  `pyttsx3`).
- Say **"ace"** followed by your command, e.g. *"ace, open notepad"* — or use
  `--no-wake` to skip the wake word entirely.
- Voice mode prints everything it hears and says; press Ctrl+C to quit.

### Changing ACE's voice

```bash
python -m ace --voices                      # list installed voices
python -m ace --voice --tts-voice zira      # try one for this session
```

To make a voice permanent, create `%USERPROFILE%\.ace\config.ini`:

```ini
[ace]
voice = zira        # any part of the voice's name
voice_rate = 180    # words per minute (150 = slower, 210 = faster)
```

Windows ships with David (male) and Zira (female). More voices: Settings →
Time & Language → Speech → Add voices.

## Project layout

```
ace/
├── __main__.py        # entry point: python -m ace
├── assistant.py       # main loop (listen → route → respond)
├── config.py          # settings, paths, API key loading
├── brain/
│   ├── router.py      # matches input against skill patterns
│   └── llm.py         # optional Claude API fallback
├── io_channels/
│   ├── text_io.py     # console input/output
│   └── voice_io.py    # microphone + text-to-speech
└── skills/
    ├── apps.py        # open/close applications
    ├── files.py       # find files, open folders
    ├── system.py      # volume, screenshots, lock, shutdown, sysinfo
    ├── web.py         # web search, open sites, weather
    └── productivity.py# notes, timers, reminders, clipboard
```

### Adding your own skill

Create a file in `ace/skills/`, decorate functions with `@skill(...)`, and
ACE picks it up automatically:

```python
from ace.skills import skill

@skill(r"say hello to (?P<name>.+)", help="say hello to <name>")
def hello(name: str) -> str:
    return f"Hello, {name}!"
```

## Notes

- ACE targets **Windows**; most skills degrade gracefully (with a friendly
  message) on other platforms so you can develop anywhere.
- Shutdown/restart always ask for confirmation first.
