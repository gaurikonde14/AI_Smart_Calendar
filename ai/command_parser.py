# ============================================================
# AURA - UNIVERSAL COMMAND PARSER
# ============================================================

import re
from datetime import datetime, timedelta


# ============================================================
# DETECT USER INTENT
# ============================================================

def detect_intent(command):
    text = command.lower().strip()

    # ---------------- MUSIC / SONG ----------------
    music_words = [
        "play song",
        "play music",
        "play ",
        "song",
        "music",
        "गाणे",
        "गाणं",
        "गाना",
        "म्युझिक",
        "song laga",
        "music laga"
    ]

    if any(word in text for word in music_words):

        calendar_words = [
            "schedule",
            "meeting",
            "appointment",
            "reminder",
            "remind me",
            "event"
        ]

        if not any(word in text for word in calendar_words):
            return "music"

    # ---------------- MOVIE ----------------
    movie_words = [
        "movie",
        "movies",
        "film",
        "films",
        "watch movie",
        "watch film",
        "चित्रपट",
        "सिनेमा",
        "फिल्म"
    ]

    if any(word in text for word in movie_words):
        return "movie"

    # ---------------- YOUTUBE ----------------
    youtube_words = [
        "youtube",
        "you tube",
        "यूट्यूब"
    ]

    if any(word in text for word in youtube_words):
        return "youtube"

    # ---------------- GOOGLE SEARCH ----------------
    google_words = [
        "google",
        "search",
        "search for",
        "find",
        "look for",
        "गूगल",
        "सर्च",
        "शोध",
        "शोधा"
    ]

    if any(word in text for word in google_words):
        return "google"

    # ---------------- MAPS ----------------
    maps_words = [
        "google maps",
        "maps",
        "map",
        "location",
        "directions",
        "navigate",
        "नकाशा",
        "लोकेशन",
        "रस्ता"
    ]

    if any(word in text for word in maps_words):
        return "maps"

    # ---------------- GMAIL ----------------
    gmail_words = [
        "gmail",
        "email",
        "e-mail",
        "mail",
        "ईमेल",
        "मेल"
    ]

    if any(word in text for word in gmail_words):
        return "gmail"

    # ---------------- FREE TIME ----------------
    free_time_words = [
        "free time",
        "free slot",
        "when am i free",
        "my free time",
        "मोकळा वेळ",
        "free"
    ]

    if any(word in text for word in free_time_words):
        return "free_time"

    # ---------------- FESTIVALS ----------------
    festival_words = [
        "festival",
        "festivals",
        "holiday",
        "holidays",
        "upcoming festival",
        "festival dates",
        "सण",
        "त्योहार"
    ]

    if any(word in text for word in festival_words):
        return "festival"

    # ---------------- TODAY ----------------
    today_words = [
        "what do i have today",
        "today schedule",
        "today's schedule",
        "today events",
        "आज काय आहे",
        "आजचे काय",
        "आजचं काय"
    ]

    if any(word in text for word in today_words):
        return "today"

    # ---------------- CALENDAR / SCHEDULE ----------------
    calendar_words = [
        "schedule",
        "calendar",
        "event",
        "meeting",
        "appointment",
        "reminder",
        "remind me",
        "add event",
        "create event",
        "book meeting",
        "शेड्यूल",
        "मीटिंग",
        "रिमाइंडर",
        "उद्या",
        "tomorrow"
    ]

    if any(word in text for word in calendar_words):
        return "calendar"

    # ---------------- TIME ----------------
    time_words = [
        "what time is it",
        "current time",
        "time now",
        "what is the time",
        "किती वाजले",
        "कितने बजे",
        "वेळ काय"
    ]

    if any(word in text for word in time_words):
        return "time"

    # ---------------- DATE ----------------
    date_words = [
        "today's date",
        "what is today's date",
        "what date is it",
        "current date",
        "date today",
        "आजची तारीख",
        "आज तारीख"
    ]

    if any(word in text for word in date_words):
        return "date"

    # ---------------- GREETING ----------------
    greeting_words = [
        "hello",
        "hi aura",
        "hey aura",
        "hello aura",
        "hey",
        "namaste",
        "नमस्कार",
        "हाय"
    ]

    if any(word in text for word in greeting_words):
        return "greeting"

    # ---------------- HELP ----------------
    help_words = [
        "help",
        "what can you do",
        "what can you do for me",
        "commands",
        "तू काय करू शकतेस",
        "काय करू शकतेस"
    ]

    if any(word in text for word in help_words):
        return "help"

    # ---------------- GENERAL ----------------
    return "general"


# ============================================================
# EXTRACT SEARCH QUERY
# ============================================================

def extract_query(command, intent):

    text = command.strip()

    # Remove assistant name
    text = re.sub(
        r"\baura\b",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Remove common polite words
    remove_words = [
        "please",
        "can you",
        "could you",
        "will you",
        "for me",
        "कृपया"
    ]

    for word in remove_words:
        text = re.sub(
            re.escape(word),
            "",
            text,
            flags=re.IGNORECASE
        )

    text = text.strip()

    # ========================================================
    # MUSIC
    # ========================================================

    if intent == "music":

        patterns = [
            r"^play\s+(.+)$",
            r"^play song\s+(.+)$",
            r"^play music\s+(.+)$",
            r"^song\s+(.+)$",
            r"^music\s+(.+)$",
            r"^song laga\s+(.+)$",
            r"^music laga\s+(.+)$",
            r"^गाणे\s+(.+)$",
            r"^गाणं\s+(.+)$",
            r"^गाना\s+(.+)$"
        ]

        for pattern in patterns:
            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            if match:
                return match.group(1).strip()

    # ========================================================
    # MOVIE
    # ========================================================

    if intent == "movie":

        patterns = [
            r"^find movie\s+(.+)$",
            r"^search movie\s+(.+)$",
            r"^movie\s+(.+)$",
            r"^movies\s+(.+)$",
            r"^watch movie\s+(.+)$",
            r"^watch\s+(.+)$",
            r"^film\s+(.+)$",
            r"^find\s+(.+)$",
            r"^चित्रपट\s+(.+)$",
            r"^सिनेमा\s+(.+)$"
        ]

        for pattern in patterns:
            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            if match:
                return match.group(1).strip()

    # ========================================================
    # YOUTUBE
    # ========================================================

    if intent == "youtube":

        patterns = [
            r"^open youtube$",
            r"^youtube$",
            r"^youtube\s+(.+)$",
            r"^search youtube\s+(.+)$",
            r"^search on youtube\s+(.+)$",
            r"^youtube search\s+(.+)$"
        ]

        for pattern in patterns:
            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            if match:

                if match.lastindex:
                    return match.group(1).strip()

                return ""

    # ========================================================
    # GOOGLE
    # ========================================================

    if intent == "google":

        patterns = [
            r"^google\s+(.+)$",
            r"^search\s+(.+)$",
            r"^search for\s+(.+)$",
            r"^find\s+(.+)$",
            r"^look for\s+(.+)$",
            r"^गूगल\s+(.+)$",
            r"^सर्च\s+(.+)$",
            r"^शोध\s+(.+)$",
            r"^शोधा\s+(.+)$"
        ]

        for pattern in patterns:
            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            if match:
                return match.group(1).strip()

    # ========================================================
    # MAPS
    # ========================================================

    if intent == "maps":

        patterns = [
            r"^google maps$",
            r"^maps$",
            r"^map$",
            r"^google maps\s+(.+)$",
            r"^maps\s+(.+)$",
            r"^map\s+(.+)$",
            r"^location\s+(.+)$",
            r"^directions to\s+(.+)$",
            r"^navigate to\s+(.+)$",
            r"^लोकेशन\s+(.+)$",
            r"^नकाशा\s+(.+)$"
        ]

        for pattern in patterns:
            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            if match:

                if match.lastindex:
                    return match.group(1).strip()

                return ""

    # ========================================================
    # GENERAL QUERY
    # ========================================================

    return text


# ============================================================
# EXTRACT DATE
# ============================================================

def extract_date(command):

    text = command.lower()

    today = datetime.now().date()

    # Today
    if "today" in text or "आज" in text:

        return today.isoformat()

    # Tomorrow
    if (
        "tomorrow" in text
        or "उद्या" in text
        or "कल" in text
    ):

        tomorrow = today + timedelta(days=1)

        return tomorrow.isoformat()

    # Day after tomorrow
    if "day after tomorrow" in text:

        date_value = today + timedelta(days=2)

        return date_value.isoformat()

    # DD/MM/YYYY or DD-MM-YYYY
    match = re.search(
        r"(\d{1,2})[\/\-](\d{1,2})[\/\-](\d{4})",
        command
    )

    if match:

        day = match.group(1).zfill(2)
        month = match.group(2).zfill(2)
        year = match.group(3)

        return f"{year}-{month}-{day}"

    return today.isoformat()


# ============================================================
# EXTRACT TIME
# ============================================================

def extract_time(command):

    # Examples:
    # 5 PM
    # 5:30 PM
    # 10 AM
    # 10:45 AM

    match = re.search(
        r"\b(\d{1,2})(?::(\d{2}))?\s*(AM|PM|am|pm)\b",
        command
    )

    if not match:
        return None

    hour = int(match.group(1))

    minute = int(
        match.group(2)
        or 0
    )

    period = match.group(3).upper()

    if period == "PM" and hour != 12:
        hour += 12

    if period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute:02d}"


# ============================================================
# PARSE COMPLETE COMMAND
# ============================================================

def parse_command(command):

    if not command:

        return {
            "intent": "general",
            "query": "",
            "title": "",
            "date": datetime.now().date().isoformat(),
            "time": None,
            "original_command": ""
        }

    intent = detect_intent(command)

    query = extract_query(
        command,
        intent
    )

    date = extract_date(command)

    time = extract_time(command)

    return {
        "intent": intent,
        "query": query,
        "title": query,
        "date": date,
        "time": time,
        "original_command": command
    }


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    commands = [

        "AURA play Kesariya",

        "play Arijit Singh songs",

        "play Tum Hi Ho",

        "find 3 Idiots movie",

        "watch comedy movies",

        "open YouTube",

        "search Python tutorials on Google",

        "Google artificial intelligence",

        "open Google Maps",

        "Google Maps Amravati",

        "open Gmail",

        "schedule meeting tomorrow at 5 PM",

        "remind me to study tomorrow at 7 PM",

        "what do I have today?",

        "find my free time",

        "what festivals are coming?",

        "what time is it?",

        "what is today's date?",

        "hello aura"
    ]

    print("=" * 60)
    print("AURA COMMAND PARSER TEST")
    print("=" * 60)

    for command in commands:

        result = parse_command(command)

        print("\nCommand:", command)

        print("Intent:", result["intent"])

        print("Query:", result["query"])

        print("Date:", result["date"])

        print("Time:", result["time"])

        print("-" * 60)