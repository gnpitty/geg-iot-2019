from time import sleep
import uuid
from time import sleep
from google.cloud import storage

PREVIEW_DELAY=2
BUCKET100 = 'ejemplo_gncon_001'
IMG_PATH = 'imagenes'
DEBUG= False

def tomaFoto( imagenFile):
    from picamera import PiCamera
    camera = PiCamera()
    camera.start_preview()
    sleep(PREVIEW_DELAY)
    camera.capture(IMG_PATH+'/'+imagenFile)
    camera.stop_preview()


def upload(imageFile):
    client = storage.Client()
    bucket = client.get_bucket(BUCKET100)
    blob2  = bucket.blob(imageFile)
    file = IMG_PATH+'/'+imageFile
    blob2.upload_from_filename(filename=file)

s3file =  str(uuid.uuid4().hex)+".jpg"
print ('Procesando: '+s3file)
tomaFoto( s3file)

#if DEBUG:
#    s3file = 'image.jpg'

upload(s3file)

