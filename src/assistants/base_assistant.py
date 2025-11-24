"""
基礎助手類別
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any
from ..api import OpenAIClient, AnthropicClient
from ..utils.logger import logger
from ..utils.config_loader import config


class BaseAssistant(ABC):
    """基礎助手抽象類別"""

    def __init__(
        self,
        assistant_type: str,
        system_prompt: str,
        use_anthropic: bool = True,
    ):
        """
        初始化助手

        Args:
            assistant_type: 助手類型
            system_prompt: 系統提示詞
            use_anthropic: 是否使用 Anthropic (Claude)
        """
        self.assistant_type = assistant_type
        self.system_prompt = system_prompt
        self.conversation_history: List[Dict[str, str]] = []

        # 載入配置
        self.config = config.get_assistant_config(assistant_type)
        model = self.config.get("model", "claude-3-5-sonnet-20241022")
        self.temperature = self.config.get("temperature", 0.7)
        self.max_tokens = self.config.get("max_tokens", 4096)

        # 初始化客戶端
        if use_anthropic or "claude" in model.lower():
            self.client = AnthropicClient(model=model)
            self.use_anthropic = True
        else:
            self.client = OpenAIClient(model=model)
            self.use_anthropic = False

        logger.info(f"{self.assistant_type} 助手初始化完成")

    def add_message(self, role: str, content: str) -> None:
        """
        添加訊息到對話歷史

        Args:
            role: 角色 (user/assistant)
            content: 訊息內容
        """
        self.conversation_history.append({"role": role, "content": content})

    def clear_history(self) -> None:
        """清空對話歷史"""
        self.conversation_history = []
        logger.info(f"{self.assistant_type} 對話歷史已清空")

    def get_history(self) -> List[Dict[str, str]]:
        """
        獲取對話歷史

        Returns:
            對話歷史列表
        """
        return self.conversation_history.copy()

    def chat(self, user_message: str) -> str:
        """
        發送訊息並獲取回應

        Args:
            user_message: 用戶訊息

        Returns:
            助手回應
        """
        # 添加用戶訊息
        self.add_message("user", user_message)

        try:
            # 發送請求
            if self.use_anthropic:
                response = self.client.chat(
                    messages=self.conversation_history,
                    system=self.system_prompt,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )
            else:
                # OpenAI 需要將 system prompt 作為第一條訊息
                messages = [{"role": "system", "content": self.system_prompt}]
                messages.extend(self.conversation_history)
                response = self.client.chat(
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                )

            # 添加助手回應
            self.add_message("assistant", response)

            return response

        except Exception as e:
            logger.error(f"{self.assistant_type} 聊天失敗: {e}")
            raise

    @abstractmethod
    def get_welcome_message(self) -> str:
        """
        獲取歡迎訊息

        Returns:
            歡迎訊息字符串
        """
        pass

    @abstractmethod
    def get_help_message(self) -> str:
        """
        獲取幫助訊息

        Returns:
            幫助訊息字符串
        """
        pass

    def start_conversation(self) -> str:
        """
        開始對話

        Returns:
            初始訊息
        """
        return self.get_welcome_message()

    def export_conversation(self, format: str = "json") -> Any:
        """
        匯出對話記錄

        Args:
            format: 匯出格式 (json/markdown)

        Returns:
            匯出的對話記錄
        """
        if format == "json":
            return {
                "assistant_type": self.assistant_type,
                "history": self.conversation_history,
            }
        elif format == "markdown":
            md_content = f"# {self.assistant_type} 對話記錄\n\n"
            for msg in self.conversation_history:
                role = "用戶" if msg["role"] == "user" else "助手"
                md_content += f"## {role}\n\n{msg['content']}\n\n"
            return md_content
        else:
            raise ValueError(f"不支援的匯出格式: {format}")
