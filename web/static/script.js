/* =========================================================
   AURA AI SMART CALENDAR
   COMPLETE MOBILE + DESKTOP FRONTEND
========================================================= */

"use strict";

/* =========================================================
   GLOBAL DATA
========================================================= */

let events = [];
let currentCalendarDate = new Date();

let selectedLanguage = "en-IN";

let recognition = null;
let isListening = false;
let recognitionSupported = false;

let toastTimer = null;


/* =========================================================
   FESTIVALS 2026
========================================================= */

const festivals = [

    {date:"2026-01-01", name:"New Year's Day", category:"National"},
    {date:"2026-01-12", name:"National Youth Day", category:"National"},
    {date:"2026-01-13", name:"Lohri", category:"Festival"},
    {date:"2026-01-14", name:"Makar Sankranti", category:"Festival"},
    {date:"2026-01-23", name:"Vasant Panchami", category:"Festival"},
    {date:"2026-01-26", name:"Republic Day", category:"National"},

    {date:"2026-02-04", name:"World Cancer Day", category:"National"},
    {date:"2026-02-15", name:"Mahashivratri", category:"Festival"},
    {date:"2026-02-19", name:"Chhatrapati Shivaji Maharaj Jayanti", category:"Maharashtra"},
    {date:"2026-02-28", name:"National Science Day", category:"National"},

    {date:"2026-03-04", name:"Holi", category:"Festival"},
    {date:"2026-03-08", name:"International Women's Day", category:"National"},
    {date:"2026-03-19", name:"Gudi Padwa", category:"Maharashtra"},
    {date:"2026-03-20", name:"Eid al-Fitr", category:"Festival"},
    {date:"2026-03-27", name:"Ram Navami", category:"Festival"},

    {date:"2026-04-01", name:"Mahavir Jayanti", category:"Festival"},
    {date:"2026-04-02", name:"Hanuman Jayanti", category:"Festival"},
    {date:"2026-04-07", name:"World Health Day", category:"National"},
    {date:"2026-04-14", name:"Dr. B. R. Ambedkar Jayanti", category:"National"},

    {date:"2026-05-01", name:"Maharashtra Day", category:"Maharashtra"},
    {date:"2026-05-01", name:"Buddha Purnima", category:"Festival"},

    {date:"2026-06-05", name:"World Environment Day", category:"National"},
    {date:"2026-06-21", name:"International Yoga Day", category:"National"},

    {date:"2026-07-29", name:"Guru Purnima", category:"Festival"},

    {date:"2026-08-15", name:"Independence Day", category:"National"},
    {date:"2026-08-16", name:"Parsi New Year", category:"Festival"},
    {date:"2026-08-17", name:"Nag Panchami", category:"Festival"},
    {date:"2026-08-28", name:"Raksha Bandhan", category:"Festival"},

    {date:"2026-09-04", name:"Janmashtami", category:"Festival"},
    {date:"2026-09-05", name:"Teachers' Day", category:"National"},
    {date:"2026-09-14", name:"Ganesh Chaturthi", category:"Maharashtra"},
    {date:"2026-09-14", name:"Hindi Diwas", category:"National"},
    {date:"2026-09-24", name:"Ganesh Visarjan", category:"Maharashtra"},

    {date:"2026-10-02", name:"Gandhi Jayanti", category:"National"},
    {date:"2026-10-11", name:"Navratri Begins", category:"Festival"},
    {date:"2026-10-20", name:"Dussehra", category:"Festival"},
    {date:"2026-10-25", name:"Valmiki Jayanti", category:"Festival"},

    {date:"2026-11-06", name:"Dhanteras", category:"Festival"},
    {date:"2026-11-08", name:"Diwali", category:"Festival"},
    {date:"2026-11-11", name:"Bhai Dooj", category:"Festival"},
    {date:"2026-11-14", name:"Children's Day", category:"National"},
    {date:"2026-11-26", name:"Constitution Day", category:"National"},

    {date:"2026-12-10", name:"Human Rights Day", category:"National"},
    {date:"2026-12-25", name:"Christmas", category:"Festival"}

];


/* =========================================================
   DOM READY
========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    initializeAURA();

});


/* =========================================================
   INITIALIZE
========================================================= */

async function initializeAURA() {

    setupNavigation();

    setupModal();

    setupButtons();

    setupChat();

    setupVoice();

    setupLanguages();

    setupFestivalFilters();

    setupCalendarControls();

    setupNotifications();

    startClock();

    setTodayHeading();

    loadFestivals("All");

    renderCalendar();

    await loadEvents();

    updateDashboard();

    setGreeting();

    console.log("✨ AURA initialized successfully");

}


/* =========================================================
   NAVIGATION
========================================================= */

function setupNavigation() {

    document.querySelectorAll(".nav-item").forEach(button => {

        button.addEventListener("click", () => {

            const sectionName = button.dataset.section;

            if (!sectionName) return;

            document.querySelectorAll(".nav-item")
                .forEach(item => item.classList.remove("active"));

            button.classList.add("active");

            document.querySelectorAll(".section")
                .forEach(section => section.classList.remove("active"));

            const target = document.getElementById(sectionName);

            if (target) {
                target.classList.add("active");
            }

            if (sectionName === "calendar") {
                renderCalendar();
            }

            if (sectionName === "schedule") {
                renderAllEvents();
            }

            if (sectionName === "festivals") {
                loadFestivals("All");
            }

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

        });

    });

}


/* =========================================================
   BUTTONS
========================================================= */

function setupButtons() {

    const createEventBtn =
        document.getElementById("createEventBtn");

    const calendarAddBtn =
        document.getElementById("calendarAddBtn");

    const scheduleAddBtn =
        document.getElementById("scheduleAddBtn");

    const openAssistantBtn =
        document.getElementById("openAssistantBtn");

    const auraOrb =
        document.getElementById("auraOrb");

    const bigAuraOrb =
        document.getElementById("bigAuraOrb");

    const viewScheduleBtn =
        document.getElementById("viewScheduleBtn");


    if (createEventBtn) {
        createEventBtn.addEventListener("click", openEventModal);
    }

    if (calendarAddBtn) {
        calendarAddBtn.addEventListener("click", openEventModal);
    }

    if (scheduleAddBtn) {
        scheduleAddBtn.addEventListener("click", openEventModal);
    }


    if (openAssistantBtn) {

        openAssistantBtn.addEventListener("click", () => {

            activateSection("assistant");

            setTimeout(() => {
                startVoiceInput();
            }, 300);

        });

    }


    /* HERO AURA ORB */

    if (auraOrb) {

        auraOrb.addEventListener("click", () => {

            startVoiceInput();

        });

    }


    /* BIG AURA ORB */

    if (bigAuraOrb) {

        bigAuraOrb.addEventListener("click", () => {

            startVoiceInput();

        });

    }


    if (viewScheduleBtn) {

        viewScheduleBtn.addEventListener("click", () => {
            activateSection("schedule");
        });

    }


    /* QUICK COMMANDS */

    document.querySelectorAll(".quick-command")
        .forEach(button => {

            button.addEventListener("click", () => {

                const command =
                    button.dataset.command || "";

                processCommand(command);

            });

        });

}


/* =========================================================
   ACTIVATE SECTION
========================================================= */

function activateSection(name) {

    document.querySelectorAll(".nav-item")
        .forEach(item => {

            item.classList.toggle(
                "active",
                item.dataset.section === name
            );

        });


    document.querySelectorAll(".section")
        .forEach(section => {

            section.classList.toggle(
                "active",
                section.id === name
            );

        });

}


/* =========================================================
   MODAL
========================================================= */

function setupModal() {

    const modal =
        document.getElementById("eventModal");

    const close =
        document.getElementById("closeModal");

    const cancel =
        document.getElementById("cancelEvent");

    const overlay =
        modal?.querySelector(".modal-overlay");

    const form =
        document.getElementById("eventForm");


    if (close) {
        close.addEventListener("click", closeEventModal);
    }

    if (cancel) {
        cancel.addEventListener("click", closeEventModal);
    }

    if (overlay) {
        overlay.addEventListener("click", closeEventModal);
    }

    if (form) {
        form.addEventListener("submit", saveEvent);
    }

}


function openEventModal() {

    const modal =
        document.getElementById("eventModal");

    if (!modal) return;

    modal.classList.add("show");


    const dateInput =
        document.getElementById("eventDate");

    const timeInput =
        document.getElementById("eventTime");


    if (dateInput && !dateInput.value) {

        dateInput.value =
            formatDateInput(new Date());

    }


    if (timeInput && !timeInput.value) {

        const now = new Date();

        now.setMinutes(
            Math.ceil(now.getMinutes() / 5) * 5
        );

        timeInput.value =
            String(now.getHours()).padStart(2, "0")
            + ":" +
            String(now.getMinutes()).padStart(2, "0");

    }

}


function closeEventModal() {

    const modal =
        document.getElementById("eventModal");

    if (modal) {
        modal.classList.remove("show");
    }

}


/* =========================================================
   SAVE EVENT
========================================================= */

async function saveEvent(e) {

    e.preventDefault();


    const title =
        document.getElementById("eventTitle").value.trim();

    const date =
        document.getElementById("eventDate").value;

    const time =
        document.getElementById("eventTime").value;

    const reminder =
        Number(document.getElementById("reminderTime").value);

    const priority =
        document.getElementById("eventPriority").value;

    const category =
        document.getElementById("eventCategory").value;

    const description =
        document.getElementById("eventDescription").value.trim();


    if (!title || !date || !time) {

        showToast(
            "Missing Details",
            "Please enter title, date and time.",
            "⚠️"
        );

        return;
    }


    const eventData = {

        title,
        date,
        time,
        reminder,
        category,
        priority,
        description

    };


    try {

        const response =
            await fetch("/api/events", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(eventData)

            });


        const result =
            await response.json();


        if (!response.ok || !result.success) {

            throw new Error(
                result.message ||
                "Unable to create event."
            );

        }


        closeEventModal();

        document.getElementById("eventForm").reset();

        await loadEvents();

        updateDashboard();

        renderCalendar();

        renderAllEvents();


        /* ONLY ONE SUCCESS TOAST */

        showToast(
            "Event Created",
            `${title} scheduled successfully.`,
            "✅"
        );


        speak(
            `Event created successfully. ${title}`
        );

    }

    catch (error) {

        console.error(error);

        showToast(
            "Server Error",
            error.message ||
            "Unable to save event.",
            "❌"
        );

    }

}


/* =========================================================
   LOAD EVENTS
========================================================= */

async function loadEvents() {

    try {

        const response =
            await fetch("/api/events");

        if (!response.ok) {
            throw new Error("API unavailable");
        }

        events =
            await response.json();

    }

    catch (error) {

        console.error(
            "Event loading error:",
            error
        );

        events = [];

    }

}


/* =========================================================
   DELETE EVENT
========================================================= */

async function deleteEvent(id) {

    if (!confirm("Delete this event?")) {
        return;
    }


    try {

        const response =
            await fetch(
                `/api/events/${id}`,
                {
                    method: "DELETE"
                }
            );


        const result =
            await response.json();


        if (!response.ok || !result.success) {

            throw new Error(
                result.message ||
                "Unable to delete event."
            );

        }


        showToast(
            "Event Deleted",
            "Event removed successfully.",
            "🗑️"
        );


        await loadEvents();

        updateDashboard();

        renderCalendar();

        renderAllEvents();

    }

    catch (error) {

        console.error(error);

        showToast(
            "Delete Error",
            error.message,
            "❌"
        );

    }

}


/* =========================================================
   DASHBOARD
========================================================= */

function updateDashboard() {

    const today =
        formatDateInput(new Date());


    const todayEvents =
        events.filter(
            event => event.date === today
        );


    const upcoming =
        events.filter(
            event =>
                event.date >= today &&
                event.date !== today
        );


    setText(
        "todayEvents",
        todayEvents.length
    );


    setText(
        "upcomingEvents",
        upcoming.length
    );


    setText(
        "reminderCount",
        events.filter(
            event => Number(event.reminder) > 0
        ).length
    );


    calculateFreeTime(today);

    renderTodaySchedule();

    renderAllEvents();

}


/* =========================================================
   TODAY SCHEDULE
========================================================= */

function renderTodaySchedule() {

    const container =
        document.getElementById("todaySchedule");

    if (!container) return;


    const today =
        formatDateInput(new Date());


    const todayEvents =
        events
            .filter(event => event.date === today)
            .sort((a, b) =>
                a.time.localeCompare(b.time)
            );


    if (!todayEvents.length) {

        container.innerHTML = `

            <div class="empty-large">

                <div>📅</div>

                <h4>No events today</h4>

                <p>
                    Ask AURA to schedule something.
                </p>

            </div>

        `;

        return;

    }


    container.innerHTML =
        todayEvents.map(eventCard).join("");

}


/* =========================================================
   ALL EVENTS
========================================================= */

function renderAllEvents() {

    const container =
        document.getElementById("eventsContainer");

    if (!container) return;


    const sorted =
        [...events].sort((a, b) => {

            const first =
                `${a.date} ${a.time}`;

            const second =
                `${b.date} ${b.time}`;

            return first.localeCompare(second);

        });


    if (!sorted.length) {

        container.innerHTML = `

            <div class="empty-large">

                <div>🗓️</div>

                <h4>No schedules yet</h4>

                <p>
                    Create your first event.
                </p>

            </div>

        `;

        return;

    }


    container.innerHTML =
        sorted.map(eventCard).join("");

}


function eventCard(event) {

    return `

        <div class="event-card">

            <div class="event-time">
                ${formatTime(event.time)}
            </div>

            <div class="event-info">

                <strong>
                    ${escapeHTML(event.title)}
                </strong>

                <small>
                    ${formatPrettyDate(event.date)}
                    •
                    ${escapeHTML(event.category || "Personal")}
                    •
                    ${escapeHTML(event.priority || "Medium")}
                </small>

            </div>

            <button
                class="delete-event"
                onclick="deleteEvent(${event.id})"
                title="Delete">

                🗑️

            </button>

        </div>

    `;

}


/* =========================================================
   FREE TIME
========================================================= */

function calculateFreeTime(date) {

    const dayEvents =
        events.filter(
            event => event.date === date
        );


    const occupied =
        dayEvents.length * 60;


    const availableMinutes =
        Math.max(
            0,
            (22 - 8) * 60 - occupied
        );


    const hours =
        availableMinutes / 60;


    setText(
        "freeTime",
        `${hours.toFixed(1)} hrs`
    );

}


/* =========================================================
   CALENDAR
========================================================= */

function setupCalendarControls() {

    const previous =
        document.getElementById("prevMonth");

    const next =
        document.getElementById("nextMonth");


    if (previous) {

        previous.addEventListener(
            "click",
            () => {

                currentCalendarDate.setMonth(
                    currentCalendarDate.getMonth() - 1
                );

                renderCalendar();

            }
        );

    }


    if (next) {

        next.addEventListener(
            "click",
            () => {

                currentCalendarDate.setMonth(
                    currentCalendarDate.getMonth() + 1
                );

                renderCalendar();

            }
        );

    }

}


function renderCalendar() {

    const container =
        document.getElementById("calendarDays");

    const heading =
        document.getElementById("calendarMonth");


    if (!container || !heading) return;


    const year =
        currentCalendarDate.getFullYear();

    const month =
        currentCalendarDate.getMonth();


    heading.textContent =
        currentCalendarDate.toLocaleString(
            "en-IN",
            {
                month: "long",
                year: "numeric"
            }
        );


    const firstDay =
        new Date(year, month, 1).getDay();

    const days =
        new Date(year, month + 1, 0).getDate();


    container.innerHTML = "";


    for (let i = 0; i < firstDay; i++) {

        const blank =
            document.createElement("div");

        container.appendChild(blank);

    }


    for (let day = 1; day <= days; day++) {

        const cell =
            document.createElement("div");

        cell.className =
            "calendar-day";


        const date =
            `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;


        if (
            date ===
            formatDateInput(new Date())
        ) {

            cell.classList.add("today");

        }


        const dayEvents =
            events.filter(
                event => event.date === date
            );


        cell.innerHTML = `

            <div class="calendar-day-number">
                ${day}
            </div>

            ${
                dayEvents
                    .slice(0, 3)
                    .map(event => `
                        <div class="calendar-event-dot">
                            ${escapeHTML(event.title)}
                        </div>
                    `)
                    .join("")
            }

        `;


        cell.addEventListener(
            "click",
            () => {

                const input =
                    document.getElementById("eventDate");

                if (input) {
                    input.value = date;
                }

                openEventModal();

            }
        );


        container.appendChild(cell);

    }

}


/* =========================================================
   FESTIVALS
========================================================= */

function setupFestivalFilters() {

    document
        .querySelectorAll(".filter-btn")
        .forEach(button => {

            button.addEventListener(
                "click",
                () => {

                    document
                        .querySelectorAll(".filter-btn")
                        .forEach(
                            btn =>
                                btn.classList.remove("active")
                        );


                    button.classList.add("active");


                    loadFestivals(
                        button.dataset.filter
                    );

                }
            );

        });

}


function loadFestivals(filter = "All") {

    const grid =
        document.getElementById("festivalGrid");

    if (!grid) return;


    let list =
        [...festivals];


    if (filter !== "All") {

        list =
            list.filter(
                festival =>
                    festival.category === filter
            );

    }


    grid.innerHTML =
        list.map(festival => `

            <div class="festival-card">

                <div class="festival-date">
                    📅 ${formatPrettyDate(festival.date)}
                </div>

                <h3>
                    ${escapeHTML(festival.name)}
                </h3>

                <p>
                    ${escapeHTML(festival.category)}
                </p>

            </div>

        `).join("");

}


/* =========================================================
   CLOCK
========================================================= */

function startClock() {

    updateClock();

    setInterval(updateClock, 1000);

}


function updateClock() {

    const now =
        new Date();


    const time =
        now.toLocaleTimeString(
            "en-IN",
            {
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit",
                hour12: true
            }
        );


    const date =
        now.toLocaleDateString(
            "en-IN",
            {
                weekday: "long",
                day: "numeric",
                month: "long",
                year: "numeric"
            }
        );


    setText("liveTime", time);

    setText("liveDate", date);

}


function setTodayHeading() {

    const heading =
        document.getElementById("todayHeading");

    if (!heading) return;


    const hour =
        new Date().getHours();


    let greeting = "Good morning";


    if (hour >= 12 && hour < 17) {
        greeting = "Good afternoon";
    }

    else if (hour >= 17) {
        greeting = "Good evening";
    }


    heading.textContent =
        `${greeting} ✨ Your smart day starts here`;

}


/* =========================================================
   AURA GREETING
========================================================= */

function setGreeting() {

    const element =
        document.getElementById("auraGreeting");

    if (!element) return;


    const hour =
        new Date().getHours();


    let greeting = "Good morning";


    if (hour >= 12 && hour < 17) {
        greeting = "Good afternoon";
    }

    else if (hour >= 17) {
        greeting = "Good evening";
    }


    element.innerHTML = `

        ${greeting}! I'm AURA 💜

        <br><br>

        I'm ready to help you organize your day.

        <br><br>

        You can say:

        <br><br>

        <b>
        "Schedule meeting tomorrow at 5 PM"
        </b>

    `;

}


/* =========================================================
   CHAT
========================================================= */

function setupChat() {

    const input =
        document.getElementById("commandInput");

    const send =
        document.getElementById("sendCommand");

    const clear =
        document.getElementById("clearChat");


    if (send) {

        send.addEventListener(
            "click",
            () => {

                const command =
                    input?.value.trim();

                if (!command) return;

                processCommand(command);

                if (input) {
                    input.value = "";
                }

            }
        );

    }


    if (input) {

        input.addEventListener(
            "keydown",
            event => {

                if (event.key === "Enter") {

                    event.preventDefault();

                    const command =
                        input.value.trim();

                    if (!command) return;

                    processCommand(command);

                    input.value = "";

                }

            }
        );

    }


    if (clear) {

        clear.addEventListener(
            "click",
            () => {

                const chat =
                    document.getElementById("chatBox");

                if (!chat) return;

                chat.innerHTML = "";

                addAURAMessage(
                    "Chat cleared 💜 How can I help you?"
                );

            }
        );

    }

}


/* =========================================================
   COMMAND PROCESSOR
========================================================= */

async function processCommand(command) {

    if (!command) return;


    addUserMessage(command);


    const text =
        command.toLowerCase().trim();


    /* GREETING */

    if (
        text === "hi" ||
        text === "hello" ||
        text.includes("hi aura") ||
        text.includes("hello aura") ||
        text.includes("hey")
    ) {

        reply(
            "Hello! 💜 I'm AURA. How can I help you?"
        );

        return;

    }


    /* TODAY */

    if (
        text.includes("today") &&
        (
            text.includes("schedule") ||
            text.includes("event") ||
            text.includes("have")
        )
    ) {

        const today =
            formatDateInput(new Date());


        const list =
            events.filter(
                event => event.date === today
            );


        if (!list.length) {

            reply(
                "You have no events scheduled for today. ✨"
            );

        }

        else {

            reply(
                "Today's schedule:<br><br>" +
                list
                    .map(event =>
                        `• ${formatTime(event.time)} — ${escapeHTML(event.title)}`
                    )
                    .join("<br>")
            );

        }

        return;

    }


    /* FREE TIME */

    if (
        text.includes("free time") ||
        text.includes("free slot") ||
        text === "free"
    ) {

        const today =
            formatDateInput(new Date());


        const todayEvents =
            events.filter(
                event => event.date === today
            );


        reply(
            todayEvents.length
                ? `You have approximately ${calculateFreeHours(todayEvents)} hours of free time today.`
                : "You have plenty of free time today! 🌸"
        );

        return;

    }


    /* FESTIVALS */

    if (
        text.includes("festival") ||
        text.includes("festivals")
    ) {

        const today =
            new Date();


        const upcoming =
            festivals
                .filter(
                    festival =>
                        new Date(festival.date) >= today
                )
                .slice(0, 5);


        if (!upcoming.length) {

            reply(
                "There are no more festivals in my current 2026 list."
            );

        }

        else {

            reply(
                "Upcoming important days:<br><br>" +
                upcoming
                    .map(
                        f =>
                            `🎉 ${formatPrettyDate(f.date)} — ${escapeHTML(f.name)}`
                    )
                    .join("<br>")
            );

        }

        return;

    }


    /* STUDY */

    if (
        text.includes("study") ||
        text.includes("studying")
    ) {

        const suggestion =
            suggestStudyTime();


        reply(
            `For studying, I suggest <b>${suggestion}</b>. 📚`
        );

        return;

    }


    /* DELETE */

    if (
        text.includes("delete") ||
        text.includes("remove")
    ) {

        if (!events.length) {

            reply("There are no events to delete.");

            return;

        }


        const last =
            events[events.length - 1];


        await deleteEvent(last.id);


        reply(
            `I've removed your latest event: <b>${escapeHTML(last.title)}</b>.`
        );

        return;

    }


    /* SCHEDULE */

    if (
        text.includes("schedule") ||
        text.includes("remind") ||
        text.includes("add event") ||
        text.includes("create event") ||
        text.includes("meeting")
    ) {

        const parsed =
            parseCommand(command);


        if (!parsed.title) {

            reply(
                "Sure 💜 Tell me the event name, date and time."
            );

            openEventModal();

            return;

        }


        const saved =
            await createEventFromCommand(parsed);


        if (saved) {

            reply(
                `Done! 💜 I've scheduled <b>${escapeHTML(parsed.title)}</b> on <b>${formatPrettyDate(parsed.date)}</b> at <b>${formatTime(parsed.time)}</b>.`
            );

        }

        return;

    }


    /* HELP */

    if (
        text.includes("help") ||
        text.includes("what can you do")
    ) {

        reply(`

            I can help you with:

            <br><br>

            📅 Create events<br>
            ⏰ Set reminders<br>
            🗓️ Check schedules<br>
            🕐 Find free time<br>
            🎉 Check festivals<br>
            📚 Suggest study time<br>
            🎙️ Voice commands

        `);

        return;

    }


    /* DEFAULT */

    reply(
        `I understood: "<b>${escapeHTML(command)}</b>" 💜<br><br>Ask me about your schedule, festivals or free time.`
    );

}


/* =========================================================
   COMMAND PARSER
========================================================= */

function parseCommand(command) {

    let title =
        command.trim();


    const now =
        new Date();


    let date =
        formatDateInput(now);


    let time =
        "12:00";


    const lower =
        command.toLowerCase();


    /* TOMORROW */

    if (
        /tomorrow|उद्या|उद्या/.test(lower)
    ) {

        const tomorrow =
            new Date(now);

        tomorrow.setDate(
            tomorrow.getDate() + 1
        );

        date =
            formatDateInput(tomorrow);

    }


    /* DAY AFTER TOMORROW */

    if (
        lower.includes("day after tomorrow")
    ) {

        const day =
            new Date(now);

        day.setDate(
            day.getDate() + 2
        );

        date =
            formatDateInput(day);

    }


    /* TODAY */

    if (
        lower.includes("today") ||
        lower.includes("आज")
    ) {

        date =
            formatDateInput(now);

    }


    /* DD/MM/YYYY */

    const dateMatch =
        command.match(
            /(\d{1,2})[\/\-](\d{1,2})[\/\-](\d{4})/
        );


    if (dateMatch) {

        const day =
            dateMatch[1].padStart(2, "0");

        const month =
            dateMatch[2].padStart(2, "0");

        const year =
            dateMatch[3];


        date =
            `${year}-${month}-${day}`;

    }


    /* TIME */

    const timeMatch =
        command.match(
            /(\d{1,2})(?::(\d{2}))?\s*(AM|PM|am|pm)/
        );


    if (timeMatch) {

        let hour =
            Number(timeMatch[1]);

        const minute =
            Number(timeMatch[2] || 0);

        const period =
            timeMatch[3].toUpperCase();


        if (period === "PM" && hour < 12) {
            hour += 12;
        }

        if (period === "AM" && hour === 12) {
            hour = 0;
        }


        time =
            `${String(hour).padStart(2, "0")}:${String(minute).padStart(2, "0")}`;


        title =
            title.replace(
                timeMatch[0],
                ""
            );

    }


    /* REMOVE COMMAND WORDS */

    title =
        title
            .replace(/schedule/gi, "")
            .replace(/scheduled/gi, "")
            .replace(/meeting/gi, "Meeting")
            .replace(/tomorrow/gi, "")
            .replace(/today/gi, "")
            .replace(/please/gi, "")
            .replace(/remind me/gi, "")
            .replace(/add event/gi, "")
            .replace(/create event/gi, "")
            .replace(/\s+/g, " ")
            .trim();


    if (!title) {
        title = "New Event";
    }


    return {
        title,
        date,
        time
    };

}


/* =========================================================
   CREATE EVENT FROM AURA
========================================================= */

async function createEventFromCommand(parsed) {

    try {

        const response =
            await fetch(
                "/api/events",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        title: parsed.title,

                        date: parsed.date,

                        time: parsed.time,

                        reminder: 30,

                        category: "Personal",

                        priority: "Medium",

                        description:
                            "Created by AURA"

                    })

                }
            );


        const result =
            await response.json();


        if (
            !response.ok ||
            !result.success
        ) {

            throw new Error(
                result.message ||
                "Could not create event."
            );

        }


        await loadEvents();

        updateDashboard();

        renderCalendar();

        renderAllEvents();


        /* IMPORTANT:
           Do NOT show another toast here.
           processCommand() will show the reply.
        */

        speak(
            `I've scheduled ${parsed.title}`
        );


        return true;

    }

    catch (error) {

        console.error(error);

        reply(
            "Sorry 💜 I couldn't save that event."
        );

        return false;

    }

}


/* =========================================================
   CHAT MESSAGES
========================================================= */

function addUserMessage(message) {

    const chat =
        document.getElementById("chatBox");

    if (!chat) return;


    const div =
        document.createElement("div");


    div.className =
        "chat-message user";


    div.innerHTML = `

        <div class="chat-small-avatar">
            G
        </div>

        <div class="chat-text">
            ${escapeHTML(message)}
        </div>

    `;


    chat.appendChild(div);

    chat.scrollTop =
        chat.scrollHeight;

}


function addAURAMessage(message) {

    const chat =
        document.getElementById("chatBox");

    if (!chat) return;


    const div =
        document.createElement("div");


    div.className =
        "chat-message aura";


    div.innerHTML = `

        <div class="chat-small-avatar">
            ✦
        </div>

        <div class="chat-text">
            ${message}
        </div>

    `;


    chat.appendChild(div);

    chat.scrollTop =
        chat.scrollHeight;

}


function reply(message) {

    addAURAMessage(message);

    speak(
        stripHTML(message)
    );

}


/* =========================================================
   VOICE SETUP
========================================================= */

function setupVoice() {

    const voiceBtn =
        document.getElementById("voiceBtn");

    const chatMic =
        document.getElementById("chatMic");

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;


    /* BUTTONS */

    if (voiceBtn) {

        voiceBtn.addEventListener(
            "click",
            startVoiceInput
        );

    }


    if (chatMic) {

        chatMic.addEventListener(
            "click",
            startVoiceInput
        );

    }


    /* BROWSER SUPPORT */

    if (!SpeechRecognition) {

        recognitionSupported = false;

        console.warn(
            "Speech Recognition is not supported."
        );

        return;

    }


    recognitionSupported = true;

    recognition =
        new SpeechRecognition();


    recognition.continuous =
        false;

    recognition.interimResults =
        false;

    recognition.maxAlternatives =
        1;

    recognition.lang =
        selectedLanguage;


    /* =====================================================
       VOICE START
    ===================================================== */

    recognition.onstart = () => {

        isListening = true;

        updateVoiceUI(true);

        showToast(
            "AURA Listening",
            "🎙️ Speak now...",
            "🎙️"
        );

        console.log("🎙️ AURA listening...");

    };


    /* =====================================================
       VOICE RESULT
    ===================================================== */

    recognition.onresult = event => {

        if (
            !event.results ||
            !event.results.length
        ) {
            return;
        }


        const transcript =
            event.results[0][0].transcript.trim();


        console.log(
            "🎤 User said:",
            transcript
        );


        const input =
            document.getElementById(
                "commandInput"
            );


        if (input) {
            input.value = transcript;
        }


        /* stop listening UI immediately */

        isListening = false;

        updateVoiceUI(false);


        /* PROCESS COMMAND */

        if (transcript) {

            processCommand(transcript);

        }

    };


    /* =====================================================
       VOICE ERROR
    ===================================================== */

    recognition.onerror = event => {

        console.error(
            "🎙️ Speech recognition error:",
            event.error
        );


        isListening = false;

        updateVoiceUI(false);


        let message =
            "Voice input failed.";


        switch (event.error) {

            case "not-allowed":
                message =
                    "Microphone permission denied. Allow microphone access in Chrome.";
                break;

            case "audio-capture":
                message =
                    "No microphone found. Check your microphone.";
                break;

            case "no-speech":
                message =
                    "I didn't hear anything. Please try again.";
                break;

            case "network":
                message =
                    "Voice service needs an internet connection.";
                break;

            case "aborted":
                return;

            default:
                message =
                    "Please try speaking again.";

        }


        showToast(
            "Voice Problem",
            message,
            "⚠️"
        );

    };


    /* =====================================================
       VOICE END
    ===================================================== */

    recognition.onend = () => {

        isListening = false;

        updateVoiceUI(false);

        console.log(
            "🎙️ AURA stopped listening."
        );

    };

}


/* =========================================================
   START VOICE INPUT
========================================================= */

function startVoiceInput() {

    /* Already listening */

    if (isListening) {

        stopVoiceInput();

        return;

    }


    /* Browser unsupported */

    if (
        !recognition ||
        !recognitionSupported
    ) {

        showToast(
            "Voice Unavailable",
            "Please use Google Chrome on HTTPS.",
            "🎙️"
        );

        return;

    }


    /* Mobile browser */

    if (
        !window.isSecureContext &&
        location.hostname !== "localhost" &&
        location.hostname !== "127.0.0.1"
    ) {

        showToast(
            "Secure Connection Required",
            "Voice needs HTTPS.",
            "🔒"
        );

        return;

    }


    recognition.lang =
        selectedLanguage;


    try {

        recognition.start();

    }

    catch (error) {

        console.log(
            "Recognition start:",
            error.message
        );

    }

}


/* =========================================================
   STOP VOICE
========================================================= */

function stopVoiceInput() {

    if (!recognition) return;


    try {

        recognition.stop();

    }

    catch (error) {

        console.log(error);

    }


    isListening = false;

    updateVoiceUI(false);

}


/* =========================================================
   VOICE UI
========================================================= */

function updateVoiceUI(active) {

    const voiceBtn =
        document.getElementById("voiceBtn");

    const auraOrb =
        document.getElementById("auraOrb");

    const bigAuraOrb =
        document.getElementById("bigAuraOrb");


    /* BUTTON */

    if (voiceBtn) {

        const span =
            voiceBtn.querySelector("span");


        if (span) {

            span.textContent =
                active
                    ? "Listening..."
                    : "Tap & Speak";

        }


        voiceBtn.classList.toggle(
            "listening",
            active
        );

        voiceBtn.setAttribute(
            "aria-label",
            active
                ? "AURA is listening"
                : "Tap to speak to AURA"
        );

    }


    /* HERO ORB */

    if (auraOrb) {

        auraOrb.classList.toggle(
            "listening",
            active
        );

        auraOrb.setAttribute(
            "aria-label",
            active
                ? "AURA is listening"
                : "Tap to speak"
        );

    }


    /* BIG ORB */

    if (bigAuraOrb) {

        bigAuraOrb.classList.toggle(
            "listening",
            active
        );

    }


    /* LISTENING TEXT */

    const listeningText =
        document.querySelector(
            ".tap-to-speak"
        );


    if (listeningText) {

        listeningText.textContent =
            active
                ? "Listening..."
                : "Tap to speak";

    }

}


/* =========================================================
   AURA FEMALE VOICE
========================================================= */

function speak(text) {

    if (!text) return;


    if (
        !("speechSynthesis" in window)
    ) {

        console.warn(
            "Speech synthesis unavailable."
        );

        return;

    }


    window.speechSynthesis.cancel();


    const utterance =
        new SpeechSynthesisUtterance(
            text
        );


    utterance.lang =
        selectedLanguage;


    utterance.rate =
        0.92;


    utterance.pitch =
        1.18;


    utterance.volume =
        1;


    const voices =
        window.speechSynthesis.getVoices();


    let femaleVoice =
        voices.find(
            voice =>
                voice.lang.startsWith(
                    selectedLanguage.split("-")[0]
                )
                &&
                /female|zira|samantha|google|heera|neerja/i
                    .test(voice.name)
        );


    if (!femaleVoice) {

        femaleVoice =
            voices.find(
                voice =>
                    voice.lang.startsWith(
                        selectedLanguage.split("-")[0]
                    )
            );

    }


    if (femaleVoice) {

        utterance.voice =
            femaleVoice;

    }


    window.speechSynthesis.speak(
        utterance
    );

}


/* =========================================================
   LANGUAGE
========================================================= */

function setupLanguages() {

    document
        .querySelectorAll(".language-btn")
        .forEach(button => {

            button.addEventListener(
                "click",
                () => {

                    document
                        .querySelectorAll(".language-btn")
                        .forEach(btn =>
                            btn.classList.remove("active")
                        );


                    button.classList.add("active");


                    selectedLanguage =
                        button.dataset.language ||
                        "en-IN";


                    if (recognition) {

                        recognition.lang =
                            selectedLanguage;

                    }


                    showToast(
                        "Language Changed",
                        button.textContent.trim(),
                        "🌐"
                    );

                }
            );

        });

}


/* =========================================================
   NOTIFICATIONS
========================================================= */

function setupNotifications() {

    const button =
        document.getElementById("notificationBtn");

    const panel =
        document.getElementById("notificationPanel");

    const close =
        document.getElementById("closeNotifications");


    if (button) {

        button.addEventListener(
            "click",
            () => {

                panel?.classList.toggle("show");

                renderNotifications();

            }
        );

    }


    if (close) {

        close.addEventListener(
            "click",
            () => {

                panel?.classList.remove("show");

            }
        );

    }

}


function renderNotifications() {

    const container =
        document.getElementById(
            "notificationList"
        );

    if (!container) return;


    const today =
        formatDateInput(new Date());


    const upcoming =
        events
            .filter(
                event =>
                    event.date >= today
            )
            .slice(0, 5);


    if (!upcoming.length) {

        container.innerHTML = `

            <div class="empty-notification">

                🔔

                <p>
                    No upcoming events
                </p>

            </div>

        `;

        return;

    }


    container.innerHTML =
        upcoming.map(event => `

            <div class="event-card">

                <div class="event-info">

                    <strong>
                        ${escapeHTML(event.title)}
                    </strong>

                    <small>
                        ${formatPrettyDate(event.date)}
                        •
                        ${formatTime(event.time)}
                    </small>

                </div>

            </div>

        `).join("");

}


/* =========================================================
   TOAST
========================================================= */

function showToast(
    title,
    message,
    icon = "✓"
) {

    const toast =
        document.getElementById("toast");

    if (!toast) return;


    setText(
        "toastTitle",
        title
    );


    setText(
        "toastMessage",
        message
    );


    setText(
        "toastIcon",
        icon
    );


    toast.classList.add("show");


    /* Prevent multiple timers */

    if (toastTimer) {
        clearTimeout(toastTimer);
    }


    toastTimer =
        setTimeout(() => {

            toast.classList.remove("show");

        }, 2500);

}


/* =========================================================
   HELPERS
========================================================= */

function setText(id, value) {

    const element =
        document.getElementById(id);

    if (element) {
        element.textContent = value;
    }

}


function formatDateInput(date) {

    const year =
        date.getFullYear();

    const month =
        String(date.getMonth() + 1)
            .padStart(2, "0");

    const day =
        String(date.getDate())
            .padStart(2, "0");


    return `${year}-${month}-${day}`;

}


function formatPrettyDate(dateString) {

    const date =
        new Date(
            dateString + "T00:00:00"
        );


    return date.toLocaleDateString(
        "en-IN",
        {
            day: "numeric",
            month: "short",
            year: "numeric"
        }
    );

}


function formatTime(time) {

    if (!time) return "--:--";


    const parts =
        time.split(":");


    let hour =
        Number(parts[0]);


    const minute =
        parts[1] || "00";


    const suffix =
        hour >= 12
            ? "PM"
            : "AM";


    hour =
        hour % 12 || 12;


    return `${hour}:${minute} ${suffix}`;

}


function escapeHTML(value) {

    return String(value ?? "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");

}


function stripHTML(text) {

    const div =
        document.createElement("div");

    div.innerHTML =
        text;

    return (
        div.textContent ||
        div.innerText ||
        ""
    );

}


function calculateFreeHours(list) {

    const occupied =
        list.length;

    return Math.max(
        0,
        14 - occupied
    ).toFixed(1);

}


function suggestStudyTime() {

    const hours = [
        "6:00 PM",
        "7:00 PM",
        "8:00 PM",
        "9:00 AM"
    ];


    const today =
        formatDateInput(new Date());


    const busy =
        events
            .filter(
                event =>
                    event.date === today
            )
            .map(
                event =>
                    formatTime(event.time)
            );


    for (const hour of hours) {

        if (!busy.includes(hour)) {
            return hour;
        }

    }


    return "9:00 PM";

}


/* =========================================================
   GLOBAL ACCESS
========================================================= */

window.deleteEvent =
    deleteEvent;

window.processCommand =
    processCommand;

window.openEventModal =
    openEventModal;

window.startVoiceInput =
    startVoiceInput;

window.stopVoiceInput =
    stopVoiceInput;


/* =========================================================
   FINAL
========================================================= */

console.log(
    "✨ AURA AI Smart Calendar - Mobile Voice Edition loaded"
);
