"""
API 使用範例
"""

import sys
from pathlib import Path

# 將 src 目錄加入 Python 路徑
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from api import OpenAIClient, AnthropicClient, GoogleSearchClient


def example_openai():
    """OpenAI API 使用範例"""
    print("\n" + "=" * 50)
    print("範例 1: OpenAI API")
    print("=" * 50 + "\n")

    try:
        # 創建客戶端
        client = OpenAIClient(model="gpt-4o")

        # 發送聊天請求
        messages = [
            {"role": "user", "content": "請用一句話介紹 AI 行銷顧問系統"}
        ]

        response = client.chat(messages)
        print("回應:", response)

    except Exception as e:
        print(f"錯誤: {e}")


def example_anthropic():
    """Anthropic (Claude) API 使用範例"""
    print("\n" + "=" * 50)
    print("範例 2: Anthropic (Claude) API")
    print("=" * 50 + "\n")

    try:
        # 創建客戶端
        client = AnthropicClient(model="claude-3-5-sonnet-20241022")

        # 發送聊天請求
        messages = [
            {"role": "user", "content": "請用一句話介紹內容行銷的重要性"}
        ]

        system = "你是一位專業的行銷顧問"

        response = client.chat(messages, system=system)
        print("回應:", response)

    except Exception as e:
        print(f"錯誤: {e}")


def example_dalle():
    """DALL-E 3 圖片生成範例"""
    print("\n" + "=" * 50)
    print("範例 3: DALL-E 3 圖片生成")
    print("=" * 50 + "\n")

    try:
        # 創建客戶端
        client = OpenAIClient()

        # 生成圖片
        prompt = "A modern marketing dashboard with charts and graphs, professional style"
        image_urls = client.generate_image(prompt)

        print(f"生成的圖片 URL: {image_urls[0]}")

    except Exception as e:
        print(f"錯誤: {e}")


def example_google_search():
    """Google Search API 使用範例"""
    print("\n" + "=" * 50)
    print("範例 4: Google Search API")
    print("=" * 50 + "\n")

    try:
        # 創建客戶端
        client = GoogleSearchClient()

        # 搜尋
        results = client.search("AI marketing trends 2025", num=5)

        print(f"找到 {len(results)} 個結果:\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['title']}")
            print(f"   {result['link']}")
            print(f"   {result['snippet']}\n")

    except Exception as e:
        print(f"錯誤: {e}")


if __name__ == "__main__":
    print("API 使用範例")
    print("=" * 50)

    # 取消註解下面的函數來運行範例
    # example_openai()
    # example_anthropic()
    # example_dalle()
    # example_google_search()

    print("\n提示：請先在 .env 文件中設定相應的 API 金鑰")
