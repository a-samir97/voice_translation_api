# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def convert_speech_to_text(file_name):
    
    # Instantiates a client
    client = speech.SpeechClient()

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        language_code='en-US',)

    audio = {"uri":f"gs://voicetranslation1/{ file_name }.flac"}

    # Detects speech in the audio file
    response =  client.recognize(config, audio)
    
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

    return response