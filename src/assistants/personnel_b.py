"""
人員 B (數位行銷) AI Agent
"""

from .base_assistant import BaseAssistant
from typing import Dict, Optional


class PersonnelBAssistant(BaseAssistant):
    """人員 B (數位行銷) 專用助手 - 社群經營與廣告投放"""

    # 工作流程類型
    WORKFLOW_SOCIAL_CONTENT = "social_content"  # 社群內容創作
    WORKFLOW_AD_CAMPAIGN = "ad_campaign"  # 廣告投放策略
    WORKFLOW_COMMUNITY_MANAGEMENT = "community_management"  # 社群經營
    WORKFLOW_INFLUENCER_COLLAB = "influencer_collab"  # 網紅合作
    WORKFLOW_DATA_ANALYSIS = "data_analysis"  # 數據分析
    WORKFLOW_CRISIS_MANAGEMENT = "crisis_management"  # 危機處理

    def __init__(self):
        # 主系統提示詞
        system_prompt = """你是弘爺漢堡數位行銷專員 (人員 B) 的專屬 AI 助手。

## 核心職責
- 社群內容創作與發布
- 廣告投放策略與優化
- 社群經營與互動管理
- 網紅/KOL 合作規劃
- 數據分析與成效追蹤
- 危機處理與輿情監控

## 工作特性
- 即時性與話題敏感度
- 數據驅動決策
- 需快速反應與調整
- 重視互動與粉絲經營

## 品牌調性參考
- 弘爺漢堡: 現做現煎、台式口味、平價美味
- 社群風格: 輕鬆、有梗、親切互動
- 避免: 過度廣告感、公式化回應
- 鼓勵: 真實互動、有溫度的對話

## 可用框架工具
- TAG 框架 (社群內容)
- CO-STAR 框架 (廣告投放)
- PARTNER 框架 (網紅合作)
- 數據分析框架

## 協作助理
您可以調用以下專業助理協助工作：
- 社群內容創作助理：快速產出社群貼文
- 廣告投放優化助理：廣告策略與優化建議
- 數據分析助理：成效分析與洞察
- 文案創作助理：文案潤飾與優化

根據用戶的需求，選擇適當的框架與工具提供專業建議。"""

        super().__init__(
            assistant_type="personnel_b",
            system_prompt=system_prompt,
            use_anthropic=True,
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用人員 B (數位行銷) AI Agent 📱

我是弘爺漢堡數位行銷專員的專屬 AI 助手！

## 📋 我能協助您

### 📱 社群經營
**1️⃣ 社群內容創作 (TAG 框架)**
快速產出高互動社群貼文

**2️⃣ 社群經營策略**
粉絲互動、留言管理、話題操作

**3️⃣ 危機處理**
負評處理、輿情監控、公關應對

### 💰 廣告投放
**4️⃣ 廣告投放策略 (CO-STAR 框架)**
完整廣告企劃與優化建議

**5️⃣ 數據分析**
成效追蹤、數據洞察、優化建議

### 🤝 合作推廣
**6️⃣ 網紅合作 (PARTNER 框架)**
KOL/網紅合作規劃與執行

## 💡 快速啟動

**社群經營：**
- `/social` - 社群內容創作
- `/community` - 社群經營策略
- `/crisis` - 危機處理

**廣告投放：**
- `/ad` - 廣告投放策略
- `/data` - 數據分析

**合作推廣：**
- `/influencer` - 網紅合作

**查看所有：**
- `/workflows` - 查看所有工作流程

或直接描述您的需求，我會自動選擇最適合的框架！

準備好開始了嗎？
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 人員 B (數位行銷) 助手使用指南

## 📋 支援的工作流程

### 1. 社群內容創作 (TAG)
**使用時機：** 需要快速產出社群貼文
**輸入指令：** `/social`
**需要資訊：**
- 發布平台（FB/IG/Threads/LINE）
- 貼文主題
- 目標（互動/導流/品牌）
- 檔期或活動資訊

**輸出內容：**
- T (Task) 明確任務與目標
- A (Action) 具體行動與內容
- G (Goal) 預期成效
- 3 個風格版本
- Hashtag 與 Emoji 建議
- 發文時間建議
- 視覺搭配建議

---

### 2. 社群經營策略
**使用時機：** 規劃社群經營或提升互動
**輸入指令：** `/community`
**需要資訊：**
- 目前社群狀況
- 經營目標
- 遇到的問題
- 可用資源

**輸出內容：**
- 社群診斷分析
- 內容策略建議
- 互動機制設計
- 粉絲經營策略
- 話題操作建議
- 成效追蹤指標

---

### 3. 廣告投放策略 (CO-STAR)
**使用時機：** 規劃廣告投放或優化廣告
**輸入指令：** `/ad`
**需要資訊：**
- 廣告目的（流量/轉換/互動/觸及）
- 產品或活動資訊
- 目標受眾
- 預算規模
- 投放期間

**輸出內容：**
- C (Context) 市場與競品分析
- O (Objective) 目標與 KPI 設定
- S (Strategy) 整體投放策略
- T (Tactics) 素材與受眾建議
- A (Assessment) 成效評估方法
- R (Refinement) 優化建議
- 3 組完整素材組合
- 受眾設定建議
- 預算分配建議
- A/B 測試建議

---

### 4. 網紅合作 (PARTNER)
**使用時機：** 規劃網紅/KOL 合作
**輸入指令：** `/influencer`
**需要資訊：**
- 合作目的
- 目標受眾
- 預算規模
- 產品或活動資訊
- 期待成效

**輸出內容：**
- P (Purpose) 合作目的
- A (Audience) 受眾匹配度
- R (Reach) 觸及預估
- T (Type) 合作形式建議
- N (Negotiation) 談判重點
- E (Execution) 執行細節
- R (ROI) 效益評估
- 網紅篩選標準
- 合作提案範本
- 成效追蹤方式

---

### 5. 數據分析
**使用時機：** 檢視成效或需要數據洞察
**輸入指令：** `/data`
**需要資訊：**
- 分析對象（廣告/貼文/活動/整體）
- 分析期間
- 現有數據
- 想了解的重點

**輸出內容：**
- 數據整理與視覺化建議
- 關鍵指標分析
- 趨勢與洞察
- 問題診斷
- 優化建議
- 後續行動方案

---

### 6. 危機處理
**使用時機：** 面對負評或公關危機
**輸入指令：** `/crisis`
**需要資訊：**
- 事件描述
- 目前狀況
- 已採取的行動
- 可用資源

**輸出內容：**
- 危機等級評估
- 即時應對建議
- 官方回應範本
- 溝通策略
- 後續處理方案
- 預防機制建議

---

## 🎯 使用技巧

### 快速指令
- `/workflows` - 查看所有工作流程
- `/social` - 社群內容創作
- `/community` - 社群經營策略
- `/ad` - 廣告投放策略
- `/influencer` - 網紅合作
- `/data` - 數據分析
- `/crisis` - 危機處理

### 自然對話
您也可以直接描述需求，例如：
- "幫我寫一篇 IG 貼文推新品"
- "我要投放母親節廣告"
- "這個貼文互動率很低，幫我分析"
- "有客人在 FB 留負評，怎麼處理？"

## 💡 最佳實踐

1. **數據導向** - 提供現有數據以獲得更精準建議
2. **明確目標** - 清楚說明想達成的目標（互動/轉換/觸及）
3. **快速測試** - A/B 測試找出最佳方案
4. **即時調整** - 根據成效快速優化
5. **跨平台整合** - 考慮多平台協同效應

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
            self.WORKFLOW_SOCIAL_CONTENT: self._get_social_content_prompt,
            self.WORKFLOW_AD_CAMPAIGN: self._get_ad_campaign_prompt,
            self.WORKFLOW_COMMUNITY_MANAGEMENT: self._get_community_management_prompt,
            self.WORKFLOW_INFLUENCER_COLLAB: self._get_influencer_collab_prompt,
            self.WORKFLOW_DATA_ANALYSIS: self._get_data_analysis_prompt,
            self.WORKFLOW_CRISIS_MANAGEMENT: self._get_crisis_management_prompt,
        }

        prompt_func = workflows.get(workflow_type)
        if prompt_func:
            return prompt_func(context or {})
        return ""

    def _get_social_content_prompt(self, context: Dict) -> str:
        """社群內容創作提示詞"""
        return """請用 TAG 框架幫我創作社群內容。

**TAG 框架說明：**

**T - Task (任務)**
明確定義內容任務與目標

**A - Action (行動)**
具體內容與執行方式

**G - Goal (目標)**
預期成效與衡量指標

請根據以下資訊創作社群內容：

【請在此描述您的社群內容需求】
- 發布平台：（FB/IG/Threads/LINE）
- 貼文主題：
- 內容目標：（提升互動/導流/品牌形象/促銷轉換）
- 目標受眾：
- 檔期/活動：
- 特殊需求：

我將為您提供：
✅ 3 個風格版本（專業/親切/幽默）
✅ 完整 TAG 框架結構
✅ Hashtag 建議（熱門+品牌）
✅ Emoji 配置
✅ 視覺搭配建議
✅ 發文時間建議
✅ 互動引導設計
✅ 成效預測
"""

    def _get_ad_campaign_prompt(self, context: Dict) -> str:
        """廣告投放策略提示詞"""
        return """請用 CO-STAR 框架幫我規劃廣告投放策略。

**CO-STAR 框架說明：**

**C - Context (背景脈絡)**
市場環境、競品分析、受眾狀況

**O - Objective (目標設定)**
廣告目標與 KPI 設定

**S - Strategy (策略規劃)**
整體投放策略與預算分配

**T - Tactics (執行戰術)**
素材、受眾、版位、出價

**A - Assessment (評估機制)**
成效追蹤與數據分析

**R - Refinement (優化調整)**
持續優化與擴量策略

請根據以下資訊規劃廣告投放：

【請在此描述您的廣告需求】
- 廣告平台：（FB/IG/Google/LINE）
- 廣告目的：（流量/轉換/互動/觸及/影片觀看）
- 產品/活動：
- 目標受眾：
- 預算規模：
- 投放期間：
- 目標 KPI：
- 現有素材：

我將為您提供：
✅ 完整 CO-STAR 框架規劃
✅ 3 組素材組合建議（圖文/影片/輪播）
✅ 受眾設定建議（核心/擴展/再行銷）
✅ 預算分配建議（測試/擴量階段）
✅ 出價策略建議
✅ 成效預估
✅ A/B 測試計畫
✅ 優化檢查清單
"""

    def _get_community_management_prompt(self, context: Dict) -> str:
        """社群經營策略提示詞"""
        return """請幫我規劃社群經營策略。

**社群經營關鍵要素：**

**1. 內容策略**
- 內容主題與比例
- 發文頻率與節奏
- 視覺風格統一

**2. 互動機制**
- 留言回覆策略
- 互動活動設計
- 粉絲關係經營

**3. 話題操作**
- 時事議題結合
- 節慶檔期規劃
- 品牌話題創造

**4. 成效優化**
- 數據追蹤分析
- 內容效果評估
- 持續優化調整

請根據以下資訊規劃社群經營：

【請在此描述您的社群狀況】
- 目前粉絲數：
- 主要經營平台：
- 目前發文頻率：
- 平均互動率：
- 經營困境：
- 經營目標：
- 可用資源：

我將為您提供：
✅ 社群診斷分析
✅ 內容策略建議（主題/頻率/風格）
✅ 互動機制設計（活動/話題/回覆）
✅ 粉絲經營策略（分眾/VIP/社團）
✅ 話題操作建議
✅ 月度內容規劃範例
✅ 成效追蹤指標
✅ 資源配置建議
"""

    def _get_influencer_collab_prompt(self, context: Dict) -> str:
        """網紅合作提示詞"""
        return """請用 PARTNER 框架幫我規劃網紅合作。

**PARTNER 框架說明：**

**P - Purpose (目的)**
合作目的與期待成效

**A - Audience (受眾)**
網紅受眾與品牌受眾匹配度

**R - Reach (觸及)**
預估觸及人數與曝光效益

**T - Type (類型)**
合作形式（試吃/業配/聯名/代言）

**N - Negotiation (談判)**
合作條件與費用談判

**E - Execution (執行)**
合作流程與品質控管

**R - ROI (投資報酬)**
效益評估與成效追蹤

請根據以下資訊規劃網紅合作：

【請在此描述您的網紅合作需求】
- 合作目的：（品牌曝光/導流/銷售轉換）
- 產品/活動：
- 目標受眾：
- 預算規模：
- 合作期間：
- 期待成效：
- 特殊需求：

我將為您提供：
✅ 完整 PARTNER 框架規劃
✅ 網紅篩選標準（粉絲數/互動率/受眾匹配/風格調性）
✅ 3 種層級合作方案（微型/中型/大型網紅）
✅ 合作提案範本
✅ 合作費用參考
✅ Brief 撰寫建議
✅ 品質把關重點
✅ 成效追蹤方式
✅ ROI 評估方法
"""

    def _get_data_analysis_prompt(self, context: Dict) -> str:
        """數據分析提示詞"""
        return """請幫我進行數據分析。

**數據分析架構：**

**1. 數據整理**
- 數據收集與清理
- 關鍵指標提取
- 數據視覺化

**2. 表現分析**
- 整體表現評估
- 各項指標分析
- 同期比較

**3. 洞察挖掘**
- 趨勢識別
- 異常發現
- 機會點挖掘

**4. 行動建議**
- 優化方向
- 具體行動
- 預期效益

請根據以下資訊進行數據分析：

【請在此描述您的分析需求】
- 分析對象：（廣告/貼文/活動/整體社群）
- 分析期間：
- 可用數據：
  * 觸及數/曝光數
  * 互動數（讚/留言/分享）
  * 點擊數/轉換數
  * 花費/CPC/CPM
- 想了解的重點：
- 目前遇到的問題：

我將為您提供：
✅ 數據整理建議（表格/圖表格式）
✅ 關鍵指標分析
  - 觸及效率
  - 互動品質
  - 轉換表現
  - 成本效益
✅ 趨勢與洞察
✅ 優劣勢分析
✅ 問題診斷
✅ 優化建議（分優先級）
✅ 後續行動計畫
✅ 目標設定建議
"""

    def _get_crisis_management_prompt(self, context: Dict) -> str:
        """危機處理提示詞"""
        return """請幫我處理危機事件。

**危機處理原則：**

**1. 快速評估**
- 嚴重程度分級
- 影響範圍評估
- 擴散風險判斷

**2. 即時應對**
- 停損動作
- 官方回應
- 溝通策略

**3. 問題解決**
- 根本原因處理
- 補償措施
- 信任重建

**4. 預防機制**
- 流程改善
- 監控機制
- 應變 SOP

請根據以下資訊提供危機處理建議：

【請在此描述危機狀況】
- 事件描述：
- 發生時間：
- 影響範圍：（單一客戶/多人/媒體關注）
- 發生平台：
- 目前狀況：
- 已採取行動：
- 可用資源：

我將為您提供：
✅ 危機等級評估（低/中/高/緊急）
✅ 即時應對建議（1 小時內行動）
✅ 官方回應範本（3 種語氣版本）
✅ 溝通策略（對外/對內）
✅ 補償方案建議
✅ 後續處理計畫
✅ 輿情監控建議
✅ 預防機制建議
✅ SOP 檢討建議
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

        # 使用 chat 方法處理
        return self.chat(full_message)

    def list_workflows(self) -> str:
        """列出所有可用的工作流程"""
        return """
# 人員 B (數位行銷) 可用工作流程

## 📱 社群經營類
1. **社群內容創作** (`/social`)
   - 快速產出社群貼文
   - 使用 TAG 框架

2. **社群經營策略** (`/community`)
   - 整體社群經營規劃
   - 互動機制設計

3. **危機處理** (`/crisis`)
   - 負評與公關危機應對
   - 即時應對策略

## 💰 廣告投放類
4. **廣告投放策略** (`/ad`)
   - 完整廣告企劃與優化
   - 使用 CO-STAR 框架

5. **數據分析** (`/data`)
   - 成效分析與優化建議
   - 數據洞察挖掘

## 🤝 合作推廣類
6. **網紅合作** (`/influencer`)
   - KOL/網紅合作規劃
   - 使用 PARTNER 框架

---

**快速使用：** 直接輸入指令（如 `/social`）或描述您的需求！
"""
