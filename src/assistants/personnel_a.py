"""
人員 A (行銷企劃) AI Agent
"""

from .base_assistant import BaseAssistant
from typing import Dict


class PersonnelAAssistant(BaseAssistant):
    """人員 A (行銷企劃) 專用助手 - 活動企劃與文案創作"""

    # 工作流程類型
    WORKFLOW_ACTIVITY_PLANNING = "activity_planning"  # 活動企劃
    WORKFLOW_COPYWRITING = "copywriting"  # 文案撰寫
    WORKFLOW_IP_LICENSING = "ip_licensing"  # IP 授權專案
    WORKFLOW_CROSS_INDUSTRY = "cross_industry"  # 異業合作
    WORKFLOW_BRAND_STORY = "brand_story"  # 品牌故事
    WORKFLOW_CONTENT_CALENDAR = "content_calendar"  # 內容日曆規劃

    def __init__(self):
        # 主系統提示詞
        system_prompt = """你是弘爺漢堡行銷企劃專員 (人員 A) 的專屬 AI 助手。

## 核心職責
- 活動企劃與執行
- 文案創作與優化
- IP 授權專案規劃
- 異業合作策劃
- 品牌故事撰寫
- 內容日曆規劃

## 工作特性
- 創意與策略並重
- 需整合線上線下活動
- 重視品牌調性一致性
- 強調故事性與共鳴度

## 品牌調性參考
- 弘爺漢堡: 現做現煎、台式口味、平價美味
- 品牌個性: 親切、有溫度、接地氣
- 溝通風格: 輕鬆、有梗、貼近生活
- 避免: 過度正式、老派用語、浮誇不實

## 可用框架工具
- IDEA 框架 (文案創作)
- AIDA 框架 (行銷活動)
- SCQA 框架 (品牌故事)
- CO-STAR 框架 (專案規劃)

## 協作助理
您可以調用以下專業助理協助工作：
- 策略規劃助理：協助整體策略制定
- 品牌活動企劃助理：提供活動執行細節
- 文案創作助理：協助文案潤飾與優化
- IP 授權專案助理：提供 IP 合作專業建議

根據用戶的需求，選擇適當的框架與工具提供專業建議。"""

        super().__init__(
            assistant_type="personnel_a",
            system_prompt=system_prompt,
            use_anthropic=True,
        )

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        return """
# 歡迎使用人員 A (行銷企劃) AI Agent 🎯

我是弘爺漢堡行銷企劃專員的專屬 AI 助手！

## 📋 我能協助您

### 🎪 活動企劃與執行
**1️⃣ 活動企劃 (AIDA 框架)**
完整的活動規劃，從概念到執行細節

**2️⃣ 異業合作策劃 (CO-STAR 框架)**
跨品牌合作提案與執行方案

**3️⃣ IP 授權專案 (CO-STAR 框架)**
IP 聯名合作規劃與授權管理

### ✍️ 文案創作與優化
**4️⃣ 文案撰寫 (IDEA 框架)**
各類行銷文案創作（廣告、社群、EDM 等）

**5️⃣ 品牌故事 (SCQA 框架)**
品牌故事與企業理念撰寫

### 📅 內容規劃
**6️⃣ 內容日曆 (專案規劃框架)**
月度/季度內容規劃與排程

## 💡 快速啟動

**活動規劃：**
- `/activity` - 活動企劃
- `/cross` - 異業合作
- `/ip` - IP 授權專案

**文案創作：**
- `/copy` - 文案撰寫
- `/story` - 品牌故事

**內容規劃：**
- `/calendar` - 內容日曆

**查看所有：**
- `/workflows` - 查看所有工作流程

或直接描述您的需求，我會自動選擇最適合的框架！

準備好開始了嗎？
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# 人員 A (行銷企劃) 助手使用指南

## 📋 支援的工作流程

### 1. 活動企劃 (AIDA)
**使用時機：** 規劃新活動或檔期
**輸入指令：** `/activity`
**需要資訊：**
- 活動目的與目標
- 目標受眾
- 預算範圍
- 時間期限

**輸出內容：**
- A (Attention) 吸引注意策略
- I (Interest) 引起興趣手法
- D (Desire) 創造渴望元素
- A (Action) 行動呼籲設計
- 完整執行時程表
- 預算分配建議

---

### 2. 文案撰寫 (IDEA)
**使用時機：** 需要創作各類行銷文案
**輸入指令：** `/copy`
**需要資訊：**
- 文案類型（廣告/社群/EDM/DM）
- 主題或產品
- 目標受眾
- 字數要求
- 風格偏好

**輸出內容：**
- I (Interest) 引人入勝的開頭
- D (Detail) 詳細的產品/服務說明
- E (Evidence) 可信的證據或案例
- A (Action) 明確的行動呼籲
- 3 個文案版本供選擇
- Hashtag 與 Emoji 建議

---

### 3. IP 授權專案 (CO-STAR)
**使用時機：** 規劃 IP 聯名合作
**輸入指令：** `/ip`
**需要資訊：**
- IP 名稱與特性
- 合作形式（產品/活動/空間）
- 合作期程
- 預算規模

**輸出內容：**
- 完整合作提案
- 產品/活動設計建議
- 行銷推廣策略
- 授權條件建議
- 風險評估
- 效益預估

---

### 4. 異業合作策劃 (CO-STAR)
**使用時機：** 規劃跨品牌合作
**輸入指令：** `/cross`
**需要資訊：**
- 合作對象產業/品牌
- 合作目的
- 雙方資源
- 期待效益

**輸出內容：**
- 合作方案建議（3 種層級）
- 價值交換模式
- 行銷活動企劃
- 分潤機制建議
- 合作協議重點
- 執行時程表

---

### 5. 品牌故事 (SCQA)
**使用時機：** 撰寫品牌內容或理念傳達
**輸入指令：** `/story`
**需要資訊：**
- 故事主題
- 想傳達的核心價值
- 目標受眾
- 使用情境

**輸出內容：**
- S (Situation) 情境設定
- C (Complication) 衝突/問題
- Q (Question) 引發思考
- A (Answer) 解決方案/價值主張
- 完整故事文本
- 應用建議（官網/社群/新聞稿）

---

### 6. 內容日曆規劃
**使用時機：** 規劃月度或季度內容
**輸入指令：** `/calendar`
**需要資訊：**
- 規劃期間（月/季/年）
- 重要檔期
- 產品上市計畫
- 資源配置

**輸出內容：**
- 完整內容日曆
- 主題分類與比例
- 各週重點與節奏
- 跨平台內容配置
- 需求資源清單

---

## 🎯 使用技巧

### 快速指令
- `/workflows` - 查看所有工作流程
- `/activity` - 活動企劃
- `/copy` - 文案撰寫
- `/ip` - IP 授權專案
- `/cross` - 異業合作
- `/story` - 品牌故事
- `/calendar` - 內容日曆

### 自然對話
您也可以直接描述需求，例如：
- "我要規劃母親節活動"
- "幫我寫一篇新品上市的 FB 文案"
- "我們想跨界合作，對象是咖啡品牌"
- "幫我寫一個品牌創立故事"

## 💡 最佳實踐

1. **提供完整 Brief** - 包含目標、受眾、預算、時程
2. **參考過往案例** - 提供過去成功或失敗的案例
3. **明確品牌調性** - 確保與弘爺漢堡品牌個性一致
4. **多輪優化** - 可以針對輸出內容進一步討論修改
5. **整合協作** - 需要時可請我聯繫其他專業助理

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
            self.WORKFLOW_ACTIVITY_PLANNING: self._get_activity_planning_prompt,
            self.WORKFLOW_COPYWRITING: self._get_copywriting_prompt,
            self.WORKFLOW_IP_LICENSING: self._get_ip_licensing_prompt,
            self.WORKFLOW_CROSS_INDUSTRY: self._get_cross_industry_prompt,
            self.WORKFLOW_BRAND_STORY: self._get_brand_story_prompt,
            self.WORKFLOW_CONTENT_CALENDAR: self._get_content_calendar_prompt,
        }

        prompt_func = workflows.get(workflow_type)
        if prompt_func:
            return prompt_func(context or {})
        return ""

    def _get_activity_planning_prompt(self, context: Dict) -> str:
        """活動企劃提示詞"""
        return """請用 AIDA 框架幫我規劃活動。

**AIDA 框架說明：**

**A - Attention (吸引注意)**
如何在眾多資訊中脫穎而出？
- 視覺設計
- 主題命名
- 前導宣傳

**I - Interest (引起興趣)**
如何讓受眾想了解更多？
- 獨特賣點
- 價值主張
- 互動機制

**D - Desire (創造渴望)**
如何讓受眾想要參與？
- 限時限量
- 獨家優惠
- 情感連結

**A - Action (行動呼籲)**
如何促使受眾立即行動？
- CTA 設計
- 參與門檻
- 轉換路徑

請根據以下資訊規劃活動：

【請在此描述您的活動需求】
- 活動目的：
- 目標受眾：
- 預算範圍：
- 執行期間：
- 期待成效：

我將為您提供：
✅ 完整 AIDA 框架活動企劃
✅ 執行時程與分工
✅ 預算分配建議
✅ 風險評估與備案
✅ 成效追蹤指標
"""

    def _get_copywriting_prompt(self, context: Dict) -> str:
        """文案撰寫提示詞"""
        return """請用 IDEA 框架幫我創作文案。

**IDEA 框架說明：**

**I - Interest (引人入勝)**
第一句話就抓住注意力
- 痛點切入
- 好奇心觸發
- 情境共鳴

**D - Detail (詳細說明)**
清楚介紹產品/服務
- 核心特色
- 使用情境
- 價值利益

**E - Evidence (提供證據)**
建立信任與可信度
- 數據支持
- 客戶見證
- 權威背書

**A - Action (行動呼籲)**
明確告知下一步
- 清晰的 CTA
- 降低門檻
- 製造急迫感

請根據以下資訊創作文案：

【請在此描述您的文案需求】
- 文案類型：（廣告/社群/EDM/DM/新聞稿）
- 主題/產品：
- 目標受眾：
- 字數要求：
- 風格偏好：（活潑/專業/溫馨/幽默）
- 發布平台：
- 特殊需求：

我將為您提供：
✅ 3 個風格版本供選擇
✅ IDEA 框架完整結構
✅ Hashtag 建議
✅ Emoji 配置
✅ 視覺搭配建議
✅ A/B 測試建議
"""

    def _get_ip_licensing_prompt(self, context: Dict) -> str:
        """IP 授權專案提示詞"""
        return """請用 CO-STAR 框架幫我規劃 IP 授權專案。

**CO-STAR 框架說明：**

**C - Context (背景脈絡)**
了解合作背景與市場環境

**O - Objective (目標設定)**
明確定義專案目標與 KPI

**S - Strategy (策略規劃)**
制定整體合作策略

**T - Tactics (執行戰術)**
具體行動方案與時程

**A - Assessment (評估機制)**
效益評估與風險控管

**R - Refinement (優化調整)**
持續改善與延伸規劃

請根據以下資訊規劃 IP 授權專案：

【請在此描述您的 IP 專案需求】
- IP 名稱：
- IP 特性：（風格/受眾/知名度）
- 合作形式：（產品聯名/活動合作/空間改造/數位內容）
- 合作期程：
- 預算規模：
- 目標效益：
- 特殊限制：

我將為您提供：
✅ 完整 CO-STAR 專案規劃
✅ 產品/活動設計建議
✅ 行銷推廣策略
✅ 授權條件建議（費用/使用範圍/期限）
✅ 風險評估與應對
✅ 效益預估（銷售/品牌/話題）
✅ 執行時程表與里程碑
"""

    def _get_cross_industry_prompt(self, context: Dict) -> str:
        """異業合作提示詞"""
        return """請用 CO-STAR 框架幫我規劃異業合作。

**CO-STAR 框架說明：**

**C - Context (背景脈絡)**
雙方品牌現況與市場定位

**O - Objective (目標設定)**
合作目的與期待成效

**S - Strategy (策略規劃)**
合作模式與價值交換

**T - Tactics (執行戰術)**
活動企劃與推廣方案

**A - Assessment (評估機制)**
效益評估與成本分攤

**R - Refinement (優化調整)**
長期合作可能性評估

請根據以下資訊規劃異業合作：

【請在此描述您的異業合作需求】
- 合作對象：（產業/品牌/規模）
- 合作目的：
- 我方資源：（門市/社群/會員/預算）
- 期待對方資源：
- 合作期程：
- 預算規模：
- 期待效益：

我將為您提供：
✅ 3 種層級合作方案（基礎/進階/深度）
✅ 價值交換模式設計
✅ 完整行銷活動企劃
✅ 分潤機制建議
✅ 合作協議重點提示
✅ 風險評估
✅ 執行時程表
✅ 成效追蹤指標
"""

    def _get_brand_story_prompt(self, context: Dict) -> str:
        """品牌故事提示詞"""
        return """請用 SCQA 框架幫我撰寫品牌故事。

**SCQA 框架說明：**

**S - Situation (情境)**
設定故事背景與場景

**C - Complication (衝突)**
點出問題或挑戰

**Q - Question (提問)**
引發受眾思考

**A - Answer (解答)**
提供解決方案與價值主張

請根據以下資訊撰寫品牌故事：

【請在此描述您的故事需求】
- 故事主題：（品牌創立/產品研發/企業理念/社會責任）
- 核心價值：
- 目標受眾：
- 使用情境：（官網/新聞稿/社群/影片腳本）
- 字數要求：
- 風格偏好：（感性/理性/勵志/溫馨）
- 特殊需求：

我將為您提供：
✅ 完整 SCQA 框架故事
✅ 情感連結點設計
✅ 金句/標語建議
✅ 多版本應用（長/中/短）
✅ 視覺呈現建議
✅ 應用場景建議
✅ 傳播策略建議
"""

    def _get_content_calendar_prompt(self, context: Dict) -> str:
        """內容日曆規劃提示詞"""
        return """請幫我規劃內容日曆。

**內容日曆規劃重點：**

**1. 策略層**
- 整體內容目標
- 主題分類與比例
- 品牌訊息一致性

**2. 執行層**
- 發布節奏與頻率
- 跨平台內容配置
- 資源需求評估

**3. 靈活性**
- 檔期與時事整合
- 突發事件應對
- 成效追蹤與調整

請根據以下資訊規劃內容日曆：

【請在此描述您的規劃需求】
- 規劃期間：（月/季/半年/年）
- 重要檔期：（節慶/活動/新品上市）
- 產品計畫：
- 發布平台：（FB/IG/LINE/官網/EDM）
- 發布頻率：
- 內容類型偏好：（產品/優惠/品牌/互動/知識）
- 資源配置：（人力/預算/素材）

我將為您提供：
✅ 完整內容日曆（Excel 格式規劃）
✅ 主題分類與內容比例
✅ 各週重點與發布節奏
✅ 跨平台內容配置策略
✅ 素材需求清單
✅ 協作分工建議
✅ 成效追蹤指標
✅ 應變機制建議
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
# 人員 A (行銷企劃) 可用工作流程

## 🎪 活動企劃類
1. **活動企劃** (`/activity`)
   - 完整活動規劃與執行方案
   - 使用 AIDA 框架

2. **異業合作** (`/cross`)
   - 跨品牌合作提案與執行
   - 使用 CO-STAR 框架

3. **IP 授權專案** (`/ip`)
   - IP 聯名合作規劃
   - 使用 CO-STAR 框架

## ✍️ 文案創作類
4. **文案撰寫** (`/copy`)
   - 各類行銷文案創作
   - 使用 IDEA 框架

5. **品牌故事** (`/story`)
   - 品牌故事與理念撰寫
   - 使用 SCQA 框架

## 📅 內容規劃類
6. **內容日曆** (`/calendar`)
   - 月度/季度內容規劃
   - 專案規劃框架

---

**快速使用：** 直接輸入指令（如 `/activity`）或描述您的需求！
"""
