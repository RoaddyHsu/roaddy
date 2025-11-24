"""
創意行銷助手
"""

from .base_assistant import BaseAssistant
from ..utils.prompts import get_prompt


class CreativeMarketingAssistant(BaseAssistant):
    """創意行銷助手 - 創意發想系統"""

    def __init__(self):
        super().__init__(
            assistant_type="creative_marketing",
            system_prompt=get_prompt("creative_marketing"),
            use_anthropic=True,
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用創意行銷助手 💡

我是您的創意行銷策略顧問，專精於：
- 🎨 創新行銷點子發想
- 🚀 執行方案規劃
- 🔄 即時互動討論
- 📊 數據支持決策

我將為您提供 3-5 個創意點子，並協助您選擇最適合的方案！

準備好激發創意了嗎？讓我們開始吧！
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 創意行銷助手使用指南

## 服務流程

### 第一階段：需求探索
我會詢問：
- 行銷目標
- 目標受眾特徵
- 預期成效
- 預算限制

### 第二階段：創意發想
針對三個面向提供創意：

1. **內容創意**
   - 故事架構
   - 視覺元素
   - 互動方式

2. **管道創意**
   - 傳播平台
   - 跨平台整合
   - 創新觸點

3. **執行創意**
   - 時程規劃
   - 資源配置
   - 工具運用

### 討論階段
- 評估創意可行性
- 調整優化方案
- 解決執行挑戰

## 最終交付

【創意行銷企劃書】包含：
1. 專案概述
2. 創意策略
3. 執行方案
4. 資源配置
5. 效益評估

輸入 "開始" 開始創意發想！
"""
