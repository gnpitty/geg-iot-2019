
from time import sleep
from google.cloud import storage

BUCKET100 = 'ejemplo_gncon_001'

def tomaFoto( imagenFile):
    from picamera import PiCamera
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture(imagenFile)
    camera.stop_preview()


def upload(imageFile):
    client = storage.Client()
    bucket = client.get_bucket(BUCKET100)
    blob2  = bucket.blob('image3.jpg')
    blob2.upload_from_filename(filename=imageFile)

file = "./image.jpg"

#tomaFoto( file)
upload(file)

