"""System control: volume, screenshots, lock/shutdown, system info."""

from __future__ import annotations

import ctypes
import subprocess
import sys
from datetime import datetime

from ace import config
from ace.skills import skill

IS_WINDOWS = sys.platform == "win32"

# Windows virtual-key codes for the media volume keys
VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
KEYEVENTF_KEYUP = 0x0002


def _press_key(vk: int, times: int = 1) -> None:
    for _ in range(times):
        ctypes.windll.user32.keybd_event(vk, 0, 0, 0)
        ctypes.windll.user32.keybd_event(vk, 0, KEYEVENTF_KEYUP, 0)


@skill(
    r"(?:volume|turn(?: the)? volume) (?P<direction>up|down)(?: .*)?",
    help="volume up / volume down — adjust system volume",
    priority=20,
)
def volume(direction: str) -> str:
    if not IS_WINDOWS:
        return "Volume control is only wired up for Windows right now."
    _press_key(VK_VOLUME_UP if direction.lower() == "up" else VK_VOLUME_DOWN, times=5)
    return f"Volume {direction.lower()}."


@skill(r"(?:mute|unmute)(?: (?:the )?(?:volume|sound|audio|pc))?", help="mute / unmute — toggle sound", priority=20)
def mute() -> str:
    if not IS_WINDOWS:
        return "Mute is only wired up for Windows right now."
    _press_key(VK_VOLUME_MUTE)
    return "Toggled mute."


@skill(
    r"(?:take (?:a )?)?screenshot(?: this)?(?: screen)?",
    help="take a screenshot — saved to Pictures\\ACE Screenshots",
    priority=20,
)
def screenshot() -> str:
    try:
        from PIL import ImageGrab
    except ImportError:
        return "Screenshots need the Pillow package: pip install Pillow"
    image = ImageGrab.grab()
    path = config.screenshots_dir() / f"screenshot-{datetime.now():%Y%m%d-%H%M%S}.png"
    image.save(path)
    return f"Screenshot saved to {path}"


@skill(r"lock(?: (?:my |the )?(?:pc|computer|screen|workstation))?", help="lock my pc — lock the screen", priority=20)
def lock_pc() -> str:
    if IS_WINDOWS:
        ctypes.windll.user32.LockWorkStation()
        return "Locking your PC."
    return "Locking is only wired up for Windows right now."


@skill(
    r"(?:shutdown|shut down)(?: (?:my |the )?(?:pc|computer))?(?: now)?",
    help="shutdown — turn off the PC (asks to confirm)",
    priority=20,
)
def shutdown() -> str:
    if not IS_WINDOWS:
        return "Shutdown is only wired up for Windows right now."
    answer = input("ACE: Really shut down the PC? (yes/no) > ").strip().lower()
    if answer in {"y", "yes"}:
        subprocess.run(["shutdown", "/s", "/t", "5"])
        return "Shutting down in 5 seconds. Goodbye!"
    return "Okay, cancelled."


@skill(
    r"(?:restart|reboot)(?: (?:my |the )?(?:pc|computer))?(?: now)?",
    help="restart — reboot the PC (asks to confirm)",
    priority=20,
)
def restart() -> str:
    if not IS_WINDOWS:
        return "Restart is only wired up for Windows right now."
    answer = input("ACE: Really restart the PC? (yes/no) > ").strip().lower()
    if answer in {"y", "yes"}:
        subprocess.run(["shutdown", "/r", "/t", "5"])
        return "Restarting in 5 seconds."
    return "Okay, cancelled."


@skill(
    r"(?:system info|system status|how(?:'s| is) my (?:pc|computer)(?: doing)?)",
    help="system info — CPU, memory and disk usage",
    priority=20,
)
def system_info() -> str:
    try:
        import psutil
    except ImportError:
        return "System info needs the psutil package: pip install psutil"
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\" if IS_WINDOWS else "/")
    battery = psutil.sensors_battery()
    lines = [
        f"CPU: {cpu:.0f}% in use",
        f"Memory: {mem.percent:.0f}% used ({mem.used / 1e9:.1f} of {mem.total / 1e9:.1f} GB)",
        f"Disk: {disk.percent:.0f}% used ({disk.free / 1e9:.1f} GB free)",
    ]
    if battery is not None:
        state = "charging" if battery.power_plugged else "on battery"
        lines.append(f"Battery: {battery.percent:.0f}% ({state})")
    return "\n".join(lines)
