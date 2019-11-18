from pathlib import Path
from time import sleep
import uuid
from time import sleep
from google.cloud import storage

BUCKET100 = 'ejemplo_gncon_001'

def tomaFoto( imagenFile):
    from picamera import PiCamera
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture(imagenFile)
    camera.stop_preview()


def upload(imageFile):
    client = storage.Client()
    bucket = client.get_bucket(BUCKET100)
    blob2  = bucket.blob(imageFile)
    blob2.upload_from_filename(filename=imageFile)

s3file =  str(uuid.uuid4().hex)+".jpg"
tomaFoto( s3file)
upload(s3file)

