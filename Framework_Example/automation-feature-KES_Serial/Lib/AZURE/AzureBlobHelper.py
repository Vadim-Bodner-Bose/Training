import re
from azure.storage.blob import BlobServiceClient
from Config.Azure_Config import BLOB_CONNECTION_STR, CONTAINER_NAME

class AzureBlobHelper:

    def version(self, version):
        major, minor, micro, build = re.search('(\d+)\.(\d+)\.(\d+)-(\d+)', version).groups()
        return int(major), int(minor), int(micro), int(build)

    def get_latest_version(self):
        kduo_list = []
        for blob in self.get_blob_list():
            if blob.name[:4] == "KDuo" and "test" not in blob.name and "dev" not in blob.name:
                kduo_list.append(re.sub('-?(RC|rc).?\\d+', "", blob.name))
        latest = max(kduo_list, key=self.version)
        return latest, latest[5:-4]

    def get_blob_list(self):
        try:
            blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STR)

            # Connect to the container
            container_client = blob_service_client.get_container_client(CONTAINER_NAME)

            # List the blobs in the container
            blob_list = container_client.list_blobs()

            return blob_list

        except Exception as ex:
            print('Exception:')
            print(ex)





