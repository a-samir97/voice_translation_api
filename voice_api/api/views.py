from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import firebase_functionality, upload_file, speechToText

from rest_framework.decorators import api_view
from rest_framework.response import Response

import json

def index(request):
    return HttpResponse("Welcome To our Voice Translation")

@api_view(['GET'])
def home(request):

    FILENAME = 'new_audio'

    firebase_functionality.download_from_firebase(FILENAME)

    # remove_noise.remove_noise_function(FILENAME)

    upload_file.upload_file_to_bucket(FILENAME, FILENAME)
    
    response_text = speechToText.convert_speech_to_text(FILENAME)

    return Response({"test":json.dumps(response_text.results[0].alternatives[0].transcript)})


def speech(request):
    return HttpResponse("Finished !!!")
