import os
import urllib3
from minio import Minio
from minio.deleteobjects import DeleteObject
from dotenv import load_dotenv

load_dotenv()

# 是否設定Proxy
PROXY_ADDRESS = os.environ.get("PROXY_ADDRESS")

# Minio存取設置
ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
MINIO_HOST = os.environ.get("MINIO_HOST")
MINIO_PORT = os.environ.get("MINIO_PORT")
MINIO_API_HOST = f"http:{MINIO_HOST}:{MINIO_PORT}"
MINIO_ENDPOINT = f"{MINIO_HOST}:{MINIO_PORT}"

# Minio Bucket名稱
MINIO_BUCKET = os.environ.get("MINIO_BUCKET")
MINIO_RESOURCE_PATH = os.environ.get("MINIO_RESOURCE_PATH")

def main():

   if PROXY_ADDRESS:
      print("with proxy")
      http_client=urllib3.ProxyManager(proxy_url=PROXY_ADDRESS)
      MINIO_CLIENT = Minio(MINIO_ENDPOINT, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False, http_client=http_client)
   else:
      print("without proxy")
      MINIO_CLIENT = Minio(MINIO_ENDPOINT, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

   MINIO_CLIENT.remove_object(bucket_name=MINIO_BUCKET, object_name=MINIO_RESOURCE_PATH)
   print(f"It is successfully delete file: {MINIO_RESOURCE_PATH}  in {MINIO_BUCKET} bucket")

if __name__ == "__main__":
    main()