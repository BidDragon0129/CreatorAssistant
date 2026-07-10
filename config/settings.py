"""
Creator Assistant Settings Models

This module contains strongly typed configuration objects
used throughout the application.
"""

from __future__ import annotations
from dataclasses import dataclass

# ==================================
# Discord settings
# ==================================
@dataclass(slots=True)
class DiscordSettings:
    "Discord bot configuration"

    token: str
    guild_id: int
    prefix: str


# =================================
# Database settings
# =================================

@dataclass(slots=True)
class DatabaseSettings:
    "Database Configuration"

    path: str

# =================================
# Logging Settings
# =================================

@dataclass(slots=True)
class LoggingSettings:
    "Application logging configuration"

    level: str
    folder: str
    filename: str = "creator_assistant.log"

# ===================================
# OBS Settings
# ===================================

@dataclass(slots=True)
class OBSSettings:
    "Obs Websocket Configuration"
    
    host: str
    port: int
    password: str

# ===================================
# Application Settings
# ===================================

@dataclass(slots=True)
class ApplicationSettings:
    "General Application configuration"

    name: str
    version: str
    debug: bool