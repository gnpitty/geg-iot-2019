from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('ejemplo_gncon_001')
# Then do other things...
blob2 = bucket.blob('/image3.jpg')
blob2.upload_from_filename(filename='./image.jpg')
