# =========================================================
# AURA - VOICE REMINDER SYSTEM
# =========================================================

# pyttsx3 is optional.
# It works on local computer but may not work on Render/Linux.
try:
    import pyttsx3
except ImportError:
    pyttsx3 = None


# =========================================================
# CREATE VOICE ENGINE
# =========================================================

engine = None

if pyttsx3 is not None:
    try:
        engine = pyttsx3.init()

        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

    except Exception as error:
        print("⚠️ Voice engine unavailable:", error)
        engine = None


# =========================================================
# SPEAK FUNCTION
# =========================================================

def speak(message):

    if not message:
        return

    print()
    print("🔊 AURA:", message)

    # Render/server doesn't have desktop voice
    if engine is None:
        print("ℹ️ Server voice is unavailable.")
        print("ℹ️ Browser voice will be used for AURA.")
        return False

    try:

        engine.say(message)
        engine.runAndWait()

        return True

    except Exception as error:

        print("❌ Voice Error:", error)

        return False


# =========================================================
# GET AVAILABLE VOICES
# =========================================================

def get_voices():

    if engine is None:

        print("⚠️ Voice engine is not available.")

        return []

    try:

        voices = engine.getProperty("voices")

        print()
        print("=" * 50)
        print("🔊 AVAILABLE VOICES")
        print("=" * 50)

        for index, voice in enumerate(voices):

            print(
                f"{index}: "
                f"{voice.name}"
            )

        return voices

    except Exception as error:

        print("❌ Voice list error:", error)

        return []


# =========================================================
# SET VOICE
# =========================================================

def set_voice(voice_index=0):

    if engine is None:

        print("⚠️ Voice engine is not available.")

        return False

    try:

        voices = engine.getProperty("voices")

        if not voices:

            print("❌ No voices available.")

            return False

        if 0 <= voice_index < len(voices):

            engine.setProperty(
                "voice",
                voices[voice_index].id
            )

            print(
                "✅ Voice changed to:",
                voices[voice_index].name
            )

            return True

        print("❌ Invalid voice index.")

        return False

    except Exception as error:

        print(
            "❌ Voice selection error:",
            error
        )

        return False


# =========================================================
# TEST VOICE
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("🤖 AURA VOICE REMINDER TEST")
    print("=" * 60)

    print()

    print("Checking available voices...")

    get_voices()

    print()

    print("Testing AURA voice...")

    speak(
        "Hello! I am AURA, your AI Smart Calendar Assistant."
    )

    print()

    print("✅ Voice test completed.")
