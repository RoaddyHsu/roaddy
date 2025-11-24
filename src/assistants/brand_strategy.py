"""
品牌策略顧問
"""

from .base_assistant import BaseAssistant
from ..utils.prompts import get_prompt


class BrandStrategyAssistant(BaseAssistant):
    """品牌策略顧問 - 品牌定位分析"""

    def __init__(self):
        super().__init__(
            assistant_type="brand_strategy",
            system_prompt=get_prompt("brand_strategy"),
            use_anthropic=True,
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用品牌策略顧問 🎯

我是您的專業品牌策略顧問，專精於：
- 🔍 競爭優勢分析
- 📍 策略定位制定
- 🎨 品牌價值主張設計
- 📈 策略活動系統（SAS）

我將透過一問一答的方式，引導您建立完整的品牌策略！

準備好了嗎？讓我們開始探索您的品牌吧！
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 品牌策略顧問使用指南

## 諮詢流程

### 第一階段：品牌基礎探索
- 品牌核心業務
- 目標客群定義
- 市場挑戰分析

### 第二階段：競爭優勢分析
- 品牌獨特特點
- 客戶痛點解決方案
- 競爭對手分析

### 第三階段：策略定位制定
- 品牌形象期望
- 核心價值主張
- 品牌個性定義

### 第四階段：策略活動規劃
- 行銷渠道盤點
- 發展目標設定
- 資源預算規劃

## 最終交付

【品牌策略規劃建議書】包含：
1. 市場洞察
2. 品牌策略框架
3. 策略活動系統
4. 執行路徑規劃

輸入 "開始" 開始品牌策略諮詢！
"""
