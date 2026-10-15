# media-collector

媒体采集库。下载视频和获取作者作品列表都在 `core` 目录。

采用 MIT 许可证。

## 入口

把 `core` 放进 Python 路径后：

```python
from download_video import download, DownloadError
from list_author_works import list_author_works
```

`download(share_text, output_path=None)` 解析分享文字或链接，下载为本地 mp4。

`list_author_works(profile_url, limit)` 按发布时间从新到旧返回作者作品。作品链接可再交给 `download`。

## 目录

```text
core/
├── download_video/       # 下载视频
└── list_author_works/    # 获取作者作品列表
```

## 在 media-factory 中

本仓库是 [media-factory](https://github.com/xdh5/media-factory) 的子仓库，路径为 `integrations/media-collector`。工厂导入 `core` 时会把这里的 `core` 目录放进 Python 路径，然后调用 `download_video` 和 `list_author_works`。嵌在工厂里时，视频和 Cookie 写到工厂仓库的 `data/download/`。

独立运行时，这些文件写到本仓库的 `data/download/`。

下载细节见 [core/download_video/download.md](core/download_video/download.md)。作者作品列表见 [core/list_author_works/list_author_works.md](core/list_author_works/list_author_works.md)。
