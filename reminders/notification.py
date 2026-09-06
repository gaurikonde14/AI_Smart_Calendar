from plyer import notification

# =========================================================
# AURA - DESKTOP NOTIFICATION SYSTEM
# =========================================================

APP_NAME = "AURA - AI Smart Calendar"


# =========================================================
# SHOW NOTIFICATION
# =========================================================

def show_notification(
    title,
    message,
    timeout=10
):

    try:

        notification.notify(
            title=title,
            message=message,
            app_name=APP_NAME,
            timeout=timeout
        )

        print("🔔 Notification sent successfully.")

        return True

    except Exception as error:

        print("❌ Notification Error:", error)

        return False


# =========================================================
# TEST NOTIFICATION
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("🤖 AURA NOTIFICATION TEST")
    print("=" * 60)

    show_notification(
        title="AURA Reminder 🔔",
        message="This is a test notification from your AI Smart Calendar.",
        timeout=10
    )

    print()
    print("✅ Notification test completed.")