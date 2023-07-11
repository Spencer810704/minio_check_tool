
# 產生.env file

```
cat << EOF > .env
# Proxy地址
PROXY_ADDRESS="http://10.15.12.202:8888/"

# Minio 帳號&密碼
ACCESS_KEY="change to your username"
SECRET_KEY="change to your password"

# Minio 主機、Port、Scheme
MINIO_HOST="minio.pf.stg"
MINIO_PORT="9000"
MINIO_SCHEME="http"

# Bucket名稱
MINIO_BUCKET="mps"
MINIO_RESOURCE_PATH="testfile.png"

# 上傳檔案路徑
UPLOADED_FILE_PATH="./image/upload/testfile.png"

# 下載檔案路徑
DOWNLOADED_FILE_PATH="./image/download/testfile.png"

EOF

```