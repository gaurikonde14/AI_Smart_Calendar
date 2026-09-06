from datetime import datetime


# =========================================================
# AURA - SMART SUGGESTION ENGINE
# =========================================================


# =========================================================
# FESTIVAL SUGGESTIONS
# =========================================================

def get_festival_suggestions(festival_name):

    festival = festival_name.lower()

    suggestions = []


    if "ganesh" in festival:

        suggestions = [
            "Buy Ganesh idol",
            "Buy puja items",
            "Clean the house",
            "Plan decoration",
            "Prepare prasad",
            "Set Ganesh Puja reminder",
            "Plan Ganesh Visarjan"
        ]


    elif "diwali" in festival:

        suggestions = [
            "Start house cleaning",
            "Buy Diwali lights",
            "Buy decorations",
            "Prepare sweets",
            "Buy gifts",
            "Plan family celebration",
            "Set Diwali reminder"
        ]


    elif "holi" in festival:

        suggestions = [
            "Buy colours",
            "Buy snacks",
            "Prepare celebration plan",
            "Invite friends and family",
            "Set Holi reminder"
        ]


    elif "gudi padwa" in festival:

        suggestions = [
            "Buy Gudi items",
            "Clean the house",
            "Prepare traditional food",
            "Plan family celebration",
            "Buy new clothes",
            "Set Gudi Padwa reminder"
        ]


    elif "dussehra" in festival:

        suggestions = [
            "Plan Dussehra celebration",
            "Prepare traditional items",
            "Plan family gathering",
            "Set Dussehra reminder"
        ]


    elif "janmashtami" in festival:

        suggestions = [
            "Prepare puja items",
            "Prepare prasad",
            "Plan decoration",
            "Set evening reminder",
            "Plan celebration"
        ]


    elif "makar sankranti" in festival:

        suggestions = [
            "Buy til-gul",
            "Prepare festive food",
            "Buy kites",
            "Plan family gathering",
            "Set festival reminder"
        ]


    elif "raksha bandhan" in festival:

        suggestions = [
            "Buy Rakhi",
            "Buy gifts",
            "Plan family gathering",
            "Prepare sweets",
            "Set Raksha Bandhan reminder"
        ]


    elif "christmas" in festival:

        suggestions = [
            "Buy Christmas gifts",
            "Decorate the house",
            "Prepare Christmas tree",
            "Plan celebration",
            "Send wishes",
            "Set Christmas reminder"
        ]


    elif "republic day" in festival:

        suggestions = [
            "Attend Republic Day event",
            "Prepare college activity",
            "Set morning reminder",
            "Read about India's Constitution"
        ]


    elif "independence day" in festival:

        suggestions = [
            "Attend flag ceremony",
            "Prepare patriotic activity",
            "Set morning reminder",
            "Learn about India's independence"
        ]


    else:

        suggestions = [
            "Learn about this occasion",
            "Plan your celebration",
            "Set a reminder",
            "Add important tasks",
            "Check your calendar"
        ]


    return suggestions


# =========================================================
# EVENT-BASED SUGGESTIONS
# =========================================================

def get_schedule_suggestions(
    event_title,
    priority="Medium"
):

    title = event_title.lower()

    suggestions = []


    # -----------------------------------------------
    # Study
    # -----------------------------------------------

    if any(
        word in title
        for word in [
            "exam",
            "study",
            "dsa",
            "python",
            "java",
            "assignment",
            "revision"
        ]
    ):

        suggestions = [

            "Keep your phone away",

            "Use a 50-minute study session",

            "Take a 10-minute break",

            "Keep your study material ready",

            "Set a reminder before starting"

        ]


    # -----------------------------------------------
    # Project
    # -----------------------------------------------

    elif any(
        word in title
        for word in [
            "project",
            "presentation",
            "viva",
            "demo"
        ]
    ):

        suggestions = [

            "Prepare your presentation",

            "Keep project files ready",

            "Check your demo",

            "Prepare possible questions",

            "Set a 30-minute reminder"

        ]


    # -----------------------------------------------
    # Meeting
    # -----------------------------------------------

    elif any(
        word in title
        for word in [
            "meeting",
            "discussion",
            "conference"
        ]
    ):

        suggestions = [

            "Prepare your notes",

            "Check meeting location",

            "Keep required documents ready",

            "Join 5 minutes early",

            "Set a reminder"

        ]


    # -----------------------------------------------
    # Birthday
    # -----------------------------------------------

    elif any(
        word in title
        for word in [
            "birthday",
            "bday"
        ]
    ):

        suggestions = [

            "Prepare a birthday wish",

            "Buy a gift",

            "Plan celebration",

            "Set an early reminder"

        ]


    # -----------------------------------------------
    # College
    # -----------------------------------------------

    elif any(
        word in title
        for word in [
            "college",
            "lecture",
            "class"
        ]
    ):

        suggestions = [

            "Prepare your notes",

            "Check today's timetable",

            "Carry required books",

            "Set a reminder before class"

        ]


    # -----------------------------------------------
    # Generic
    # -----------------------------------------------

    else:

        suggestions = [

            "Set a reminder",

            "Add a description",

            "Set event priority",

            "Check for schedule conflicts",

            "Keep some free time before the event"

        ]


    # -----------------------------------------------
    # Priority
    # -----------------------------------------------

    if priority == "Urgent":

        suggestions.insert(
            0,
            "⚠️ This is urgent. Complete it as early as possible."
        )


    elif priority == "High":

        suggestions.insert(
            0,
            "🔴 High priority event. Avoid scheduling conflicts."
        )


    return suggestions


# =========================================================
# UPCOMING FESTIVALS
# =========================================================

def check_upcoming_festival(
    festivals,
    days=7
):

    today = datetime.now().date()

    upcoming = []


    for festival in festivals:

        try:

            festival_date = datetime.strptime(
                festival["date"],
                "%Y-%m-%d"
            ).date()

        except (
            ValueError,
            KeyError
        ):

            continue


        difference = (
            festival_date - today
        ).days


        if 0 <= difference <= days:

            upcoming.append({

                "name": festival["name"],

                "date": festival["date"],

                "days_left": difference

            })


    upcoming.sort(
        key=lambda x: x["date"]
    )


    return upcoming


# =========================================================
# DAILY SUMMARY
# =========================================================

def create_daily_summary(events):

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )


    today_events = [

        event

        for event in events

        if event.get("date") == today

    ]


    if not today_events:

        return "You have no scheduled events today."


    today_events.sort(
        key=lambda x: x.get(
            "time",
            "99:99"
        )
    )


    first_event = today_events[0]

    return (
        f"You have {len(today_events)} "
        f"event(s) today. "
        f"Your first event is "
        f"{first_event.get('title', 'Event')} "
        f"at {first_event.get('time', 'unknown time')}."
    )


# =========================================================
# SMART DAILY ADVICE
# =========================================================

def get_daily_advice(events):

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )


    today_events = [

        event

        for event in events

        if event.get("date") == today

    ]


    advice = []


    if len(today_events) == 0:

        advice.append(
            "🌟 Your day is free. "
            "You can plan something productive."
        )


    elif len(today_events) <= 3:

        advice.append(
            "😊 Your schedule looks manageable."
        )


    else:

        advice.append(
            "⚠️ You have a busy day. "
            "Keep some buffer time between events."
        )


    # Check urgent events

    urgent_events = [

        event

        for event in today_events

        if event.get("priority") == "Urgent"

    ]


    if urgent_events:

        advice.append(
            f"🚨 You have {len(urgent_events)} "
            f"urgent event(s) today."
        )


    # Check study events

    study_events = [

        event

        for event in today_events

        if any(
            word in event.get(
                "title",
                ""
            ).lower()

            for word in [
                "study",
                "exam",
                "assignment"
            ]
        )

    ]


    if study_events:

        advice.append(
            "📚 Keep your study materials ready."
        )


    return advice


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    print("=" * 60)

    print("🤖 AURA SMART SUGGESTION ENGINE")

    print("=" * 60)


    # Festival test

    print()

    print("🎉 GANESH FESTIVAL SUGGESTIONS")

    for item in get_festival_suggestions(
        "Ganesh Chaturthi"
    ):

        print("•", item)


    # Event test

    print()

    print("📚 STUDY SUGGESTIONS")

    for item in get_schedule_suggestions(
        "Python Exam",
        "High"
    ):

        print("•", item)


    # Daily advice test

    print()

    print("🧠 DAILY ADVICE")

    events = [

        {
            "title": "Python Study",
            "date": datetime.now().strftime(
                "%Y-%m-%d"
            ),
            "time": "10:00",
            "priority": "High"
        }

    ]


    for item in get_daily_advice(events):

        print("•", item)