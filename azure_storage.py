import os
import json
from azure.storage.blob import BlobServiceClient

CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME =  "notes"
BLOB_NAME = "notes.json"

def get_blob_client():
    service = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container = service.get_container_client(CONTAINER_NAME)
    return container.get_blob_client(BLOB_NAME)

def load_notes():
    try: 
        blob = get_blob_client()
        data = blob.download_blob().readall()
        return json.loads(data)
    except Exception:
        return[]
    
    
def save_notes(notes):
    blob = get_blob_client()
    blob.upload_blob(json.dumps(notes), overwrite=True)