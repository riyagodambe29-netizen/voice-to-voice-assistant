from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI

load_dotenv()

client = OpenAI()

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        print("Speak something...")

        audio = r.listen(source)
        print("Processing audio (STT)...")

        stt = r.recognize_google(audio)
        print("You said:", stt)

        SYSTEM_PROMPT = """
You are an expert voice agent.
The user's message is a speech transcript.
Respond naturally because your response will be converted back into speech.
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": stt}
            ]
        )

        print("AI Response:", response.choices[0].message.content)

if __name__ == "__main__":
    main()