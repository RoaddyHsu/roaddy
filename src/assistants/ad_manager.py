"""
廣告投手
"""

from .base_assistant import BaseAssistant
from ..utils.prompts import get_prompt


class AdManagerAssistant(BaseAssistant):
    """廣告投手 - 廣告投放策略"""

    def __init__(self):
        super().__init__(
            assistant_type="ad_manager",
            system_prompt=get_prompt("ad_manager"),
            use_anthropic=False,  # 使用 GPT-4o
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用廣告投手 🎯

我是您的專業廣告投放顧問，專精於：
- 📊 跨平台廣告策略規劃
- 💰 預算配置與優化
- 🎨 廣告素材規劃
- 📈 數據分析與 ROI 優化

我將協助您制定最佳的廣告投放策略，達成您的行銷目標！

請告訴我您的產品和目標，讓我們開始吧！
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 廣告投手使用指南

## 我能提供的服務

1. **廣告平台配置建議**
   - 平台選擇與預算分配
   - 投放時段建議
   - 競價策略

2. **廣告素材規劃**
   - 廣告形式建議
   - 素材規格建議
   - 文案方向
   - A/B 測試建議

3. **投放策略規劃**
   - 目標受眾設定
   - 再行銷策略
   - 預算控制
   - 投放時程

4. **數據追蹤與優化**
   - 轉換追蹤設定
   - 報表監控重點
   - ROI 計算
   - 優化建議

## 預算配置建議

**B2B 市場：**
- LinkedIn Ads: 40%
- Google Ads: 35%
- 專業媒體: 15%
- 其他平台: 10%

**B2C 市場：**
- Meta Ads: 35%
- Google Ads: 30%
- TikTok Ads: 20%
- 其他平台: 15%

## 需要的資訊

請提供：
- 產品/服務類型
- 目標市場（B2B/B2C）
- 目標受眾
- 月度預算
- 主要 KPI

輸入 "開始" 開始規劃您的廣告投放策略！
"""
