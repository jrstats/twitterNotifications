from fileinput import filename
import azure.storage.blob as blob
import azure.cosmos as cosmos
import json

class StorageBlob:
    def __init__(self, url, key, container, filename):
        self.container = container
        self.filename = filename
        self.storage_client = blob.BlobServiceClient(url, key)
        self.blob_client = self.storage_client.get_blob_client(container, filename)
        
    def _getBlobClient(self, filename=None, container=None):
        ## check to see if parameters have been passed
        ## otherwise, use defaults
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename
        
        ## use appropriate blob_client
        if (container == self.container) and (filename == self.filename):
            blob_client = self.blob_client
        else:
            blob_client = self.storage_client.get_blob_client(container, filename)

        return blob_client

    @classmethod
    def fromDict(cls, keys):
        url = keys["blob_url"]
        key = keys["blob_key"]
        container = keys["blob_container"]
        filename = keys["blob_filename"]
        return cls(url, key, container, filename)

    def download(self, filename=None, container=None):
        blob_client = self._getBlobClient(filename, container)

        ## read data
        try:
            return blob_client.download_blob().content_as_text()
        except:
            return ""


    def upload(self, data, filename=None, container=None):
        blob_client = self._getBlobClient(filename, container)
        blob_client.upload_blob(data)

        


class StorageCosmos:
    def __init__(self, url, key, database, container):
        self.database = database
        self.container = container
        self.storage_client = cosmos.CosmosClient(url, key)
        self.database_client = self.storage_client.get_database_client(database)
        self.container_client = self.database_client.get_container_client(container)

    def _getContainerClient(self, database=None, container=None):
        ## check to see if parameters have been passed
        ## otherwise, use defaults
        if database is None:
            database_client = self.database_client
        else:
            database_client = self.storage_client.get_database_client(database)
        
        if container is None:
            container_client = self.container_client
        else:
            container_client = database_client.get_container_client(container)
        
        return container_client

    @staticmethod
    def _dataToStr(data):
        return "\n".join([json.dumps(d)["id"] for d in data])

    @staticmethod
    def _strToData(x):
        pass

    @classmethod
    def fromDict(cls, keys):
        url = keys["cosmos_url"]
        key = keys["cosmos_key"]
        database = keys["cosmos_database"]
        container = keys["cosmos_container"]
        return cls(url, key, database, container)

    def download(self, database=None, container=None):
        container_client = self._getContainerClient(database, container)

        try:
            items = container_client.query_items("select id from mycontainer")
            return self._dataToStr(items)
        except:
            return ""


    def upload(self, data, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename
        bc = self.storage_client.get_blob_client(container, filename)
        bc.upload_blob(data)

        
class StorageFile:
    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def fromDict(cls, keys):
        filename = keys["filename"]
        return cls(filename)

    def download(self, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename

        bc = self.storage_client.get_blob_client(container, filename)

        try:
            return bc.download_blob().content_as_text()
        except:
            return ""


    def upload(self, data, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename
        bc = self.storage_client.get_blob_client(container, filename)
        bc.upload_blob(data)

        