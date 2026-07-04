"""Web: searches, opening sites, quick weather."""

from __future__ import annotations

import urllib.parse
import webbrowser

from ace.skills import skill

SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "maps": "https://maps.google.com",
    "github": "https://github.com",
    "reddit": "https://www.reddit.com",
    "twitter": "https://twitter.com",
    "x": "https://twitter.com",
    "instagram": "https://www.instagram.com",
    "netflix": "https://www.netflix.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "chatgpt": "https://chat.openai.com",
    "claude": "https://claude.ai",
}

_site_names = "|".join(sorted(SITES, key=len, reverse=True))


@skill(
    rf"(?:open|go to) (?P<site>{_site_names})(?:\.com)?",
    help="open youtube / gmail / maps ... — open a website",
    priority=25,
)
def open_site(site: str) -> str:
    webbrowser.open(SITES[site.lower()])
    return f"Opening {site} in your browser."


@skill(
    r"(?:open|go to) (?P<url>(?:https?://)?[\w.-]+\.(?:com|org|net|io|in|dev|ai|co)(?:/\S*)?)",
    help="open <website.com> — open any URL",
    priority=25,
)
def open_url(url: str) -> str:
    full = url if url.startswith("http") else f"https://{url}"
    webbrowser.open(full)
    return f"Opening {url}."


@skill(
    r"(?:search(?: for| the web for)?|google|look up) (?P<query>.+)",
    help="search <anything> — web search",
    priority=60,  # after "search file ..." which is more specific
)
def web_search(query: str) -> str:
    webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}")
    return f"Searching the web for '{query}'."


@skill(
    r"(?:play|youtube) (?P<query>.+?)(?: on youtube)?",
    help="play <song/video> — search it on YouTube",
    priority=35,
)
def play_on_youtube(query: str) -> str:
    webbrowser.open(
        f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(query)}"
    )
    return f"Looking for '{query}' on YouTube."


@skill(
    r"(?:what(?:'s| is) the )?weather(?: like)?(?: in (?P<city>.+?))?(?: today)?",
    help="weather / weather in <city> — quick forecast",
    priority=25,
)
def weather(city: str = "") -> str:
    import urllib.error
    import urllib.request

    location = city.strip() if city else ""
    url = f"https://wttr.in/{urllib.parse.quote(location)}?format=3"
    try:
        with urllib.request.urlopen(url, timeout=6) as response:
            report = response.read().decode().strip()
        return report
    except (urllib.error.URLError, TimeoutError):
        # no internet or service down — fall back to a browser search
        webbrowser.open(
            "https://www.google.com/search?q="
            + urllib.parse.quote_plus(f"weather {location}".strip())
        )
        return "I couldn't fetch the forecast directly, so I opened it in your browser."
