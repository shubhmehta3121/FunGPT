# FunGPT
## Gujarati Speech to Text and Text Generation with Google Gemini API

This Python script allows users to perform Gujarati speech recognition and translation to English using the Google Web Speech API. The recognized text is then translated to English and used as a prompt to generate a response in English using the Google Gemini API. Finally, the generated English response is translated back to Gujarati and converted to speech.

## How to Operate

### Prerequisites

1. **Google API Key**: Before using the script, you need to obtain a Google Gemini API key. You can get one from the [Google AI Studio](https://makersuite.google.com/app/apikey).
2. **Python Libraries**: Ensure that the required Python libraries are installed. You can install them using `pip`:

    ```
    pip install translate speech_recognition google-generativeai gtts playsound
    ```

### Setup

1. **API Key Configuration**: Replace `"YOUR_API_KEY"` with your actual Google Gemini API key in the script.

2. **Language Preferences**: You can change the input and output languages according to your preference. By default, the script recognizes Gujarati speech and translates it to English. Similarly, the generated English response is translated back to Gujarati.

### How to Use

1. **Run the Script**: Execute the Python script. It will start listening for Gujarati speech input.

2. **Speak**: Speak in Gujarati towards the microphone. The script will recognize your speech and print the recognized text.

3. **Translation and Text Generation**: The recognized Gujarati text is translated to English. This English text is used as a prompt to generate a response using the Gemini API. The generated English response is then translated back to Gujarati.

4. **Speech Output**: The translated Gujarati response is converted to speech and played back.

### User Customization

- **API Key**: Replace `"YOUR_API_KEY"` with your actual Gemini API key.
- **Language Preferences**: Modify the `say_lang` and `convert_lang` parameters in the `translate_text` function to change the input and output languages.

### Example Usage

Suppose you want to converse with someone speaking Gujarati, and you want to understand their speech in English and reply back in Gujarati. This script facilitates that by providing real-time translation and generation of responses.

## Notes

- The script is designed to handle real-time speech recognition, translation, text generation, and speech synthesis.
- Ensure a stable internet connection for accessing the Google Web Speech API and the Gemini API.
- Experiment with different input and output languages as per your requirements.

Feel free to explore and customize the script further based on your needs and preferences! If you encounter any issues or have suggestions for improvements, please feel free to contribute to the repository or raise an issue. Happy conversing! 🎙️🌐
