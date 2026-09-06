from pathlib import Path

# =========================================================
# AURA - SMART CALENDAR CONFIGURATION
# =========================================================

# Project base directory
BASE_DIR = Path(__file__).resolve().parent


# =========================================================
# DATABASE
# =========================================================

DATABASE_DIR = BASE_DIR / "database"

DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "calendar.db"


# =========================================================
# APPLICATION
# =========================================================

APP_NAME = "AURA - AI Smart Calendar"

APP_VERSION = "1.0.0"

ASSISTANT_NAME = "AURA"


# =========================================================
# LANGUAGES
# =========================================================

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr"
}


# =========================================================
# EVENT CATEGORIES
# =========================================================

EVENT_CATEGORIES = [
    "Personal",
    "Study",
    "College",
    "Work",
    "Meeting",
    "Birthday",
    "Festival",
    "Holiday",
    "Other"
]


# =========================================================
# PRIORITY
# =========================================================

PRIORITIES = [
    "Low",
    "Medium",
    "High",
    "Urgent"
]


# =========================================================
# REMINDER SETTINGS
# =========================================================

DEFAULT_REMINDER_MINUTES = 30

REMINDER_OPTIONS = [
    0,
    5,
    10,
    15,
    30,
    60,
    120
]


# =========================================================
# VOICE SETTINGS
# =========================================================

VOICE_ENABLED = True

VOICE_RATE = 170

VOICE_VOLUME = 1.0


# =========================================================
# NOTIFICATION
# =========================================================

NOTIFICATION_ENABLED = True


# =========================================================
# DATE & TIME
# =========================================================

TIMEZONE = "Asia/Kolkata"

DEFAULT_TIME_FORMAT = "12h"

DEFAULT_DATE_FORMAT = "%d %B %Y"


# =========================================================
# CALENDAR SETTINGS
# =========================================================

CALENDAR_START_HOUR = 6

CALENDAR_END_HOUR = 23

DEFAULT_EVENT_DURATION = 60


# =========================================================
# AI SETTINGS
# =========================================================

AI_ENABLED = True

SUPPORTED_COMMAND_LANGUAGES = [
    "English",
    "Hindi",
    "Marathi"
]


# =========================================================
# APP INFORMATION
# =========================================================

print("⚙️ AURA configuration loaded")