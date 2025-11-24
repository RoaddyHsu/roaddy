"""
Manager 專用 AI Agent
"""

from .base_assistant import BaseAssistant
from typing import Dict, Optional


class ManagerAssistant(BaseAssistant):
    """Manager 專用助手 - 策略規劃與決策支援"""

    # 工作流程類型
    WORKFLOW_DAILY_PLANNING = "daily_planning"
    WORKFLOW_SOCIAL_CONTENT = "social_content"
    WORKFLOW_AD_STRATEGY = "ad_strategy"
    WORKFLOW_PROJECT_DECISION = "project_decision"
    WORKFLOW_CONTENT_QA = "content_qa"

    def __init__(self):
        # 主系統提示詞
        system_prompt = """你是弘爺漢堡行銷部主管 Roaddy 的專屬 AI 策略顧問。

## 核心職責
- 策略規劃與決策支援
- 跨職能專案統籌
- 團隊管理與培訓
- 成效分析與優化建議

## 工作特性
- 需同時處理策略層與執行層
- 目前兼任 A(行銷企劃)、B(數位行銷)、E(團購PM) 職務
- 重視效率與產出品質
- 強調數據驅動決策

## 品牌調性參考
- 弘爺漢堡: 現做現煎、台式口味、平價美味
- 避免: 過度正式、老派用語
- 偏好: 親切、有梗、貼近生活

## 工作流程
你支援以下工作流程：
1. 每日工作規劃 (CoT 框架)
2. 社群內容快速產出 (TAG 框架)
3. 廣告投放決策 (CO-STAR 框架)
4. 專案決策分析 (CoT 框架)
5. 內容品質把關 (RODES 框架)

根據用戶的需求，選擇適當的框架提供專業建議。"""

        super().__init__(
            assistant_type="manager",
            system_prompt=system_prompt,
            use_anthropic=True,
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用 Manager 專用 AI Agent 👔

我是弘爺漢堡行銷部主管 Roaddy 的專屬 AI 策略顧問！

## 🎯 我能協助您

### 1️⃣ 每日工作規劃 (CoT 框架)
幫您規劃當日工作優先級和時間分配

### 2️⃣ 社群內容快速產出 (TAG 框架)
快速產出社群貼文，提供 3 個版本供選擇

### 3️⃣ 廣告投放決策 (CO-STAR 框架)
完整的廣告策劃，包含受眾設定、素材建議、成效預估

### 4️⃣ 專案決策分析 (CoT 框架)
協助您進行專案決策，提供結構化分析

### 5️⃣ 內容品質把關 (RODES 框架)
檢查內容品質，給出評分和改善建議

## 💡 使用方式

### 快速啟動
- 輸入 `/workflows` 查看所有工作流程
- 輸入 `/daily` 開始每日規劃
- 輸入 `/social` 產出社群內容
- 輸入 `/ad` 規劃廣告投放
- 輸入 `/decide` 進行決策分析
- 輸入 `/qa` 檢查內容品質

或直接描述您的需求，我會自動選擇最適合的框架！

準備好開始了嗎？
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# Manager 助手使用指南

## 📋 支援的工作流程

### 1. 每日工作規劃 (CoT)
**使用時機：** 每天早上開始工作前
**輸入指令：** `/daily`
**需要資訊：**
- 今天是星期幾
- 本週重點
- 進行中專案
- 今日會議安排

**輸出內容：**
- 優先級分析
- 時間分配建議
- 任務分類（必須/重要/可彈性）
- 風險識別
- 具體執行順序

---

### 2. 社群內容快速產出 (TAG)
**使用時機：** 需要快速產出社群貼文時
**輸入指令：** `/social`
**需要資訊：**
- 發布平台（FB/IG/Threads）
- 主題（新品/優惠/品牌故事/互動）
- 檔期資訊

**輸出內容：**
- 3 個文案版本
- 視覺建議
- 發文時間建議
- Hashtag 和 Emoji 配置

---

### 3. 廣告投放決策 (CO-STAR)
**使用時機：** 規劃新的廣告活動時
**輸入指令：** `/ad`
**需要資訊：**
- 廣告目的
- 活動資訊
- 預算
- 目標受眾

**輸出內容：**
- 廣告策略建議
- 3 組素材組合
- 受眾設定建議
- 成效預估
- 優化建議

---

### 4. 專案決策分析 (CoT)
**使用時機：** 面臨重要專案決策時
**輸入指令：** `/decide`
**需要資訊：**
- 決策議題
- 背景資訊
- 各種選項及其優缺點

**輸出內容：**
- 完整的決策分析
- 情境模擬
- 比較表格
- 推薦方案和理由
- 風險應對
- 決策檢查清單

---

### 5. 內容品質把關 (RODES)
**使用時機：** 發布內容前的最後檢查
**輸入指令：** `/qa`
**需要資訊：**
- 待檢查的內容
- 內容類型

**輸出內容：**
- 五個維度評分
  - R (Role) 角色適切性
  - O (Objective) 目標明確性
  - D (Details) 細節完整性
  - E (Engagement) 互動吸引力
  - S (Structure) 結構邏輯性
- 總分和評級
- 優先改善項目
- 修改後版本

---

## 🎯 使用技巧

### 快速指令
- `/workflows` - 查看所有工作流程
- `/daily` - 每日工作規劃
- `/social` - 社群內容產出
- `/ad` - 廣告投放決策
- `/decide` - 專案決策分析
- `/qa` - 內容品質把關

### 自然對話
您也可以直接描述需求，例如：
- "幫我規劃今天的工作"
- "我需要一篇 IG 貼文"
- "幫我分析這個專案該怎麼做"
- "檢查這篇文案的品質"

## 💡 最佳實踐

1. **提供完整背景** - 越詳細的資訊，建議越精準
2. **使用快速指令** - 更快進入工作流程
3. **多輪對話** - 可以進一步討論和優化建議
4. **匯出記錄** - 重要決策建議可用 `/export` 匯出

需要開始使用嗎？輸入 `/workflows` 查看所有工作流程！
"""

    def get_workflow_prompt(self, workflow_type: str, context: Dict = None) -> str:
        """
        獲取特定工作流程的提示詞

        Args:
            workflow_type: 工作流程類型
            context: 上下文資訊

        Returns:
            工作流程提示詞
        """
        workflows = {
            self.WORKFLOW_DAILY_PLANNING: self._get_daily_planning_prompt,
            self.WORKFLOW_SOCIAL_CONTENT: self._get_social_content_prompt,
            self.WORKFLOW_AD_STRATEGY: self._get_ad_strategy_prompt,
            self.WORKFLOW_PROJECT_DECISION: self._get_project_decision_prompt,
            self.WORKFLOW_CONTENT_QA: self._get_content_qa_prompt,
        }

        prompt_func = workflows.get(workflow_type)
        if prompt_func:
            return prompt_func(context or {})
        return ""

    def _get_daily_planning_prompt(self, context: Dict) -> str:
        """每日工作規劃提示詞"""
        return """請用 CoT (Chain of Thought) 框架幫我規劃今日工作。

請按照以下步驟思考：

**Step 1: 優先級判斷**
分析今日所有待辦事項的緊急度與重要度

**Step 2: 時間分配**
根據工作時間(09:00-18:00)與會議安排，規劃時間區塊

**Step 3: 任務分類**
- 🔴 必須今日完成
- 🟡 重要但可彈性
- 🟢 可委派或延後

**Step 4: 風險識別**
指出可能的時間衝突或資源瓶頸

**Step 5: 行動建議**
給出具體的執行順序與時間安排

請以時間軸方式呈現，包含：
- 時段
- 任務
- 預估時間
- 優先級
- 注意事項
"""

    def _get_social_content_prompt(self, context: Dict) -> str:
        """社群內容產出提示詞"""
        return """使用 TAG (Task-Action-Goal) 框架產出社群貼文。

請產出：

## 1. 文案（3個版本供選擇）
- 風格：年輕活潑、創意吸睛
- 必含元素：Hashtag、Emoji、CTA

## 2. 視覺建議
- 主視覺方向
- 色調建議
- 構圖建議

## 3. 發文時機
- 最佳發文時間
- 理由說明

## 品牌調性參考
- 弘爺漢堡：現做現煎、台式口味、平價美味
- 避免：過度正式、老派用語
- 偏好：親切、有梗、貼近生活

## 輸出格式

### 版本1: [風格描述]
【文案】
【Hashtag】
【Emoji 使用】
【視覺建議】
【發文時間】

### 版本2: [風格描述]
[同上]

### 版本3: [風格描述]
[同上]

### 推薦使用: 版本X
【推薦理由】
"""

    def _get_ad_strategy_prompt(self, context: Dict) -> str:
        """廣告投放決策提示詞"""
        return """使用 CO-STAR 框架規劃廣告投放。

請提供：

## 1. 廣告策略建議
- 投放策略
- 預算分配
- 時程規劃

## 2. 素材建議（3組）

**組合A:**
- 主視覺：[描述]
- 主標題：[文案]
- 內文：[文案]
- CTA：[文案]
- 適用：[情境]

**組合B:** [同上]
**組合C:** [同上]

## 3. 受眾設定
- 受眾組合建議
- A/B 測試規劃
- 再行銷策略

## 4. 成效預估
- 預估觸及：[數字]
- 預估點擊：[數字]
- 預估CPC：[金額]
- 預估轉換：[數字]
- 預估ROAS：[倍數]

## 5. 優化建議
- 前3天觀察重點
- 優化調整方向
- 備用方案
"""

    def _get_project_decision_prompt(self, context: Dict) -> str:
        """專案決策分析提示詞"""
        return """請用 CoT (Chain of Thought) 框架協助專案決策。

請按照以下步驟分析：

**Step 1: 目標釐清**
- 這個決策要達成什麼核心目標？
- 成功的定義是什麼？

**Step 2: 選項評估**
逐一分析每個選項：
- 對目標的貢獻度
- 可行性分析
- 風險評估
- 資源需求

**Step 3: 情境模擬**
- 最佳情境：如果一切順利會如何？
- 最差情境：如果遇到問題會如何？
- 最可能情境：實際上會如何？

**Step 4: 比較分析**
用表格比較各選項的：
- 目標達成度
- 成本效益
- 執行難度
- 風險程度
- 時間需求

**Step 5: 建議結論**
- 推薦方案：[選項X]
- 推薦理由：[3-5點]
- 執行建議：[具體步驟]
- 風險應對：[預防措施]
- 備案：[如果推薦方案不可行]

**Step 6: 決策檢查清單**
在執行前需要確認的事項

請以結構化方式呈現完整分析過程與建議。
"""

    def _get_content_qa_prompt(self, context: Dict) -> str:
        """內容品質把關提示詞"""
        return """使用 RODES 框架檢查內容品質。

請按照 RODES 框架逐項檢查：

## R (Role) - 角色適切性
✅ 檢查項目：
- [ ] 是否符合品牌定位（台式漢堡、現做現煎、平價美味）？
- [ ] 語氣是否符合弘爺風格（年輕活潑、創意吸睛）？
- [ ] 是否避免過度正式或老派用語？

📝 評分：[1-5分]
💡 改善建議：

## O (Objective) - 目標明確性
✅ 檢查項目：
- [ ] 傳達目標是否清楚？
- [ ] CTA（行動呼籲）是否明確？
- [ ] 是否能引導受眾採取行動？
- [ ] 目標受眾是否精準？

📝 評分：[1-5分]
💡 改善建議：

## D (Details) - 細節完整性
✅ 檢查項目：
- [ ] 資訊是否完整（時間/地點/價格/方式）？
- [ ] 是否有錯字或語病？
- [ ] 數據是否正確？
- [ ] 連結是否有效？
- [ ] Hashtag 是否適當？
- [ ] 法規遵循（價格標示/食品標示等）？

📝 評分：[1-5分]
💡 改善建議：

## E (Engagement) - 互動吸引力
✅ 檢查項目：
- [ ] 開頭是否吸睛？
- [ ] 是否能引發情感共鳴？
- [ ] 是否有互動誘因（提問/抽獎/分享）？
- [ ] 視覺元素建議是否吸引人？
- [ ] 是否容易被分享？

📝 評分：[1-5分]
💡 改善建議：

## S (Structure) - 結構邏輯性
✅ 檢查項目：
- [ ] 架構是否清晰？
- [ ] 段落是否易讀？
- [ ] 重點是否突出？
- [ ] 邏輯是否順暢？
- [ ] 長度是否適當？

📝 評分：[1-5分]
💡 改善建議：

---

## 總體評估

### 總分：[X/25分]

### 評級：
- 23-25分：⭐⭐⭐⭐⭐ 優秀，可直接使用
- 20-22分：⭐⭐⭐⭐ 良好，微調後使用
- 17-19分：⭐⭐⭐ 尚可，需要修改
- 14-16分：⭐⭐ 不佳，需大幅修改
- 13分以下：⭐ 不合格，需重寫

### 優先改善項目（依重要性排序）
1. [項目]
2. [項目]
3. [項目]

### 修改後版本
[提供改善後的完整內容]

### 修改說明
[說明修改了哪些地方及理由]
"""

    def start_workflow(self, workflow_type: str, user_input: str = "") -> str:
        """
        啟動特定工作流程

        Args:
            workflow_type: 工作流程類型
            user_input: 用戶輸入

        Returns:
            助手回應
        """
        # 獲取工作流程提示詞
        workflow_prompt = self.get_workflow_prompt(workflow_type)

        if not workflow_prompt:
            return "抱歉，不支援此工作流程。請輸入 /workflows 查看所有可用的工作流程。"

        # 組合完整訊息
        full_message = f"{workflow_prompt}\n\n{user_input}" if user_input else workflow_prompt

        # 發送訊息
        return self.chat(full_message)

    def list_workflows(self) -> str:
        """列出所有工作流程"""
        return """
## 📋 所有工作流程

### 1️⃣ 每日工作規劃 (CoT 框架)
**指令：** `/daily`
**說明：** 規劃當日工作優先級和時間分配

### 2️⃣ 社群內容快速產出 (TAG 框架)
**指令：** `/social`
**說明：** 快速產出社群貼文，提供 3 個版本

### 3️⃣ 廣告投放決策 (CO-STAR 框架)
**指令：** `/ad`
**說明：** 完整廣告策劃，含受眾設定和成效預估

### 4️⃣ 專案決策分析 (CoT 框架)
**指令：** `/decide`
**說明：** 結構化專案決策分析

### 5️⃣ 內容品質把關 (RODES 框架)
**指令：** `/qa`
**說明：** 檢查內容品質，給出評分和改善建議

---

輸入對應指令開始使用，或直接描述您的需求！
"""
