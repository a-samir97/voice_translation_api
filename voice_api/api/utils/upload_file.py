from google.cloud import storage
import os 
from pydub import AudioSegment

BUCKET_NAME = 'voicetranslation1'

def upload_file_to_bucket(source_file_name, destination_blob_name):
    
    """
    Uploads a file to the bucket.
    bucket_name = "your-bucket-name"
    source_file_name = "local/path/to/file"
    destination_blob_name = "storage-object-name"
    """
    wav_audio = AudioSegment.from_file(f"{ source_file_name }.wav", format="wav")
    wav_audio.export(f"{ source_file_name }.flac", format="flac")

    filename =  source_file_name + ".flac"
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(filename)

    blob.upload_from_filename(filename)

    print("Upload Done !")

