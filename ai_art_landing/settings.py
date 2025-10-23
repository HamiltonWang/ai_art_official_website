from pathlib import Path
from time import time
from dataclasses import dataclass, field
from typing import Any, List, Optional, Type


def static_url_for(static: str, path: str) -> str:
    return f"/{static}/{path}?v={settings.server_startup_time}"


@dataclass
class TransientSettings:

    # Indicates that the server should continue to run.
    # When set to false it indicates that the shutdown procedure is ongoing.
    # If false no new tasks, threads, etc should be started.
    # Long-running while loops should use this flag instead of `while True:`
    app_running: bool = field(default=True)


@dataclass
class ThemesSettings:
    app_site_title: str = field(default="AI Art")
    app_site_tagline: str = field(default="path to financial freedom")
    app_site_description: str = field(
        default="The world's most powerful suite of bitcoin tools."
    )


@dataclass
class EnvSettings:
    debug: bool = field(default=True)
    bundle_assets: bool = field(default=True)
    host: str = field(default="127.0.0.1")
    port: int = field(default=5000)
    forwarded_allow_ips: str = field(default="*")
    app_title: str = field(default="AI Art official website")
    app_path: str = field(default=".")
    version: str = field(default="0.0.1")
    user_agent: str = field(default="")
    enable_log_to_file: bool = field(default=True)
    log_rotation: str = field(default="100 MB")
    log_retention: str = field(default="3 months")
    server_startup_time: int = field(default=time())

    app_data_folder: str = field(default="./data")
    app_baseurl = "https://aiart.io/"


class Settings(EnvSettings, TransientSettings, ThemesSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        # json_loads = list_parse_fallback


def set_cli_settings(**kwargs):
    for key, value in kwargs.items():
        setattr(settings, key, value)


settings = Settings()
