from time import sleep
import uuid
from time import sleep
from google.cloud import storage
import sys
import os

PREVIEW_DELAY=2
BUCKET100 = 'ejemplo_gncon_001'
IMG_PATH = 'imagenes'
DEBUG= False

# captura de foto en Raspberry Pi
def tomaFoto( imagenFile):
    from picamera import PiCamera
    camera = PiCamera()
    camera.start_preview()
    sleep(PREVIEW_DELAY)
    camera.capture(IMG_PATH+'/'+imagenFile)
    camera.stop_preview()

# captura de foto en la MAC OS X
def capImageOSX(imagenFile):
    import cv2
    cap = cv2.VideoCapture(0)
    
    file =  IMG_PATH+"/"+imagenFile
    print("file: " + file)
    while(True):
      ret, frame = cap.read()
      rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
      
      cv2.imshow('frame', rgb)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite(file, frame)
        break

    cap.release()
    cv2.destroyAllWindows()
     
# upload del archivo de imagen al Bucket de datos en GC-Storage
def upload(imageFile):
    client = storage.Client()
    bucket = client.get_bucket(BUCKET100)
    blob2  = bucket.blob(imageFile)
    file = IMG_PATH+'/'+imageFile
    blob2.upload_from_filename(filename=file)

s3file =  str(uuid.uuid4().hex)+".jpg"
print ('Procesando: '+s3file)

if sys.platform == "darwin":
    capImageOSX(s3file)
else:
    tomaFoto( s3file)

 

upload(s3file)

