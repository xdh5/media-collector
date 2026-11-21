"""采集库的可写工作目录与运行配置。"""

import os
from pathlib import Path

from dotenv import load_dotenv


def workspace_root() -> Path:
    return Path(os.getenv("MEDIA_COLLECTOR_WORKSPACE", Path.cwd())).resolve()


def load_configuration() -> None:
    load_dotenv(Path(os.getenv("MEDIA_COLLECTOR_ENV_FILE", workspace_root() / ".env")), override=False)
