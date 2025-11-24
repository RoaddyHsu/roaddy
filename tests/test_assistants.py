"""
助手模組測試
"""

import sys
from pathlib import Path

# 將 src 目錄加入 Python 路徑
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

import pytest
from assistants import (
    ContentMarketingAssistant,
    CopywritingAssistant,
    SocialMediaAssistant,
    BrandStrategyAssistant,
    CreativeMarketingAssistant,
    EcommerceAssistant,
    AdManagerAssistant,
)


class TestAssistants:
    """助手測試類別"""

    def test_content_marketing_init(self):
        """測試內容行銷助手初始化"""
        assistant = ContentMarketingAssistant()
        assert assistant.assistant_type == "content_marketing"
        assert assistant.system_prompt != ""
        assert len(assistant.conversation_history) == 0

    def test_copywriting_init(self):
        """測試文案撰寫助手初始化"""
        assistant = CopywritingAssistant()
        assert assistant.assistant_type == "copywriting"
        assert assistant.system_prompt != ""

    def test_social_media_init(self):
        """測試社群行銷助手初始化"""
        assistant = SocialMediaAssistant()
        assert assistant.assistant_type == "social_media"

    def test_brand_strategy_init(self):
        """測試品牌策略顧問初始化"""
        assistant = BrandStrategyAssistant()
        assert assistant.assistant_type == "brand_strategy"

    def test_creative_marketing_init(self):
        """測試創意行銷助手初始化"""
        assistant = CreativeMarketingAssistant()
        assert assistant.assistant_type == "creative_marketing"

    def test_ecommerce_init(self):
        """測試電商行銷助手初始化"""
        assistant = EcommerceAssistant()
        assert assistant.assistant_type == "ecommerce"

    def test_ad_manager_init(self):
        """測試廣告投手初始化"""
        assistant = AdManagerAssistant()
        assert assistant.assistant_type == "ad_manager"

    def test_add_message(self):
        """測試添加訊息"""
        assistant = ContentMarketingAssistant()
        assistant.add_message("user", "測試訊息")

        assert len(assistant.conversation_history) == 1
        assert assistant.conversation_history[0]["role"] == "user"
        assert assistant.conversation_history[0]["content"] == "測試訊息"

    def test_clear_history(self):
        """測試清空歷史"""
        assistant = ContentMarketingAssistant()
        assistant.add_message("user", "測試訊息")
        assistant.clear_history()

        assert len(assistant.conversation_history) == 0

    def test_get_history(self):
        """測試獲取歷史"""
        assistant = ContentMarketingAssistant()
        assistant.add_message("user", "訊息1")
        assistant.add_message("assistant", "回應1")

        history = assistant.get_history()
        assert len(history) == 2
        assert history[0]["role"] == "user"
        assert history[1]["role"] == "assistant"

    def test_export_json(self):
        """測試 JSON 匯出"""
        assistant = ContentMarketingAssistant()
        assistant.add_message("user", "測試")
        assistant.add_message("assistant", "回應")

        data = assistant.export_conversation("json")
        assert "assistant_type" in data
        assert "history" in data
        assert len(data["history"]) == 2

    def test_export_markdown(self):
        """測試 Markdown 匯出"""
        assistant = ContentMarketingAssistant()
        assistant.add_message("user", "測試")
        assistant.add_message("assistant", "回應")

        md = assistant.export_conversation("markdown")
        assert "# content_marketing" in md
        assert "## 用戶" in md
        assert "## 助手" in md

    def test_welcome_message(self):
        """測試歡迎訊息"""
        assistant = ContentMarketingAssistant()
        welcome = assistant.get_welcome_message()
        assert welcome != ""
        assert isinstance(welcome, str)

    def test_help_message(self):
        """測試幫助訊息"""
        assistant = ContentMarketingAssistant()
        help_msg = assistant.get_help_message()
        assert help_msg != ""
        assert isinstance(help_msg, str)


if __name__ == "__main__":
    # 運行測試
    pytest.main([__file__, "-v"])
