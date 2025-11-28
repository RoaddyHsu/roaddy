"""
助手模組測試
"""

import sys
from pathlib import Path

# 將專案根目錄加入 Python 路徑
root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))

import pytest
from src.assistants import (
    ManagerAssistant,
    PersonnelAAssistant,
    PersonnelBAssistant,
    PersonnelCAssistant,
    PersonnelDAssistant,
    PersonnelEAssistant,
)


class TestAssistants:
    """助手測試類別"""

    def test_manager_init(self):
        """測試 Manager 助手初始化"""
        assistant = ManagerAssistant()
        assert assistant.assistant_type == "manager"
        assert assistant.system_prompt != ""
        assert len(assistant.conversation_history) == 0

    def test_personnel_a_init(self):
        """測試人員 A 助手初始化"""
        assistant = PersonnelAAssistant()
        assert assistant.assistant_type == "personnel_a"
        assert assistant.system_prompt != ""

    def test_personnel_b_init(self):
        """測試人員 B 助手初始化"""
        assistant = PersonnelBAssistant()
        assert assistant.assistant_type == "personnel_b"

    def test_personnel_c_init(self):
        """測試人員 C 助手初始化"""
        assistant = PersonnelCAssistant()
        assert assistant.assistant_type == "personnel_c"

    def test_personnel_d_init(self):
        """測試人員 D 助手初始化"""
        assistant = PersonnelDAssistant()
        assert assistant.assistant_type == "personnel_d"

    def test_personnel_e_init(self):
        """測試人員 E 助手初始化"""
        assistant = PersonnelEAssistant()
        assert assistant.assistant_type == "personnel_e"

    def test_add_message(self):
        """測試添加訊息"""
        assistant = ManagerAssistant()
        assistant.add_message("user", "測試訊息")

        assert len(assistant.conversation_history) == 1
        assert assistant.conversation_history[0]["role"] == "user"
        assert assistant.conversation_history[0]["content"] == "測試訊息"

    def test_clear_history(self):
        """測試清空歷史"""
        assistant = ManagerAssistant()
        assistant.add_message("user", "測試訊息")
        assistant.clear_history()

        assert len(assistant.conversation_history) == 0

    def test_get_history(self):
        """測試獲取歷史"""
        assistant = ManagerAssistant()
        assistant.add_message("user", "訊息1")
        assistant.add_message("assistant", "回應1")

        history = assistant.get_history()
        assert len(history) == 2
        assert history[0]["role"] == "user"
        assert history[1]["role"] == "assistant"

    def test_export_json(self):
        """測試 JSON 匯出"""
        assistant = ManagerAssistant()
        assistant.add_message("user", "測試")
        assistant.add_message("assistant", "回應")

        data = assistant.export_conversation("json")
        assert "assistant_type" in data
        assert "history" in data
        assert len(data["history"]) == 2

    def test_export_markdown(self):
        """測試 Markdown 匯出"""
        assistant = ManagerAssistant()
        assistant.add_message("user", "測試")
        assistant.add_message("assistant", "回應")

        md = assistant.export_conversation("markdown")
        assert "# manager" in md
        assert "## 用戶" in md
        assert "## 助手" in md

    def test_welcome_message(self):
        """測試歡迎訊息"""
        assistant = ManagerAssistant()
        welcome = assistant.get_welcome_message()
        assert welcome != ""
        assert isinstance(welcome, str)

    def test_help_message(self):
        """測試幫助訊息"""
        assistant = ManagerAssistant()
        help_msg = assistant.get_help_message()
        assert help_msg != ""
        assert isinstance(help_msg, str)


if __name__ == "__main__":
    # 運行測試
    pytest.main([__file__, "-v"])
