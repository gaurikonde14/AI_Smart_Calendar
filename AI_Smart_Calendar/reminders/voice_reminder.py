import pyttsx3

# =========================================================
# AURA - VOICE REMINDER SYSTEM
# =========================================================

# Create voice engine
engine = pyttsx3.init()


# =========================================================
# VOICE SETTINGS
# =========================================================

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


# =========================================================
# SPEAK FUNCTION
# =========================================================

def speak(message):

    if not message:
        return

    try:

        print()
        print("🔊 AURA:", message)

        engine.say(message)

        engine.runAndWait()

    except Exception as error:

        print("❌ Voice Error:", error)


# =========================================================
# GET AVAILABLE VOICES
# =========================================================

def get_voices():

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