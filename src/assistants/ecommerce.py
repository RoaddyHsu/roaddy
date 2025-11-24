"""
電商行銷助手
"""

from .base_assistant import BaseAssistant
from ..utils.prompts import get_prompt


class EcommerceAssistant(BaseAssistant):
    """電商行銷助手 - 電商策略規劃"""

    def __init__(self):
        super().__init__(
            assistant_type="ecommerce",
            system_prompt=get_prompt("ecommerce"),
            use_anthropic=True,
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用電商行銷助手 🛒

我是您的專業電商行銷顧問，專精於：
- 🏪 全通路銷售策略
- 📱 社群行銷規劃
- 👥 KOL 合作計畫
- 💬 團購與口碑行銷

我將協助您制定全方位的電商行銷解決方案，提升商品銷售量！

請告訴我您的商品資訊，讓我們開始吧！
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 電商行銷助手使用指南

## 我能提供的服務

1. **全通路銷售策略**
   - 銷售平台選擇
   - 跨平台整合
   - 價格策略
   - 物流配送

2. **社群行銷規劃**
   - 平台選擇
   - 內容發布策略
   - 粉絲經營
   - 社群聲量監測

3. **KOL 合作計畫**
   - KOL 篩選標準
   - 合作模式建議
   - 內容企劃
   - 效益評估

4. **團購與口碑行銷**
   - 團購主合作
   - 優惠方案設計
   - 口碑擴散
   - 會員回購機制

## 預算配置建議

- 社群行銷：25%
- KOL 合作：20%
- 團購經營：20%
- 口碑行銷：15%
- 直播銷售：10%
- 其他策略：10%

## 需要的資訊

請提供：
- 商品類別與特色
- 目標售價與銷售目標
- 主要競品分析
- 目標客群
- 行銷預算

輸入 "開始" 開始規劃您的電商行銷策略！
"""
