"""
OpenAI API 客戶端
"""

import os
from typing import List, Dict, Optional
from openai import OpenAI
from ..utils.logger import logger


class OpenAIClient:
    """OpenAI API 客戶端"""

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o"):
        """
        初始化 OpenAI 客戶端

        Args:
            api_key: OpenAI API 金鑰
            model: 使用的模型
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("請設定 OPENAI_API_KEY 環境變數")

        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        logger.info(f"OpenAI 客戶端初始化完成，使用模型: {self.model}")

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> str:
        """
        發送聊天請求

        Args:
            messages: 對話訊息列表
            temperature: 溫度參數
            max_tokens: 最大 token 數

        Returns:
            回應內容
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )

            content = response.choices[0].message.content
            logger.info(f"OpenAI 回應成功，使用 tokens: {response.usage.total_tokens}")
            return content

        except Exception as e:
            logger.error(f"OpenAI API 請求失敗: {e}")
            raise

    def generate_image(
        self,
        prompt: str,
        size: str = "1024x1024",
        quality: str = "standard",
        n: int = 1,
    ) -> List[str]:
        """
        使用 DALL-E 3 生成圖片

        Args:
            prompt: 圖片描述
            size: 圖片尺寸（1024x1024, 1024x1792, 1792x1024）
            quality: 圖片品質（standard, hd）
            n: 生成圖片數量

        Returns:
            圖片 URL 列表
        """
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size=size,
                quality=quality,
                n=n,
            )

            image_urls = [img.url for img in response.data]
            logger.info(f"DALL-E 3 成功生成 {len(image_urls)} 張圖片")
            return image_urls

        except Exception as e:
            logger.error(f"DALL-E 3 生成圖片失敗: {e}")
            raise
