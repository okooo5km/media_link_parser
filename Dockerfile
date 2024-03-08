# 使用官方 Python 3.12 基础镜像
FROM python:3.12-slim-buster

# 设置工作目录
WORKDIR /app

# 将当前目录的内容复制到工作目录中
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行 xhs.py 文件
CMD ["python3", "xhs.py"]