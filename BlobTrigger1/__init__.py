import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient, ContentSettings
from datetime import datetime, timedelta, timezone

def main(myblob: func.InputStream):
    if myblob.name and myblob.length:
        logging.info(f"Python blob trigger function processed blob \n"
                    f"Name: {myblob.name}\n"
                    f"Blob Size: {myblob.length} bytes")

# prd container variable
connection_string = "DefaultEndpointsProtocol=https;AccountName=prdbizv3;AccountKey=vkKPUKGacSCiC8PC7g/dEsLB4mRFCwaM/1vWPoL1MCnocm60CNHifXwzxGeoXndYv9/bZzAwdMgc+AStPlMEYA==;EndpointSuffix=core.windows.net"
container_name = "record"
blob_path = "auto_record/"
input_file_extension = '.mp4'
output_content_type_mp4 = "video/mp4"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container=container_name)
blobs_list = container_client.list_blobs(name_starts_with=blob_path)

#blob creation time check variable
current_time = datetime.utcnow()
one_day_ago = current_time - timedelta(days=1)

for blob in blobs_list:
    blob_client = container_client.get_blob_client(blob.name)
    if input_file_extension in blob.name and blob_path in blob.name and blob.creation_time >= one_day_ago:
        blob_client.set_http_headers(content_settings=ContentSettings(content_type=output_content_type_mp4))
    else:
        pass