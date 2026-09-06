from flask import Flask, render_template, request, jsonify
from pathlib import Path
import sqlite3
import threading
import time

# Reminder system
from reminders.reminder_engine import run_reminder_monitor


# ============================================================
# AURA - AI SMART CALENDAR
# ============================================================

app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static"
)

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE = DATABASE_DIR / "calendar.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_db():
    connection = sqlite3.connect(
        DATABASE,
        check_same_thread=False
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# CREATE DATABASE TABLE
# ============================================================

def init_database():

    connection = get_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            event_date TEXT NOT NULL,

            event_time TEXT NOT NULL,

            reminder_time INTEGER DEFAULT 30,

            category TEXT DEFAULT 'Personal',

            priority TEXT DEFAULT 'Medium',

            description TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

    print("✅ Database ready")


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    return render_template("index.html")


# ============================================================
# GET ALL EVENTS
# ============================================================

@app.route("/api/events", methods=["GET"])
def get_events():

    try:

        connection = get_db()

        events = connection.execute("""
            SELECT
                id,
                title,
                event_date,
                event_time,
                reminder_time,
                category,
                priority,
                description
            FROM events
            ORDER BY event_date ASC, event_time ASC
        """).fetchall()

        connection.close()

        result = []

        for event in events:

            result.append({
                "id": event["id"],
                "title": event["title"],
                "date": event["event_date"],
                "time": event["event_time"],
                "reminder": event["reminder_time"],
                "category": event["category"],
                "priority": event["priority"],
                "description": event["description"]
            })

        return jsonify(result)

    except Exception as error:

        print("❌ GET EVENTS ERROR:", error)

        return jsonify({
            "success": False,
            "message": str(error)
        }), 500


# ============================================================
# ADD NEW EVENT
# ============================================================

@app.route("/api/events", methods=["POST"])
def add_event():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "success": False,
                "message": "No data received."
            }), 400

        title = str(data.get("title", "")).strip()

        date = str(data.get("date", "")).strip()

        event_time = str(
            data.get("time", "")
        ).strip()

        reminder = data.get(
            "reminder",
            30
        )

        category = data.get(
            "category",
            "Personal"
        )

        priority = data.get(
            "priority",
            "Medium"
        )

        description = data.get(
            "description",
            ""
        )

        # ----------------------------------------------------
        # Validation
        # ----------------------------------------------------

        if not title:

            return jsonify({
                "success": False,
                "message": "Event title is required."
            }), 400

        if not date:

            return jsonify({
                "success": False,
                "message": "Event date is required."
            }), 400

        if not event_time:

            return jsonify({
                "success": False,
                "message": "Event time is required."
            }), 400

        # ----------------------------------------------------
        # Convert reminder
        # ----------------------------------------------------

        try:

            reminder = int(reminder)

        except:

            reminder = 30

        # ----------------------------------------------------
        # Database insert
        # ----------------------------------------------------

        connection = get_db()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO events (
                title,
                event_date,
                event_time,
                reminder_time,
                category,
                priority,
                description
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            title,
            date,
            event_time,
            reminder,
            category,
            priority,
            description
        ))

        connection.commit()

        event_id = cursor.lastrowid

        connection.close()

        print(
            f"✅ Event added: {title} | "
            f"{date} | {event_time}"
        )

        return jsonify({

            "success": True,

            "message":
                "Event created successfully.",

            "id": event_id,

            "event": {
                "id": event_id,
                "title": title,
                "date": date,
                "time": event_time,
                "reminder": reminder,
                "category": category,
                "priority": priority,
                "description": description
            }

        }), 201

    except Exception as error:

        print(
            "❌ ADD EVENT ERROR:",
            error
        )

        return jsonify({

            "success": False,

            "message": str(error)

        }), 500


# ============================================================
# DELETE EVENT
# ============================================================

@app.route(
    "/api/events/<int:event_id>",
    methods=["DELETE"]
)
def delete_event(event_id):

    try:

        connection = get_db()

        cursor = connection.cursor()

        cursor.execute(
            """
            DELETE FROM events
            WHERE id = ?
            """,
            (event_id,)
        )

        connection.commit()

        deleted = cursor.rowcount

        connection.close()

        if deleted == 0:

            return jsonify({

                "success": False,

                "message":
                    "Event not found."

            }), 404

        print(
            f"🗑️ Event deleted: {event_id}"
        )

        return jsonify({

            "success": True,

            "message":
                "Event deleted successfully."

        })

    except Exception as error:

        print(
            "❌ DELETE EVENT ERROR:",
            error
        )

        return jsonify({

            "success": False,

            "message": str(error)

        }), 500


# ============================================================
# TEST API
# ============================================================

@app.route("/api/test", methods=["GET"])
def test_api():

    return jsonify({

        "success": True,

        "message":
            "AURA API is working!",

        "api":
            "/api/events"

    })


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("🤖 AURA - AI SMART CALENDAR")
    print("=" * 60)

    # Database
    init_database()

    # Reminder monitor
    try:

        run_reminder_monitor()

        print(
            "✅ Reminder system started"
        )

    except Exception as error:

        print(
            "⚠️ Reminder system error:",
            error
        )

    print(
        "✅ Flask server started"
    )

    print()
    print(
        "🌐 Website:"
    )

    print(
        "http://127.0.0.1:5000"
    )

    print()
    print(
        "🔗 Events API:"
    )

    print(
        "http://127.0.0.1:5000/api/events"
    )

    print()
    print(
        "🧪 Test API:"
    )

    print(
        "http://127.0.0.1:5000/api/test"
    )

    print("=" * 60)

    # Important:
    # use_reloader=False prevents the reminder
    # thread from starting twice.

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000,
        use_reloader=False
    )