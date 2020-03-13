from firebase_admin import storage, credentials, db
import firebase_admin


cred = credentials.Certificate(r'/home/ahmedsamir/Desktop/voice_translation_api/voice_api/api/voicetranslation-b5526-firebase-adminsdk-a932h-9f728d97f8.json')

firebase_admin.initialize_app(cred, {
    'storageBucket':'voicetranslation-b5526.appspot.com'
})

def upload_string(string):

    bucket = storage.bucket()
    blob = bucket.blob('text.txt')
    blob.upload_from_string(string)

def upload_to_firebase():

    bucket = storage.bucket()
    blob = bucket.blob('new_audio.flac')
    blob.upload_from_filename('new_audio.flac')

def download_from_firebase(filename):

    bucket = storage.bucket()
    blob = bucket.blob('new_audio.wav')
    blob.download_to_filename('new_audio.wav')


def upload_to_database_function(string):
    
    ref = db.reference(app=app, url='https://voicetranslation-b5526.firebaseio.com')
    users_ref = ref.child('texts')
    users_ref.set({
        'text': string
    })

