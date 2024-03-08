from typing import List, Optional
import os
import sys
import toml
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

sys.path.append(os.path.abspath('XHS-Downloader'))


class UrlData(BaseModel):
    urls: List[str]


class Configuration(BaseModel):
    work_path: str  # 作品数据/文件保存根路径，默认值：项目根路径
    folder_name: str  # 作品文件储存文件夹名称（自动创建），默认值：Download
    user_agent: str  # 请求头 User-Agent，可选参数
    cookie: str  # 小红书网页版 Cookie，无需登录，必需参数
    proxy: Optional[str]  # 网络代理
    timeout: int  # 请求数据超时限制，单位：秒，默认值：10
    chunk: int  # 下载文件时，每次从服务器获取的数据块大小，单位：字节
    max_retry: int  # 请求数据失败时，重试的最大次数，单位：秒，默认值：5
    record_data: bool  # 是否记录作品数据至文件
    image_format: str  # 图文作品文件下载格式，支持：PNG、WEBP
    folder_mode: bool  # 是否将每个作品的文件储存至单独的文件夹
    download: bool  # 是否下载作品文件，默认值：False
    efficient: bool  # 高效模式，禁用请求延时


# 读取配置文件
config_file = "config.toml"
if not os.path.exists("config.toml"):
    config_file = "config.example.toml"
config = toml.load(config_file)

# 解析到配置模型
config = Configuration(**config)

sys.path.append(os.path.abspath('XHS-Downloader'))

app = FastAPI()


async def parse_xhs_videos(urls: List[str] = ["https://www.xiaohongshu.com/explore/65c37cce000000002c02a59b"]):
    multiple_links = " ".join(urls)
    from source import XHS
    async with XHS(work_path=config.work_path,
                   folder_name=config.folder_name,
                   user_agent=config.user_agent,
                   cookie=config.cookie,
                   proxy=config.proxy,
                   timeout=config.timeout,
                   chunk=config.chunk,
                   max_retry=config.max_retry,
                   record_data=config.record_data,
                   image_format=config.image_format,
                   folder_mode=config.folder_mode) as xhs:  # 使用自定义参数
        # 返回作品详细信息，包括下载地址
        info = await xhs.extract(multiple_links, config.download, config.efficient)
        return info


@app.post("/xhs")
async def parse(urls: UrlData):
    return await parse_xhs_videos(urls.urls)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
