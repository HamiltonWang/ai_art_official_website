import json
import re

from pathlib import Path
from typing import Any, List, Optional, Type

import jinja2

from ai_art_landing.jinja2_templating import Jinja2Templates
from ai_art_landing.settings import settings, static_url_for


def template_renderer() -> Jinja2Templates:
    folders = ["ai_art_landing/templates", "ai_art_landing/core/templates"]

    t = Jinja2Templates(loader=jinja2.FileSystemLoader(folders))
    t.env.globals["static_url_for"] = static_url_for

    t.env.globals["SITE_TITLE"] = settings.app_title
    t.env.globals["APP_VERSION"] = settings.version

    if settings.bundle_assets:
        t.env.globals["INCLUDED_JS"] = []
        t.env.globals["INCLUDED_CSS"] = [
                                         "dist/libs/tiny-slider/tiny-slider.css",
                                         "dist/libs/tobii/css/tobii.min.css",
                                         "dist/libs/@iconscout/unicons/css/line.css",
                                         "dist/libs/@mdi/font/css/materialdesignicons.min.css",
                                         "dist/css/tailwind.css"]
    else:
        vendor_filepath = Path(settings.app_path, "static", "vendor.json")
        with open(vendor_filepath) as vendor_file:
            vendor_files = json.loads(vendor_file.read())
            t.env.globals["INCLUDED_JS"] = vendor_files["js"]
            t.env.globals["INCLUDED_CSS"] = vendor_files["css"]

    return t
