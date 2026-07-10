"""
Creator Assistant Default Configuration

This module contains the default values used throughout the application
whenever a value is not provided in the environment configureation.
"""

from __future__ import annotations
from pathlib import Path

# ===========================
#          APPLCATION
# ===========================
APP_NAME = "CREATOR_ASSISTANT"
APP_VERSION = "0.1.0"
APP_CODENAME = "Foundation"

# ===========================
#        GENERAL
# ===========================
DEFAULT_DEBUG = False
DEFAULT_PREFIX = "$"
DEFAULT_TIMEZONE = "EST"

# ===========================
#         DIRECTORIES
# ===========================
DEFAULT_DATA_FOLDER = Path("data")
DEFAULT_LOG_FOLDER = Path("logs")
DEFAULT_CLIP_FOLDER = Path("clips")
DEFAULT_RECORDING_FOLDER = Path("recordings")
DEFAULT_ASSET_FOLDER = Path("assets")
DEFAULT_BACKUP_FOLDER = Path("backups")

# ===========================
#          LOGGING
# ===========================

DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_LOG_FILE = "creator_assistant.log"

# ===========================
#           DATABASE
# ===========================

DEFAULT_DATABASE = DEFAULT_DATA_FOLDER / "creator.db"

# ===========================
#            DISCORD
# ===========================

DEFAULT_COMMAND_PREFIX = "$"
DEFAULT_ACTIVITY = "Helping creators build content!"

# ===========================
#             OBS
# ===========================

DEFAULT_OBS_HOST = "localhost"
DEFAULT_OBS_PORT = 4455

# ===========================
#             DASHBOARD
# ===========================

DEFAULT_DASHBOARD_HOST = "localhost"
DEFAULT_DASHBOARD_PORT = 8000

# ===========================
#             SCHEDULER
# ===========================

DEFAULT_BACKUP_INTERVAL_HOURS = 24
DEFAULT_SAVE_INTERVAL_MINUTES = 15

# ===========================
#             MEDIA
# ===========================

DEFAULT_CLIP_EXTENSION = ".mp4"
DEFAULT_IMAGE_EXTENSION = ".png"

# ===========================
#             GITHUB
# ===========================

DEFAULT_BRANCH = "main"

# ===========================
#             API TIMEOUTS
# ===========================

DEFAULT_HTTP_TIMEOUT = 30

# ===========================
#             RETRY SETTINGS
# ===========================

DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_DELAY = 5