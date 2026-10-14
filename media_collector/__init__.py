"""媒体采集入口。

当前能力是分享链接下载。后续采集能力从这里继续导出。
"""

from .download import DownloadError, download, extract_url, extract_urls

__all__ = [
    "DownloadError",
    "download",
    "extract_url",
    "extract_urls",
]
