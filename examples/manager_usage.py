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


def example_weekly_meeting():
    """週會準備與記錄範例"""
    print("\n" + "=" * 60)
    print("範例 6: 週會準備與記錄 (SCQA 框架)")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 模擬對話
    user_message = """
    請幫我準備本週的週會內容。

    本週工作回顧（11/18-11/22）：

    已完成項目：
    - 新品上市活動企劃（100%）
    - Facebook 廣告投放設定（100%）
    - 11月社群貼文產出（20篇）

    進行中項目：
    - Q1社群行銷策略（80%，預計下週完成）
    - 團購平台合作案（60%，等待對方回覆）
    - 年度行銷計畫（40%，12月中完成）

    數據表現：
    - 粉絲成長：+1,200（目標 +1,000）✓
    - 貼文平均觸及：8,500（目標 7,000）✓
    - 廣告 ROAS：3.2（目標 3.0）✓
    - 線上訂單：280 單（目標 300 單）✗

    遇到的問題：
    - 團購平台回覆緩慢，影響專案進度
    - 線上訂單略低於目標，需要討論優化策略
    - 人力吃緊，部分非緊急工作延後

    下週重點：
    - 新品上市活動執行（11/29 開始）
    - 完成 Q1 社群策略
    - 年度規劃初稿
    """

    print("用戶:", user_message)
    print("\n啟動週會準備與記錄...\n")

    response = assistant.start_workflow(
        assistant.WORKFLOW_WEEKLY_MEETING,
        user_message
    )

    print("助手回應:")
    print(response)


def example_monthly_review():
    """月度績效評估範例"""
    print("\n" + "=" * 60)
    print("範例 7: 月度績效評估 (RISE 框架)")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 模擬對話
    user_message = """
    請幫我進行 11 月份的績效評估。

    === 關鍵數據 ===

    社群經營：
    - 粉絲成長：+4,800（目標 +4,000）達成率 120%
    - 貼文觸及：平均 8,200（目標 7,000）達成率 117%
    - 互動率：3.8%（目標 3.5%）達成率 109%
    - 最佳貼文：新品預告影片，觸及 25,000，互動 1,200

    廣告投放：
    - 總預算：$50,000 / 實際 $48,500（使用率 97%）
    - 總觸及：320,000 / CPM $151
    - 總點擊：12,800 / CPC $3.8 / CTR 4%
    - 總轉換：640 / CPA $76 / CVR 5%
    - ROAS：3.2（目標 3.0）

    業績/轉換：
    - 線上訂單：1,150 單（目標 1,200 單）達成率 96%
    - 到店轉換：估計 2,300 人（來自社群 40%，廣告 35%，其他 25%）
    - 營業額貢獻：$850,000（較上月 +12%）

    專案執行：
    - 完成專案：3 個（新品上市、雙11 活動、KOL 合作）
    - 進行中專案：2 個（Q1 策略 85%、團購合作 70%）
    - 延遲專案：1 個（年度規劃，因需求調整）

    === 觀察到的情況 ===

    亮點：
    - 影片內容表現突出，互動率比圖文高 40%
    - 廣告 ROAS 連續三個月超標
    - 社群粉絲成長加速

    問題：
    - 線上訂單略低於目標
    - 團購合作進度緩慢
    - 人力不足，同時處理多專案壓力大

    趨勢：
    - 用戶偏好短影片內容
    - 晚上 8-10 點互動最高
    - Instagram 成長快於 Facebook
    """

    print("用戶:", user_message)
    print("\n啟動月度績效評估...\n")

    response = assistant.start_workflow(
        assistant.WORKFLOW_MONTHLY_REVIEW,
        user_message
    )

    print("助手回應:")
    print(response)


def example_annual_planning():
    """年度規劃範例"""
    print("\n" + "=" * 60)
    print("範例 8: 年度規劃 (ERA 框架)")
    print("=" * 60 + "\n")

    # 創建助手實例
    assistant = ManagerAssistant()

    # 模擬對話
    user_message = """
    請幫我規劃 2026 年度的行銷計畫。

    === 2025 年度回顧 ===

    整體績效：
    - 年度預算：$600,000 / 實際使用：$585,000（執行率 97.5%）
    - 社群成長：期初 28,000 → 期末 78,000（成長 178%）✓
    - 品牌曝光：年度觸及 580 萬（目標 500 萬）✓
    - 業績貢獻：$9,800,000（目標 $9,000,000）✓
    - 平均 ROAS：3.1（目標 3.0）✓

    重大專案：
    1. 品牌重塑計畫（Q1-Q2）- 成功提升品牌形象
    2. KOL 行銷專案（全年）- 合作 15 位 KOL，效果良好
    3. 電商平台拓展（Q2-Q3）- 成功進駐 3 個平台
    4. 會員經營系統（Q3-Q4）- 累積 12,000 會員
    5. 年度大型活動（Q4）- 創造 $1,200,000 營收

    主要成果：
    - 社群粉絲大幅成長
    - 品牌知名度提升
    - 成功開拓線上通路
    - 建立會員基礎

    遇到的挑戰：
    - 競爭加劇
    - 廣告成本上升
    - 人力資源不足
    - 市場需求變化快

    === 2026 年環境分析 ===

    市場趨勢：
    - 短影音持續主流
    - AI 行銷工具普及
    - 消費者更重視品牌價值
    - 線上線下整合需求增加

    競品動態：
    - 主要競品加大數位投資
    - 新興品牌採用創新行銷

    我們的優勢：
    - 強大的社群基礎
    - 良好的品牌形象
    - 高效的團隊執行力

    我們的劣勢：
    - 預算有限
    - 人力不足
    - 數位工具使用有限

    === 2026 年期望 ===

    公司給的目標：
    - 營業額成長 25%
    - 會員數達 25,000
    - 品牌知名度再提升
    - 持續優化 ROAS

    可用預算：$750,000（較去年 +25%）
    """

    print("用戶:", user_message)
    print("\n啟動年度規劃...\n")

    response = assistant.start_workflow(
        assistant.WORKFLOW_ANNUAL_PLANNING,
        user_message
    )

    print("助手回應:")
    print(response)


def example_list_workflows():
    """列出所有工作流程"""
    print("\n" + "=" * 60)
    print("範例 9: 列出所有工作流程")
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

    # === 日常工作流程範例 ===
    # example_daily_planning()
    # example_social_content()
    # example_ad_strategy()
    # example_project_decision()
    # example_content_qa()

    # === 綜合管理工作流程範例 ===
    # example_weekly_meeting()
    # example_monthly_review()
    # example_annual_planning()

    # === 查看所有工作流程 ===
    # example_list_workflows()

    print("\n提示：請先在 .env 文件中設定 ANTHROPIC_API_KEY，然後取消註解範例函數")
