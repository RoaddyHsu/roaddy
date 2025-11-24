"""
Manager 助手使用範例
"""

import sys
from pathlib import Path

# 將 src 目錄加入 Python 路徑
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from assistants import ManagerAssistant


def example_daily_planning():
    """每日工作規劃範例"""
    print("\n" + "=" * 60)
    print("範例 1: 每日工作規劃 (CoT 框架)")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 模擬對話
    user_message = """
    今天是星期一，我需要規劃今天的工作。

    本週重點：
    - 新品上市活動（漢堡新品）
    - 社群互動提升計畫

    進行中專案：
    - 新品上市活動企劃
    - Q1社群行銷策略
    - 團購平台合作案

    今日會議：
    - 10:00-11:00 新品發表會會前會
    - 14:00-15:00 週會（討論上週成效）
    """

    print("用戶:", user_message)
    print("\n啟動每日工作規劃...\n")

    # 使用快速指令
    response = assistant.start_workflow(
        assistant.WORKFLOW_DAILY_PLANNING,
        user_message
    )

    print("助手回應:")
    print(response)


def example_social_content():
    """社群內容產出範例"""
    print("\n" + "=" * 60)
    print("範例 2: 社群內容快速產出 (TAG 框架)")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 模擬對話
    user_message = """
    請幫我產出一篇 Instagram 貼文。

    主題：新品上市 - 黑胡椒牛肉堡
    平台：Instagram
    檔期：本週五上市

    產品特色：
    - 現煎牛肉排
    - 特調黑胡椒醬
    - 加量起司
    - 限時優惠價 $99（原價 $129）
    """

    print("用戶:", user_message)
    print("\n啟動社群內容產出...\n")

    response = assistant.start_workflow(
        assistant.WORKFLOW_SOCIAL_CONTENT,
        user_message
    )

    print("助手回應:")
    print(response)


def example_ad_strategy():
    """廣告投放決策範例"""
    print("\n" + "=" * 60)
    print("範例 3: 廣告投放決策 (CO-STAR 框架)")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 模擬對話
    user_message = """
    請幫我規劃新品上市的廣告投放。

    廣告目的：新品銷售轉換
    活動名稱：黑胡椒牛肉堡上市
    活動期間：本週五至下週日（共10天）
    預算：30,000元
    平台：Facebook + Instagram

    目標：
    - 觸及 10 萬人
    - 至少 500 次轉換（到店購買或線上訂購）
    - ROAS > 3

    目標受眾：
    - 年齡：18-45歲
    - 地區：台北、新北、桃園
    - 興趣：美食、速食、漢堡
    """

    print("用戶:", user_message)
    print("\n啟動廣告投放決策...\n")

    response = assistant.start_workflow(
        assistant.WORKFLOW_AD_STRATEGY,
        user_message
    )

    print("助手回應:")
    print(response)


def example_project_decision():
    """專案決策分析範例"""
    print("\n" + "=" * 60)
    print("範例 4: 專案決策分析 (CoT 框架)")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 模擬對話
    user_message = """
    我需要幫助做一個決策。

    決策議題：是否與 KOL 合作推廣新品？

    背景：
    - 新品即將上市
    - 預算有限（總預算 10 萬）
    - 目標是快速打開知名度

    選項A：與大型 KOL 合作（1位）
    - 費用：8 萬
    - 粉絲數：50 萬
    - 預估觸及：15-20 萬
    - 優點：影響力大、可信度高
    - 缺點：費用高、只有一次曝光
    - 風險：效果難保證

    選項B：與中型 KOL 合作（3-4位）
    - 費用：8-10 萬（每位 2-2.5 萬）
    - 粉絲數：10-15 萬/人
    - 預估觸及：10-15 萬
    - 優點：多次曝光、觸及不同族群
    - 缺點：需要多方溝通協調
    - 風險：品質參差不齊

    選項C：主攻廣告投放，不找 KOL
    - 費用：10 萬全投廣告
    - 預估觸及：20-30 萬
    - 優點：可控性高、可持續優化
    - 缺點：缺乏第三方背書
    - 風險：廣告疲勞
    """

    print("用戶:", user_message)
    print("\n啟動專案決策分析...\n")

    response = assistant.start_workflow(
        assistant.WORKFLOW_PROJECT_DECISION,
        user_message
    )

    print("助手回應:")
    print(response)


def example_content_qa():
    """內容品質把關範例"""
    print("\n" + "=" * 60)
    print("範例 5: 內容品質把關 (RODES 框架)")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 待檢查的內容
    content_to_check = """
    🔥 新品上市！黑胡椒牛肉堡

    弘爺漢堡最新力作！精選台灣牛肉，現煎現做，搭配特調黑胡椒醬，讓你一口就愛上！

    🎉 限時優惠
    原價 $129，現在只要 $99！

    📍 全台門市同步開賣
    🕐 營業時間：10:00-22:00

    快來品嚐！

    #弘爺漢堡 #黑胡椒牛肉堡 #新品上市 #台灣牛肉 #現做現煎
    """

    user_message = f"""
    請檢查以下 Facebook 貼文的品質：

    {content_to_check}

    內容類型：Facebook 社群貼文
    """

    print("用戶:", user_message)
    print("\n啟動內容品質把關...\n")

    response = assistant.start_workflow(
        assistant.WORKFLOW_CONTENT_QA,
        user_message
    )

    print("助手回應:")
    print(response)


def example_list_workflows():
    """列出所有工作流程"""
    print("\n" + "=" * 60)
    print("範例 6: 列出所有工作流程")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 列出工作流程
    workflows = assistant.list_workflows()
    print(workflows)


if __name__ == "__main__":
    print("Manager 助手使用範例")
    print("=" * 60)

    # 取消註解下面的函數來運行範例
    # example_daily_planning()
    # example_social_content()
    # example_ad_strategy()
    # example_project_decision()
    # example_content_qa()
    # example_list_workflows()

    print("\n提示：請先在 .env 文件中設定 ANTHROPIC_API_KEY，然後取消註解範例函數")
