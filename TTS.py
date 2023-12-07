import speech_recognition as sr
from gtts import gTTS
import os

class SpeechProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen_to_microphone(input:str,self):
        with sr.Microphone() as source:
            SpeechProcessor.text_to_speech(input)
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=5)

        try:
            return self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I could not understand audio.")
        except sr.RequestError as e:
            print(f"Error accessing Google Speech Recognition service: {e}")

    def text_to_speech(self, text, language='en', filename='output.mp3'):
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(filename)
        os.startfile(filename)

if __name__ == "__main__":
    speech_processor = SpeechProcessor()

    # Step 1: Listen to the user's speech
    user_input = speech_processor.listen_to_microphone()

    if user_input:
        # Step 2: Convert user's speech to text and print
        print("You said:", user_input)

        # Step 3: Convert text back to speech
        speech_processor.text_to_speech(user_input)
