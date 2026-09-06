import time
import threading
import sqlite3

from datetime import datetime, timedelta
from pathlib import Path

from reminders.voice_reminder import speak
from reminders.notification import show_notification


# =========================================================
# AURA - SMART REMINDER ENGINE
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE = BASE_DIR / "database" / "calendar.db"


# =========================================================
# DATABASE
# =========================================================

def get_db():

    connection = sqlite3.connect(
        DATABASE,
        check_same_thread=False
    )

    connection.row_factory = sqlite3.Row

    return connection


# =========================================================
# GET EVENTS FROM DATABASE
# =========================================================

def get_events():

    try:

        connection = get_db()

        events = connection.execute("""
            SELECT *
            FROM events
            ORDER BY event_date, event_time
        """).fetchall()

        connection.close()

        return [dict(event) for event in events]

    except Exception as error:

        print("❌ Database Error:", error)

        return []


# =========================================================
# CHECK REMINDER
# =========================================================

def check_reminder(event):

    try:

        event_date = event["event_date"]

        event_time = event["event_time"]

        reminder_minutes = event.get(
            "reminder_time",
            30
        )

        # Event date + exact time

        event_datetime = datetime.strptime(
            f"{event_date} {event_time}",
            "%Y-%m-%d %H:%M"
        )

        # Calculate reminder time

        reminder_datetime = (
            event_datetime
            - timedelta(minutes=int(reminder_minutes))
        )

        now = datetime.now()

        difference = (
            now - reminder_datetime
        ).total_seconds()

        # Reminder should trigger
        # within 60 seconds

        if 0 <= difference < 60:

            return True

        return False

    except (
        KeyError,
        ValueError,
        TypeError
    ):

        return False


# =========================================================
# TRIGGER REMINDER
# =========================================================

def trigger_reminder(event):

    title = event.get(
        "title",
        "Calendar Event"
    )

    event_time = event.get(
        "event_time",
        ""
    )

    category = event.get(
        "category",
        "Personal"
    )


    message = (
        f"Reminder! "
        f"{title} is scheduled "
        f"at {event_time}."
    )


    print()
    print("=" * 60)
    print("🔔 AURA REMINDER")
    print("=" * 60)

    print("📌 Event:", title)
    print("⏰ Time:", event_time)
    print("📂 Category:", category)

    print("=" * 60)


    # Desktop notification

    show_notification(

        title="🔔 AURA Reminder",

        message=message,

        timeout=10

    )


    # Voice reminder

    speak(message)


# =========================================================
# REMINDER MONITOR
# =========================================================

def start_reminder_monitor():

    already_triggered = set()

    print()
    print("=" * 60)
    print("🤖 AURA REMINDER MONITOR")
    print("=" * 60)
    print("🔔 Reminder system is running...")
    print("⏱️ Checking every 10 seconds")
    print("=" * 60)


    while True:

        try:

            events = get_events()


            for event in events:

                event_id = event.get(
                    "id"
                )


                if event_id in already_triggered:

                    continue


                if check_reminder(event):

                    trigger_reminder(event)

                    already_triggered.add(
                        event_id
                    )


            # Check every 10 seconds

            time.sleep(10)


        except Exception as error:

            print(
                "❌ Reminder Monitor Error:",
                error
            )

            time.sleep(10)


# =========================================================
# RUN REMINDER MONITOR IN BACKGROUND
# =========================================================

def run_reminder_monitor():

    reminder_thread = threading.Thread(

        target=start_reminder_monitor,

        daemon=True

    )

    reminder_thread.start()

    print(
        "✅ Background reminder thread started."
    )

    return reminder_thread


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    print("=" * 60)

    print("🤖 AURA REMINDER ENGINE TEST")

    print("=" * 60)


    events = get_events()


    print()

    print(
        "📅 Events found:",
        len(events)
    )


    for event in events:

        print(
            f"{event.get('event_date')} "
            f"{event.get('event_time')} "
            f"→ "
            f"{event.get('title')}"
        )


    print()

    print(
        "✅ Reminder engine test completed."
    )