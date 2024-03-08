# xhs_media_parser

这是一个使用 [XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader.git) 作为解析核心的 Web API 服务工具。通过这个项目，可以简单构建解析小红书视频下载链接的 API，仅用于学习和验证技术方案使用。

两种方式部署使用：

1. 直接运行：安装依赖，直接 python 运行；
2. Docker 部署：自定义配置文件并构建镜像，通过镜像启动容器部署。

## 准备工作

开始之前，拉取代码，本项目使用其他仓库作为子模块。

```shell
git clone --recurse-submodules https://github.com/okooo5km/xhs_media_parser
cd xhs_media_parser
```

自定义自己的配置，目录下复制 `config.example.toml` 文件到本目录，新配置文件命名为 `config.toml`，按需修改里面的配置即可。

## 部署

```shell
cp config.example.toml config.toml
```

### 直接运行

1. Python 3.12 及以上版本。
2. 通过命令 `pip install -r requirements.txt` 安装必要的依赖。

直接运行

```shell
python xhs.py
```

### Docker 部署

需要安装 Docker。

#### 制作镜像

```shell
docker build -t xhs-media-parser .
```

#### 启动容器

```shell
docker run -p 8000:8000 xhs-media-parser
```
