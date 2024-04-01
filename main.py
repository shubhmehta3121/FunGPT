# Import necessary libraries
from translate import Translator
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
import os
import string
from playsound import playsound

# Function to recognize Gujarati speech
def recognize_gujarati_speech():
    recognizer = sr.Recognizer()  # Initialize recognizer

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen for speech and convert it to text
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio, language='gu-IN')
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))

# Function to translate text
def translate_text(say_lang, convert_lang, sentence):
    translator = Translator(from_lang=say_lang, to_lang=convert_lang)
    translation = translator.translate(sentence)
    return translation

# Function to generate text using Gemini API
def generate_text(api_key, prompt):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Function to convert text to Gujarati speech
def text_to_gujarati_speech(text):
    # Specify language as Gujarati
    language = 'gu'

    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save and play the speech
    tts.save('temp_gujarati_speech.mp3')
    playsound('temp_gujarati_speech.mp3')

# Function to remove punctuation from text
def remove_punctuation(sentence):
    # Define punctuation characters
    punctuation_chars = string.punctuation

    # Remove punctuation from the sentence
    clean_sentence = ''.join(char for char in sentence if char not in punctuation_chars)

    return clean_sentence

# Main function
def main():
    # Call the function to recognize Gujarati speech
    recognized_guj_text = recognize_gujarati_speech()

    # Translate recognized Gujarati text to English
    eng_text = translate_text(say_lang='gu-IN', convert_lang='en', sentence=str(recognized_guj_text))
    print("Translated Text:", eng_text)

    # Generate response using Gemini API
    gpt_response = generate_text(api_key="AIzaSyC4EK-dtFyNJIdg3BxsIXGCEXc3__XESYI", prompt=eng_text)  # Replace with your API key
    print("GPT Response:", gpt_response)

    # Remove punctuation from response
    new_gpt_response = remove_punctuation(gpt_response[:500])  # Adjust length if needed
    print("Cleaned Response:", new_gpt_response)

    # Translate response to Gujarati
    guj_text = translate_text(say_lang='en', convert_lang='gu-IN', sentence=str(new_gpt_response))
    print("Translated Response:", guj_text)

    # Convert response to Gujarati speech
    text_to_gujarati_speech(guj_text)

if __name__ == "__main__":
    main()
