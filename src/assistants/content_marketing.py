"""
內容行銷助手
"""

from .base_assistant import BaseAssistant
from ..utils.prompts import get_prompt


class ContentMarketingAssistant(BaseAssistant):
    """內容行銷助手 - 專注於 SEO 優化"""

    def __init__(self):
        super().__init__(
            assistant_type="content_marketing",
            system_prompt=get_prompt("content_marketing"),
            use_anthropic=True,
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用內容行銷助手 📊

我是您的專業內容行銷顧問，專精於：
- 🎯 白帽 SEO 技術優化
- 📝 內容策略規劃
- 📈 數據分析與追蹤
- 🔍 關鍵字研究與佈局

我將協助您制定完整的 SEO 優化策略，提升網站在搜尋引擎的排名。

請告訴我您的網站資訊，讓我們開始吧！
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 內容行銷助手使用指南

## 我能幫您做什麼？

1. **技術面 SEO 優化**
   - 網站架構分析
   - 載入速度優化
   - 行動版優化建議
   - Schema 標記建議

2. **內容面優化策略**
   - 關鍵字研究與分析
   - 內容架構規劃
   - 標題優化建議
   - 內外部連結策略

3. **SEO 文案撰寫**
   - TDK 撰寫範本
   - 內文結構建議
   - 關鍵字密度分析

4. **數據追蹤與分析**
   - Google Analytics 設定
   - Search Console 優化
   - KPI 設定建議

## 如何開始？

請提供以下資訊：
- 網站網址
- 網站類型
- 主要目標關鍵字
- 目標受眾
- 競爭對手網站

輸入 "開始" 或直接告訴我您的需求！
"""
