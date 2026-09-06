from datetime import datetime


# =========================================================
# AURA - SMART SCHEDULER
# =========================================================


def time_to_minutes(time_string):
    """
    Convert HH:MM into total minutes.
    Example: 10:30 -> 630
    """

    if not time_string:
        return None

    hour, minute = map(
        int,
        time_string.split(":")
    )

    return hour * 60 + minute


# =========================================================
# MINUTES -> TIME
# =========================================================

def minutes_to_time(minutes):
    """
    Convert minutes into HH:MM.
    """

    hour = minutes // 60
    minute = minutes % 60

    return f"{hour:02d}:{minute:02d}"


# =========================================================
# CHECK EVENT CONFLICT
# =========================================================

def check_conflict(new_event, existing_events):
    """
    Check whether new event overlaps with existing events.
    """

    new_date = new_event.get("date")
    new_time = new_event.get("time")

    if not new_time:
        return []

    new_duration = new_event.get(
        "duration",
        60
    )

    new_start = time_to_minutes(
        new_time
    )

    new_end = (
        new_start +
        new_duration
    )

    conflicts = []


    for event in existing_events:

        # Different date = no conflict
        if event.get("date") != new_date:
            continue

        event_time = event.get("time")

        if not event_time:
            continue

        event_start = time_to_minutes(
            event_time
        )

        event_duration = event.get(
            "duration",
            60
        )

        event_end = (
            event_start +
            event_duration
        )


        # Overlap condition
        if (
            new_start < event_end
            and
            new_end > event_start
        ):

            conflicts.append(event)


    return conflicts


# =========================================================
# FIND FREE TIME SLOTS
# =========================================================

def find_free_slots(
    date,
    existing_events,
    duration=60
):

    # Calendar working hours
    start_day = 8 * 60
    end_day = 22 * 60

    busy_slots = []


    # -----------------------------------------------
    # Collect busy slots
    # -----------------------------------------------

    for event in existing_events:

        if event.get("date") != date:
            continue

        event_time = event.get("time")

        if not event_time:
            continue

        start = time_to_minutes(
            event_time
        )

        event_duration = event.get(
            "duration",
            60
        )

        end = start + event_duration

        busy_slots.append(
            (start, end)
        )


    # Sort by start time

    busy_slots.sort()


    free_slots = []

    current_time = start_day


    # -----------------------------------------------
    # Find gaps
    # -----------------------------------------------

    for busy_start, busy_end in busy_slots:

        if (
            current_time + duration
            <= busy_start
        ):

            free_slots.append({

                "start": minutes_to_time(
                    current_time
                ),

                "end": minutes_to_time(
                    current_time + duration
                )

            })


        current_time = max(
            current_time,
            busy_end
        )


    # -----------------------------------------------
    # Check remaining time
    # -----------------------------------------------

    if (
        current_time + duration
        <= end_day
    ):

        free_slots.append({

            "start": minutes_to_time(
                current_time
            ),

            "end": minutes_to_time(
                current_time + duration
            )

        })


    return free_slots


# =========================================================
# PRIORITY SCORE
# =========================================================

def priority_score(priority):

    scores = {

        "Urgent": 4,

        "High": 3,

        "Medium": 2,

        "Low": 1

    }

    return scores.get(
        priority,
        2
    )


# =========================================================
# SUGGEST BEST TIME
# =========================================================

def suggest_time(
    date,
    existing_events,
    duration=60,
    priority="Medium"
):

    free_slots = find_free_slots(
        date,
        existing_events,
        duration
    )


    if not free_slots:

        return None


    # For now choose earliest
    # available slot

    return free_slots[0]


# =========================================================
# GET DAILY SCHEDULE
# =========================================================

def get_daily_schedule(
    date,
    events
):

    daily_events = [

        event

        for event in events

        if event.get("date") == date

    ]


    daily_events.sort(
        key=lambda x: x.get(
            "time",
            "99:99"
        )
    )


    return daily_events


# =========================================================
# SCHEDULE SUMMARY
# =========================================================

def schedule_summary(
    date,
    events
):

    daily_events = get_daily_schedule(
        date,
        events
    )


    if not daily_events:

        return (
            f"No events scheduled "
            f"for {date}."
        )


    return (
        f"You have "
        f"{len(daily_events)} "
        f"event(s) scheduled "
        f"for {date}."
    )


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    existing_events = [

        {
            "id": 1,
            "title": "College",
            "date": "2026-09-07",
            "time": "10:00",
            "duration": 120
        },

        {
            "id": 2,
            "title": "Project Meeting",
            "date": "2026-09-07",
            "time": "14:00",
            "duration": 60
        }

    ]


    # -----------------------------------------------
    # Test conflict
    # -----------------------------------------------

    new_event = {

        "title": "DSA Study",

        "date": "2026-09-07",

        "time": "11:00",

        "duration": 60

    }


    conflicts = check_conflict(
        new_event,
        existing_events
    )


    print("=" * 60)

    print("🤖 AURA SMART SCHEDULER")

    print("=" * 60)


    print()

    print(
        "Conflict count:",
        len(conflicts)
    )


    if conflicts:

        print()

        print("⚠️ CONFLICT FOUND")

        for event in conflicts:

            print(
                "-",
                event["title"],
                "at",
                event["time"]
            )

    else:

        print(
            "✅ No conflict"
        )


    # -----------------------------------------------
    # Test free slots
    # -----------------------------------------------

    print()

    print("🕐 FREE TIME SLOTS")

    free_slots = find_free_slots(

        "2026-09-07",

        existing_events,

        duration=60

    )


    for slot in free_slots:

        print(
            slot["start"],
            "→",
            slot["end"]
        )


    # -----------------------------------------------
    # Best time
    # -----------------------------------------------

    print()

    best_time = suggest_time(

        "2026-09-07",

        existing_events,

        duration=60

    )


    print(
        "💡 Suggested time:",
        best_time
    )