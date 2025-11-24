"""
Anthropic (Claude) API 客戶端
"""

import os
from typing import List, Dict, Optional
from anthropic import Anthropic
from ..utils.logger import logger


class AnthropicClient:
    """Anthropic Claude API 客戶端"""

    def __init__(
        self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20241022"
    ):
        """
        初始化 Anthropic 客戶端

        Args:
            api_key: Anthropic API 金鑰
            model: 使用的模型
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("請設定 ANTHROPIC_API_KEY 環境變數")

        self.client = Anthropic(api_key=self.api_key)
        self.model = model
        logger.info(f"Anthropic 客戶端初始化完成，使用模型: {self.model}")

    def chat(
        self,
        messages: List[Dict[str, str]],
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> str:
        """
        發送聊天請求

        Args:
            messages: 對話訊息列表
            system: 系統提示詞
            temperature: 溫度參數
            max_tokens: 最大 token 數

        Returns:
            回應內容
        """
        try:
            # 準備請求參數
            kwargs = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }

            if system:
                kwargs["system"] = system

            response = self.client.messages.create(**kwargs)

            content = response.content[0].text
            logger.info(f"Anthropic 回應成功，使用 tokens: {response.usage.input_tokens + response.usage.output_tokens}")
            return content

        except Exception as e:
            logger.error(f"Anthropic API 請求失敗: {e}")
            raise
