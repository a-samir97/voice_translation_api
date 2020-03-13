from google.cloud import texttospeech
import os

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'speechToText-ea44db92bc5d.json'

def convert_text_to_speech(file_name):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    print("Enter Your Text here : ")

    input_string = input()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=input_string)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    with open(f'{ file_name }.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print(f'Audio content written to file "{ file_name }.mp3"')
