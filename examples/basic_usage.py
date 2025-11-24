"""
基本使用範例
"""

import sys
from pathlib import Path

# 將 src 目錄加入 Python 路徑
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from assistants import ContentMarketingAssistant, CopywritingAssistant


def example_content_marketing():
    """內容行銷助手使用範例"""
    print("\n" + "=" * 50)
    print("範例 1: 內容行銷助手")
    print("=" * 50 + "\n")

    # 創建助手實例
    assistant = ContentMarketingAssistant()

    # 顯示歡迎訊息
    print(assistant.get_welcome_message())

    # 模擬對話
    user_message = """
    我有一個電商網站，主要銷售有機保養品。
    網站：https://example.com
    目標關鍵字：有機保養品、天然護膚
    目標受眾：25-45歲女性
    主要競爭對手：其他有機保養品品牌
    """

    print("\n用戶:", user_message)
    print("\n助手回應:")

    # 獲取回應
    response = assistant.chat(user_message)
    print(response)


def example_copywriting():
    """文案撰寫助手使用範例"""
    print("\n" + "=" * 50)
    print("範例 2: 文案撰寫助手")
    print("=" * 50 + "\n")

    # 創建助手實例
    assistant = CopywritingAssistant()

    # 顯示歡迎訊息
    print(assistant.get_welcome_message())

    # 模擬對話
    user_message = """
    請為我的咖啡店寫一篇 Instagram 文案。
    主題：新品上市 - 焦糖瑪奇朵
    風格：輕鬆活潑
    字數：300-400字
    """

    print("\n用戶:", user_message)
    print("\n助手回應:")

    # 獲取回應
    response = assistant.chat(user_message)
    print(response)


def example_conversation_export():
    """對話匯出範例"""
    print("\n" + "=" * 50)
    print("範例 3: 對話匯出")
    print("=" * 50 + "\n")

    # 創建助手實例
    assistant = ContentMarketingAssistant()

    # 模擬對話
    assistant.chat("我想優化我的網站 SEO")
    assistant.chat("我的網站是電商平台")

    # 匯出為 JSON
    json_data = assistant.export_conversation("json")
    print("JSON 格式:")
    print(json_data)

    print("\n" + "-" * 50 + "\n")

    # 匯出為 Markdown
    md_content = assistant.export_conversation("markdown")
    print("Markdown 格式:")
    print(md_content)


if __name__ == "__main__":
    # 注意：這些範例需要設定 API 金鑰才能運行

    print("AI 行銷顧問系統 - 使用範例")
    print("=" * 50)

    # 取消註解下面的函數來運行範例
    # example_content_marketing()
    # example_copywriting()
    # example_conversation_export()

    print("\n提示：請先在 .env 文件中設定 API 金鑰，然後取消註解範例函數")
