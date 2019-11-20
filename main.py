from google.cloud import vision
import io
import logging
from google.cloud import logging as cloudlogging
 

lg_client = cloudlogging.Client()

lg_handler = lg_client.get_default_handler()
cloud_logger = logging.getLogger("cloudLogger")
cloud_logger.setLevel(logging.DEBUG)
cloud_logger.addHandler(lg_handler)
cloud_logger.info("Informacion con tipo INFO, Version 2.0.4")
cloud_logger.error("Informacion con tipo Error, para mensajes de error")
 
def publish_message(project_id, topic_name,data):
    from google.cloud import pubsub_v1
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    future = publisher.publish(topic_path, data=data)
    print(future.result())
    
def detect_faces_uri(uri):
    """Detects faces in the file located in Google Cloud Storage or the web."""
    print("URI:"+uri)
    cloud_logger.info(f"detect_faces_uri:{uri}")
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    # [START vision_python_migration_image_uri]
    image = vision.types.Image()
    image.source.image_uri = uri
    image.source.gcs_image_uri = uri

    # [END vision_python_migration_image_uri]

    response = client.face_detection(image=image)
    faces = response.face_annotations

    objects = client.object_localization(
        image=image).localized_object_annotations
    #print('=' * 79)
    print('Number of objects found: {}'.format(len(objects)))    

    # Names of likelihood from google.cloud.vision.enums
    #likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
    #                   'LIKELY', 'VERY_LIKELY')
    mensaje1 =  'Faces total:'+str(len(faces))
    cloud_logger.info(mensaje1)
    mensaje = str.encode(mensaje1+":"+uri)
    topic_name = "geginfo"
    project_id = 'iot-geg-2019'
    publish_message(project_id, topic_name,mensaje)
  
def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    cloud_logger.info('log debug, esta es una prueba')
    uri2 = "gs://"+event['bucket']+"/"+event['name']
    cloud_logger.info(f"Uri2:{uri2}")
    cloud_logger.info(f"event: {event}")
    detect_faces_uri( uri2)
   # detect_faces(event.data.medialink)
   
  

    
