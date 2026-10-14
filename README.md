# media-collector

媒体采集库。当前提供分享链接和口令的视频下载，后续采集能力从 `media_collector` 入口继续扩展。

采用 MIT 许可证。

## 入口

```python
from media_collector import download, DownloadError
```

`download(share_text, output_path=None)` 解析分享文字或链接，下载为本地 mp4。

## 目录

```text
media_collector/
├── __init__.py      # 采集入口
└── download/        # 分享链接下载
```

## 在 media-factory 中

本仓库是 [media-factory](https://github.com/xdh5/media-factory) 的子仓库，路径为 `integrations/media-collector`。工厂代码通过 `core.tools.download` 转到这里。嵌在工厂里时，视频和 Cookie 写到工厂仓库的 `data/download/`。

独立运行时，这些文件写到本仓库的 `data/download/`。

下载细节见 [media_collector/download/download.md](media_collector/download/download.md)。
