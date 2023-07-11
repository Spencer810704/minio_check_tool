Table of contents
- [簡介](#簡介)
- [安裝](#安裝)
  - [產生配置檔 (.env)](#產生配置檔-env)
- [使用](#使用)
  - [測試新增檔案](#測試新增檔案)
  - [測試下載檔案](#測試下載檔案)
  - [測試刪除檔案](#測試刪除檔案)

# 簡介
因一次線上故障 , 當時無法快速定位出是應用層面 , 亦或是Forward Proxy的問題 , 故撰寫腳本進行快速測試 , 


以下為工具安裝方式

<br>


# 安裝

```
# Clone專案
git clone https://github.com/Spencer810704/minio_check_tool

# 切換目錄
cd minio_check_tool

# 安裝套件
pip install -r requirements.txt
```

<br>

## 產生配置檔 (.env)

```
cat << EOF > .env
# Proxy 地址
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

<br>

# 使用

<br>

## 測試新增檔案
```shell
python upload_file.py
```

<br>

## 測試下載檔案
```shell
python download_file.py
```

<br>

## 測試刪除檔案
```shell
python delete_file.py

```

<br>
