
"""
Creator Assistant Configuration Manager

Responsible for loading environment variables,
creating settings objects, validating configuration,
and preparing application directories.
"""

from __future__ import annotations
from pathlib import Path
from dotenv import load_dotenv

import os
from config.defaults import (
    DEFAULT_ASSET_FOLDER,
    DEFAULT_CLIP_FOLDER,
    DEFAULT_DATA_FOLDER,
    DEFAULT_DATABASE,
    DEFAULT_DEBUG,
    DEFAULT_LOG_FOLDER,
    DEFAULT_LOG_LEVEL,
    DEFAULT_RECORDING_FOLDER,
    DEFAULT_PREFIX,
    DEFAULT_OBS_HOST,
    DEFAULT_OBS_PORT
)

from config.settings import (
    ApplicationSettings,
    DatabaseSettings,
    DiscordSettings,
    LoggingSettings,
    OBSSettings,
)

class Config:
    """
    Main application configuration
    
    This class should be the only place 
    that directly accesses environment variables.
    """

    def __init__(self) -> None:
        # Load .env file
        load_dotenv()

        # General Application
        self.application = ApplicationSettings(
            name="Creator Assistant",
            version= "0.1.0",
            debug= self._get_bool(
                "DEBUG",
                DEFAULT_DEBUG
            ),
        )

        # Discord
        self.discord = DiscordSettings(
            token = self._get_required(
                "DISCORD_TOKEN"
            ),

            guild_id=self._get_int(
                "DISCORD_GUILD_ID",
                0
            ),

            prefix=os.getenv(
                "BOT_PREFIX",
                DEFAULT_PREFIX,
            ),
        )

        self.database = DatabaseSettings(
            path=os.getenv(
                "DATABASE_PATH",
                str(DEFAULT_DATABASE),
            )
        )

        self.logging = LoggingSettings(
            level=os.getenv(
                "LOG_LEVEL",
                DEFAULT_LOG_LEVEL,
            ),

            folder=str(
                DEFAULT_LOG_FOLDER
            ),
        )

        # OBS
        self.obs = OBSSettings(
            host=os.getenv(
                "OBS_HOST",
                DEFAULT_OBS_HOST,
            ),

            port=self._get_int(
                "OBS_PORT",
                DEFAULT_OBS_PORT,
            ),

            password=os.getenv(
                "OBS_PASSWORD",
                ""
            ),
        )

        # Create required folders
        self._create_directories()



    # ====================================
    # Environment Helpers
    # ====================================
    @staticmethod
    def _get_required(name: str) -> str:
        "Get required environment variable."

        value = os.getenv(name)
        if not value:
            raise EnvironmentError(f"Missing required environment variable: {name}")
        
        return value
    
    @staticmethod
    def _get_int(
        name: str,
        default: int
    )-> int:
        
        "Convert environment variable to integer."
        value = os.getenv(name)
        if value is None:
            return default
        
        try:
            return int(value)
        except ValueError:
            raise ValueError(
                f"{name} must be an integer."
            )
    
    @staticmethod
    def _get_bool(
        name: str,
        default: bool
    ) -> bool:
        "Convert environment variable to boolean"

        value = os.getenv(name)

        if value is None:
            return default
        
        return value.lower() in (
            "true",
            "1",
            "yes",
            "y"
        )

    # ==================================
    # Folder Creation
    # ==================================
    @staticmethod
    def _create_directories() -> None:
        "Create application folders"

        folders = [
            DEFAULT_DATA_FOLDER,
            DEFAULT_LOG_FOLDER,
            DEFAULT_CLIP_FOLDER,
            DEFAULT_RECORDING_FOLDER,
            DEFAULT_ASSET_FOLDER,
        ]

        for folder in folders:
            Path(folder).mkdir(
                parents=True,
                exist_ok=True,
            )

    # ================================================================
    # DEBUG INFORMATION
    # ================================================================
    def summary(self) -> str:
        """ 
        Returns safe configuration information.
        Does not expose secrets.
        """

        return (
            "\n"
            "==============================\n"
            " Creator Assistant Config\n"
            "==============================\n"
            f"Application: {self.application.name}\n"
            f"Version: {self.application.version}\n"
            f"Debug: {self.application.debug}\n"
            "\n"
            f"Guild ID: {self.discord.guild_id}\n"
            f"Prefix: {self.discord.prefix}\n"
            "\n"
            f"Database: {self.database.path}\n"
            f"Log Level: {self.logging.level}\n"
            "\n"
            f"OBS Host: {self.obs.host}\n"
            f"OBS Port: {self.obs.port}\n"
            "==============================\n"
        )