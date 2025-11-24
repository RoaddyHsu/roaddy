"""
配置載入模組
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv


class ConfigLoader:
    """配置載入器"""

    def __init__(self, config_path: str = None):
        """
        初始化配置載入器

        Args:
            config_path: 配置文件路徑
        """
        # 載入環境變數
        load_dotenv()

        # 設定配置文件路徑
        if config_path is None:
            project_root = Path(__file__).parent.parent.parent
            config_path = project_root / "config" / "config.yaml"

        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        載入配置文件

        Returns:
            配置字典
        """
        if not self.config_path.exists():
            raise FileNotFoundError(f"配置文件不存在: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get(self, key: str, default: Any = None) -> Any:
        """
        獲取配置值

        Args:
            key: 配置鍵（支持點號分隔的多層級鍵，如 "assistants.content_marketing.model"）
            default: 默認值

        Returns:
            配置值
        """
        keys = key.split(".")
        value = self.config

        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
                if value is None:
                    return default
            else:
                return default

        return value

    def get_assistant_config(self, assistant_type: str) -> Dict[str, Any]:
        """
        獲取助手配置

        Args:
            assistant_type: 助手類型

        Returns:
            助手配置字典
        """
        return self.get(f"assistants.{assistant_type}", {})

    def get_api_key(self, service: str) -> str:
        """
        從環境變數獲取 API 金鑰

        Args:
            service: 服務名稱（如 "OPENAI", "ANTHROPIC", "GOOGLE"）

        Returns:
            API 金鑰

        Raises:
            ValueError: 如果 API 金鑰未設定
        """
        key_name = f"{service.upper()}_API_KEY"
        api_key = os.getenv(key_name)

        if not api_key:
            raise ValueError(f"請在 .env 文件中設定 {key_name}")

        return api_key


# 全局配置實例
config = ConfigLoader()
