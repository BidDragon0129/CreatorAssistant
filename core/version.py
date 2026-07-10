"""
Application version information.
"""

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class AppInfo:
    # Static application information
    NAME: str = "Creator Assistant"
    DESCRIPTION: str = (
        "A modular content creation assistant for streamers."
    )

    AUTHOR: str = "Jay, and Pip"
    VERSION: str = "0.0.1"
    COPYRIGHT: str= "COPYRIGHT (C) 2026 Jay, and Pip. All rights reserved."
    LICENSE: str = "MIT License"
    REPOSITORY: str = ("https://github.com/BidDragon0129/CreatorAssistant")
    PYTHON_REQUIRED: str = ">=3.12"
    BUILD: str = "Development"
    CODENAME: str= "Foundation"

APP = AppInfo()