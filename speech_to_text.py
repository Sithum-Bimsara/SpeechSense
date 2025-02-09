import speech_recognition as sr
import pyttsx3

def speak_text(command):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def recognize_speech():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening for speech input...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print("You said:", text)
        speak_text(text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    recognize_speech()
