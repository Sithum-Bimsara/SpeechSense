# Speech-to-Text and Text-to-Speech Project

This project captures speech from a microphone, converts it to text using Google Speech Recognition, and then speaks the recognized text back.

## Clone and Run the Project

### 1. Clone the Repository
```sh
git clone https://github.com/Sithum-Bimsara/SpeechSense.git
cd SpeechSense
```

### 2. Install Dependencies
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

### 3. Run the Script
```sh
python speech_to_text.py
```

## How the Code Works

### 1. Import Required Modules
```python
import speech_recognition as sr
import pyttsx3
```
- `speech_recognition`: Recognizes speech and converts it into text.
- `pyttsx3`: Converts text to speech.

### 2. Function to Convert Text to Speech
```python
def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
```
- Initializes the TTS engine and speaks the given text.

### 3. Function to Recognize Speech
```python
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening for speech input...")
        audio = recognizer.listen(source)
```
- Listens to speech input and adjusts for ambient noise.

### 4. Converting Speech to Text
```python
    try:
        text = recognizer.recognize_google(audio)
        text = text.lower()
        print("You said:", text)
        speak_text(text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
```
- Converts speech to text using Google API and speaks it back.
- Handles errors if speech is unclear or the service is unavailable.

### 5. Running the Program
```python
if __name__ == "__main__":
    recognize_speech()
```
- Executes `recognize_speech()` when the script runs directly.

## Expected Output
**Input (User speaks into the mic):**
📢 "Hello, how are you?"

**Output on Screen:**
```
Adjusting for ambient noise... Please wait.
Listening for speech input...
You said: hello, how are you?
```

**Output as Speech:**
🎤 "hello, how are you?"

---
This project demonstrates real-time speech recognition and text-to-speech conversion using Python. 🚀🎙️

