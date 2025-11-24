"""
文案撰寫助手
"""

from .base_assistant import BaseAssistant
from ..utils.prompts import get_prompt
from ..api import OpenAIClient
from typing import Optional
import os


class CopywritingAssistant(BaseAssistant):
    """文案撰寫助手 - 跨平台文案創作"""

    def __init__(self):
        super().__init__(
            assistant_type="copywriting",
            system_prompt=get_prompt("copywriting"),
            use_anthropic=True,
        )

        # 初始化 DALL-E 客戶端用於圖片生成
        self.enable_image_generation = self.config.get("enable_image_generation", True)
        if self.enable_image_generation:
            try:
                self.dalle_client = OpenAIClient()
            except:
                self.enable_image_generation = False

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用文案撰寫助手 ✍️

我是您的專業文案創作顧問，專精於：
- 📱 跨平台文案創作（Facebook、Instagram、Threads、部落格、LinkedIn）
- 🎨 平台特性優化
- 🖼️ 自動生成配圖（DALL-E 3）
- #️⃣ HashTag 和 Emoji 智能配置

我將根據不同平台特性，為您打造最適合的文案內容！

請告訴我您想要的平台和主題，讓我們開始創作吧！
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 文案撰寫助手使用指南

## 支援平台

1. **Facebook**
   - 長篇內容（500-1000字）
   - Markdown 格式
   - 3-5 組 HashTag
   - 配圖生成

2. **Instagram**
   - 中短篇內容（300-500字）
   - 5-10 組精準 HashTag
   - 豐富 Emoji 點綴
   - 視覺化排版

3. **Threads**
   - 短篇精華（300字以內）
   - 單一核心 HashTag
   - 簡潔有力表達

4. **部落格**
   - 長篇深入內容（1000字以上）
   - SEO 優化格式
   - 完整 Markdown 結構

5. **LinkedIn**
   - 專業內容（400-600字）
   - 專業用語為主
   - 無 Emoji 和 HashTag

## 如何使用？

請提供：
- 目標平台（FB/IG/Threads/部落格/LinkedIn）
- 語氣口吻（專業/輕鬆/正式/活潑）
- 預期字數
- 文案主題或原始內容

範例：「請為我的咖啡店寫一篇 Instagram 文案，輕鬆活潑的風格，主題是新品上市」
"""

    def generate_image(self, prompt: str) -> Optional[str]:
        """
        生成配圖

        Args:
            prompt: 圖片描述

        Returns:
            圖片 URL 或 None
        """
        if not self.enable_image_generation:
            return None

        try:
            image_urls = self.dalle_client.generate_image(
                prompt=prompt, size="1024x1024", quality="standard"
            )
            return image_urls[0] if image_urls else None
        except Exception as e:
            return None
