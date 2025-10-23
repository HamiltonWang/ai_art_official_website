import logging
import sys
from pathlib import Path

from loguru import logger

from ai_art_landing.settings import settings


def log_server_info():
    logger.info("Starting AI Art Landing")
    logger.info(f"Version: {settings.version}")
    logger.info(f"Baseurl: {settings.app_baseurl}")
    logger.info(f"Host: {settings.host}")
    logger.info(f"Port: {settings.port}")
    logger.info(f"Debug: {settings.debug}")
    logger.info(f"Site title: {settings.app_site_title}")
    logger.info(f"Data folder: {settings.app_data_folder}")


def configure_logger() -> None:
    logger.remove()
    log_level: str = "DEBUG" if settings.debug else "INFO"
    formatter = Formatter()
    logger.add(sys.stdout, level=log_level, format=formatter.format)

    if settings.enable_log_to_file:
        logger.add(
            Path(settings.app_data_folder, "logs", "app.log"),
            rotation=settings.log_rotation,
            retention=settings.log_retention,
            level="INFO",
            format=formatter.format,
        )
        logger.add(
            Path(settings.app_data_folder, "logs", "debug.log"),
            rotation=settings.log_rotation,
            retention=settings.log_retention,
            level="DEBUG",
            format=formatter.format,
        )

    logging.getLogger("uvicorn").handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.error").handlers = [InterceptHandler()]
    logging.getLogger("uvicorn.error").propagate = False

    logging.getLogger("sqlalchemy").handlers = [InterceptHandler()]
    logging.getLogger("sqlalchemy.engine.base").handlers = [InterceptHandler()]
    logging.getLogger("sqlalchemy.engine.base").propagate = False
    logging.getLogger("sqlalchemy.engine.base.Engine").handlers = [InterceptHandler()]
    logging.getLogger("sqlalchemy.engine.base.Engine").propagate = False


class Formatter:
    def __init__(self):
        self.padding = 0
        self.minimal_fmt = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SS}</green> | <level>{level}</level> | "
            "<level>{message}</level>\n"
        )
        if settings.debug:
            self.fmt = (
                "<green>{time:YYYY-MM-DD HH:mm:ss.SS}</green> | "
                "<level>{level: <4}</level> | "
                "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
                "<level>{message}</level>\n"
            )
        else:
            self.fmt = self.minimal_fmt

    def format(self, record):
        function = "{function}".format(**record)
        if function == "emit":  # uvicorn logs
            return self.minimal_fmt
        return self.fmt


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        logger.log(level, record.getMessage())
