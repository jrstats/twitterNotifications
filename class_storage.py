import azure.storage.blob as blob

class StorageBlob:
    def __init__(self, url, key, container, filename):
        self.bsc = blob.BlobServiceClient(url, key)
        self.container = container
        self.filename = filename

    @classmethod
    def fromDict(cls, keys):
        url = keys["blob_url"]
        key = keys["blob_key"]
        container = keys["blob_container"]
        filename = keys["blob_filename"]
        return cls(url, key, container, filename)

    def download(self, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename

        bc = self.bsc.get_blob_client(container, filename)

        try:
            return bc.download_blob().content_as_text()
        except:
            return ""


    def upload(self, data, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename
        bc = self.bsc.get_blob_client(container, filename)
        bc.upload_blob(data)

        


class StorageCosmos:
    def __init__(self, url, key, container, filename):
        self.bsc = blob.BlobServiceClient(url, key)
        self.container = container
        self.filename = filename

    @classmethod
    def fromDict(cls, keys):
        url = keys["blob_url"]
        key = keys["blob_key"]
        container = keys["blob_container"]
        filename = keys["blob_filename"]
        return cls(url, key, container, filename)

    def download(self, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename

        bc = self.bsc.get_blob_client(container, filename)

        try:
            return bc.download_blob().content_as_text()
        except:
            return ""


    def upload(self, data, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename
        bc = self.bsc.get_blob_client(container, filename)
        bc.upload_blob(data)

        
class StorageFile:
    def __init__(self, url, key, container, filename):
        self.bsc = blob.BlobServiceClient(url, key)
        self.container = container
        self.filename = filename

    @classmethod
    def fromDict(cls, keys):
        url = keys["blob_url"]
        key = keys["blob_key"]
        container = keys["blob_container"]
        filename = keys["blob_filename"]
        return cls(url, key, container, filename)

    def download(self, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename

        bc = self.bsc.get_blob_client(container, filename)

        try:
            return bc.download_blob().content_as_text()
        except:
            return ""


    def upload(self, data, filename=None, container=None):
        if container is None:
            container = self.container
        if filename is None:
            filename = self.filename
        bc = self.bsc.get_blob_client(container, filename)
        bc.upload_blob(data)

        