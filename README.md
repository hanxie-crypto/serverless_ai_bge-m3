# 环境及版本
python3.10-3.12

# 模型下载
aria2c --disable-ipv6 --input-file links.txt --dir app/models/bge-m3

# 依赖安装，在根目录

pip3 install -r app/embedding/requirements.txt

# 启动，在根目录
python3 app/embedding/app/main.py

# 构建镜像

构建镜像需要先完成模型下载