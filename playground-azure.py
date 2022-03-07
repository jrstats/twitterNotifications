import azure.storage.blob as blob
import json
import pandas as pd
from io import StringIO

with open("TimerTrigger1/keys.json", "r") as f:
    keys = json.load(f)

filepath = "test.txt"
bsc = blob.BlobServiceClient(keys["blob_url"], keys["blob_key"])
bc = bsc.get_blob_client(keys["blob_container"], filepath)
bc.upload_blob(pd.DataFrame([[1], [2], [3]]).to_csv(index=False), overwrite=True)
# print(pd.DataFrame(bc.download_blob().content_as_text()))
print(pd.read_csv(StringIO(bc.download_blob().content_as_text())))
# blob.BlobClient().append_block()
