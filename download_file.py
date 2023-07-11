import os
import urllib3
from minio import Minio
from dotenv import load_dotenv

load_dotenv()

# 上傳檔案路徑
DOWNLOADED_FILE_PATH = os.environ.get("DOWNLOADED_FILE_PATH")

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

   MINIO_CLIENT.fget_object(bucket_name=MINIO_BUCKET, object_name=MINIO_RESOURCE_PATH, file_path=DOWNLOADED_FILE_PATH)
   print("It is successfully downloaded from bucket")

if __name__ == "__main__":
    main()