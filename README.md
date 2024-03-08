# xhs_media_parser

这是一个使用 [XHS-Downloader](https://github.com/JoeanAmier/XHS-Downloader.git) 作为解析核心的工具，主要提供视频下载链接和作品信息解析的 API。

两种方式部署使用：

1. 直接运行：安装依赖，直接 python 运行；
2. Docker 部署：自定义配置文件并构建镜像，通过镜像启动容器部署。

## 准备工作

开始之前，拉取代码，本项目使用其他仓库作为子模块。

```shell
git clone --recurse-submodules https://github.com/okooo5km/xhs_media_parser
cd xhs_media_parser
```

自定义自己的配置，目录下复制 `config.example.toml` 文件到本目录，新配置文件命名为 `config.toml`，按需修改里面的配置即可。其中注意修改 Cookie，下面是获取 Cookie 的步骤。

1. 打开浏览器（可选无痕模式启动），访问 <https://www.xiaohongshu.com/explore>
2. 按下 F12 打开开发人员工具
3. 选择 网络 选项卡
4. 选择 Fetch/XHR 筛选器
5. 点击小红书页面任意作品
6. 在 网络 选项卡挑选包含 Cookie 的数据包
7. 检查 Cookie 是否包含 web_session 字段
8. 全选复制包含 web_session 字段的 Cookie

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

## Endpoints

部署成功后可以通过 `https://127.0.0.1:8000/docs` 查看接口信息。

目前只有一个：`/parse`：

POST 方法，数据为 json 格式：

```json
{
    "urls": [
        "xxxx",
        "xxxx"
    ]
}
```

响应数据格式形如：

```json
[
  {
    "收藏数量": "425",
    "评论数量": "100",
    "分享数量": "68",
    "点赞数量": "4629",
    "作品标签": [],
    "作品ID": "6014db730000000001008878",
    "作品标题": "深山偶遇钩距虾脊兰",
    "作品描述": "钩距虾脊兰 Calanthe graciliflora Hayata\n兰科 Orchidaceae\n虾脊兰属 Calanthe",
    "作品类型": "视频",
    "IP归属地": "",
    "发布时间": "2021-01-30_12:07:15",
    "最后更新时间": "2021-01-30_12:07:15",
    "作者昵称": "一方见地",
    "作者ID": "5f05aff80000000001007117",
    "下载地址": [
      "https://sns-video-hw.xhscdn.com/spectrum/8bb83aa13b9a1bbc5dc4f5d93d55c2509cab63eb"
    ]
  }
]
```

## 免责声明

- 使用者对本项目的使用由使用者自行决定，并自行承担风险。
- 作者对使用者使用本项目所产生的任何损失、责任、或风险概不负责。
- 本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。
- 作者尽力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。
- 使用者在使用本项目时必须严格遵守 GNU General Public License v3.0 的要求，并在适当的地方注明使用了 GNU General Public License v3.0 的代码。
- 使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。
- 使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。
- 本项目的作者不会提供 XHS-Downloader 项目的付费版本，也不会提供与 XHS-Downloader 项目相关的任何商业服务。
- 基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的各种情况负全部责任。

在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险和后果。
