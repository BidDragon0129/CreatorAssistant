import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from config import Config
def test_config_loads():
    config = Config()

    assert config.application.name == "Creator Assistant"
    assert config.discord.prefix == "$"