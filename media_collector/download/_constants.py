"""视频下载常量。"""

from pathlib import Path


def _storage_root() -> Path:
    """独立运行时用本仓库根目录；作为 media-factory 子仓库时用工厂根目录。"""
    here = Path(__file__).resolve()
    for parent in here.parents:
        git_dir = parent / ".git"
        if not git_dir.is_dir():
            continue
        if (parent / "core").is_dir():
            return parent
        if (parent / "media_collector").is_dir():
            return parent
    return here.parents[2]


_STORAGE_ROOT = _storage_root()
DEFAULT_VIDEO_DIR = _STORAGE_ROOT / "data" / "download" / "videos"
# 手动登录 Cookie 目录（Netscape 格式），<platform>.txt 优先于自动访客 Cookie。
MANUAL_COOKIE_DIR = _STORAGE_ROOT / "data" / "download" / "cookies"

DOWNLOAD_TIMEOUT_SECONDS = 600
DOWNLOAD_CONNECT_TIMEOUT_SECONDS = 30
MUX_TIMEOUT_SECONDS = 120
PARSE_SOCKET_TIMEOUT_SECONDS = 30

DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)
DEFAULT_REFERER = "https://www.douyin.com/"

# 各平台解析与下载时的 Referer（抖音不走 yt-dlp，见 _douyin.py）。
PLATFORM_REFERER = {
    "bilibili": "https://www.bilibili.com/",
    "weibo": "https://weibo.com/",
    "xhs": "https://www.xiaohongshu.com/",
    "youtube": "https://www.youtube.com/",
    "tiktok": "https://www.tiktok.com/",
    "kuaishou": "https://www.kuaishou.com/",
}

# 对外返回的中文名（douyin_research 等调用方依赖"抖音"字面量）。
PLATFORM_NAMES = {
    "douyin": "抖音",
    "bilibili": "哔哩哔哩",
    "weibo": "微博",
    "xhs": "小红书",
    "youtube": "YouTube",
    "tiktok": "TikTok",
    "kuaishou": "快手",
    "wechat": "微信视频号",
    "auto": "其他",
}
