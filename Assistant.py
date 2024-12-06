import speech_recognition as sr
import pyttsx3
import openai


openai.api_key = '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'


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("There was an error with the speech recognition service.")
            speak("There was an error with the speech recognition service.")
            return None
        except sr.WaitTimeoutError:
            print("You didn't say anything.")
            speak("You didn't say anything.")
            return None

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        message = response['choices'][0]['message']['content']
        return message
    except Exception as e:
        print(f"Error generating response: {e}")
        speak("There was an error generating a response.")
        return None

def main():
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() in ["exit", "quit", "stop", "bye" , "goodbye"]:
                speak("Goodbye!")
                break
            response = generate_response(user_input)
            if response:
                print(f"Assistant: {response}")
                speak(response)


if __name__ == "__main__":
    main()
