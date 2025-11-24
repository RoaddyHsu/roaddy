"""
社群行銷助手
"""

from .base_assistant import BaseAssistant
from ..utils.prompts import get_prompt


class SocialMediaAssistant(BaseAssistant):
    """社群行銷助手 - 社群策略規劃"""

    def __init__(self):
        super().__init__(
            assistant_type="social_media",
            system_prompt=get_prompt("social_media"),
            use_anthropic=False,  # 使用 GPT-4o
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用社群行銷助手 🚀

我是您的專業社群行銷顧問，專精於：
- 📱 跨平台內容策劃
- 👥 社群經營與互動
- 📊 數據分析與優化
- 💡 品牌行銷策略

我將協助您制定完整的社群行銷策略，提升品牌影響力！

請告訴我您的品牌資訊，讓我們開始規劃吧！
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 社群行銷助手使用指南

## 我能提供的服務

1. **社群平台配置建議**
   - 主力平台選擇
   - 各平台內容定位
   - 發文頻率建議

2. **內容策略規劃**
   - 內容主題規劃
   - 內容形式建議
   - 互動策略設計

3. **營運時程表**
   - 每週發文安排
   - 每月重點活動
   - 季度行銷規劃

4. **廣告投放策略**
   - 預算分配建議
   - 目標受眾設定
   - ROI 預估

## 需要的資訊

請提供：
- 品牌名稱與產業
- 目標受眾族群
- 品牌調性
- 行銷目標
- 預算規劃

輸入 "開始" 開始規劃您的社群行銷策略！
"""
