# 弘爺漢堡 AI 行銷團隊系統 (Hongye Burger AI Marketing Team System)

一套完整的 AI 行銷團隊系統，模擬真實行銷部門的角色分工與協作流程。

## 系統特色

🎯 **角色導向架構** - 模擬真實團隊組織結構
🤖 **智能工作流程** - 每個角色配備專業工作流程與框架
🔄 **協作機制** - 角色間可相互協作完成複雜任務
📊 **多種 AI 框架** - 整合 CoT、TAG、AIDA、IDEA、SCQA 等多種 AI 提示框架

## 團隊成員

### 1. Manager (主管) 👔
**職責：** 策略規劃與決策支援、團隊管理

**日常工作流程：**
- 每日工作規劃（CoT 框架）
- 社群內容快速產出（TAG 框架）
- 廣告投放決策（CO-STAR 框架）
- 專案決策分析（CoT 框架）
- 內容品質把關（RODES 框架）

**綜合管理工作流程：**
- 週會準備與記錄（SCQA 框架）
- 月度績效評估（RISE 框架）
- 年度規劃（ERA 框架）

**快速指令：** `/daily` `/social` `/ad` `/decide` `/qa` `/weekly` `/monthly` `/annual`

---

### 2. 人員 A (行銷企劃) 🎯
**職責：** 活動企劃、文案創作、IP 授權、異業合作

**工作流程：**
- 活動企劃（AIDA 框架）
- 文案撰寫（IDEA 框架）
- IP 授權專案（CO-STAR 框架）
- 異業合作策劃（CO-STAR 框架）
- 品牌故事（SCQA 框架）
- 內容日曆規劃

**快速指令：** `/activity` `/copy` `/ip` `/cross` `/story` `/calendar`

---

### 3. 人員 B (數位行銷) 📱
**職責：** 社群經營、廣告投放、數據分析、網紅合作

**工作流程：**
- 社群內容創作（TAG 框架）
- 廣告投放策略（CO-STAR 框架）
- 社群經營策略
- 網紅合作（PARTNER 框架）
- 數據分析
- 危機處理

**快速指令：** `/social` `/ad` `/community` `/influencer` `/data` `/crisis`

---

### 4. 人員 C (視覺設計) 🎨
**職責：** 品牌視覺、活動設計、包裝設計、空間設計

**工作流程：**
- 視覺概念發想
- 活動視覺規劃
- 品牌視覺規範
- 社群視覺設計
- 包裝設計
- 空間視覺設計

**快速指令：** `/concept` `/campaign` `/brand` `/social` `/package` `/space`

---

### 5. 人員 D (美編專員) 🖌️
**職責：** 設計執行、簡報製作、社群圖文、印刷製作

**工作流程：**
- 設計執行指引
- 簡報製作
- 社群圖文製作
- 印刷製作規範
- 檔案管理
- 設計品質檢查

**快速指令：** `/design` `/ppt` `/social` `/print` `/file` `/qa`

---

### 6. 人員 E (團購PM) 📦
**職責：** 團購企劃、廠商管理、物流配送、客服處理

**工作流程：**
- 團購企劃
- 廠商管理
- 物流配送規劃
- 客服處理
- 成效追蹤
- 危機處理

**快速指令：** `/plan` `/vendor` `/logistics` `/cs` `/track` `/crisis`

---

## 技術架構

```
roaddy/
├── src/
│   ├── assistants/          # 各類助手模組
│   │   ├── base_assistant.py      # 基礎助手類別
│   │   ├── manager.py             # Manager 主管
│   │   ├── personnel_a.py         # 人員 A (行銷企劃)
│   │   ├── personnel_b.py         # 人員 B (數位行銷)
│   │   ├── personnel_c.py         # 人員 C (視覺設計)
│   │   ├── personnel_d.py         # 人員 D (美編專員)
│   │   └── personnel_e.py         # 人員 E (團購PM)
│   ├── api/                 # API 整合層
│   │   ├── openai_client.py       # OpenAI API
│   │   ├── anthropic_client.py    # Anthropic API
│   │   └── google_search.py       # Google Search API
│   ├── utils/               # 工具函數
│   │   ├── logger.py              # 日誌系統
│   │   ├── config_loader.py       # 配置載入
│   │   └── prompts.py             # 提示詞管理
│   └── main.py             # 主程式入口
├── config/                  # 配置文件
│   └── config.yaml                # 系統配置
├── examples/               # 使用範例
│   ├── manager_usage.py           # Manager 使用範例
│   └── api_usage.py               # API 使用範例
├── tests/                   # 測試文件
├── .env.example            # 環境變數範例
├── requirements.txt        # Python 依賴
├── run.sh                  # Linux/Mac 啟動腳本
└── run.bat                 # Windows 啟動腳本
```

## 快速開始

### 方式一：使用啟動腳本（推薦）

**Linux/Mac：**
```bash
./run.sh
```

**Windows：**
```bash
run.bat
```

啟動腳本會自動：
- 創建虛擬環境
- 安裝依賴套件
- 檢查配置文件
- 啟動系統

### 方式二：手動安裝

#### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

#### 2. 配置環境變數

複製 `.env.example` 到 `.env` 並填入您的 API 金鑰：

```bash
cp .env.example .env
```

編輯 `.env` 文件：
```env
OPENAI_API_KEY=sk-your-openai-api-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-api-key
GOOGLE_API_KEY=your-google-api-key  # 選用
GOOGLE_CSE_ID=your-google-cse-id    # 選用
```

#### 3. 運行程式

```bash
# 互動式選單
python src/main.py

# 直接啟動指定助手
python src/main.py -a 1  # Manager (主管)
python src/main.py -a 2  # 人員 A (行銷企劃)
python src/main.py -a 3  # 人員 B (數位行銷)
python src/main.py -a 4  # 人員 C (視覺設計)
python src/main.py -a 5  # 人員 D (美編專員)
python src/main.py -a 6  # 人員 E (團購PM)
```

## 使用方式

### 1. 啟動系統

運行 `python src/main.py` 後會看到歡迎畫面：

```
╭─ 歡迎 ─────────────────────────────────╮
│ 🚀 弘爺漢堡 AI 行銷團隊系統             │
│                                        │
│ 1. Manager (主管)                      │
│ 2. 人員 A (行銷企劃)                    │
│ 3. 人員 B (數位行銷)                    │
│ 4. 人員 C (視覺設計)                    │
│ 5. 人員 D (美編專員)                    │
│ 6. 人員 E (團購PM)                      │
│                                        │
│ [0] 退出系統                           │
╰────────────────────────────────────────╯
```

### 2. 選擇助手

輸入數字選擇您需要的助手，系統會顯示該助手的歡迎訊息和功能說明。

### 3. 開始對話

直接輸入您的需求，或使用快速指令啟動特定工作流程：

**範例 1 - 自然對話：**
```
You: 我要規劃母親節活動
```

**範例 2 - 使用快速指令：**
```
You: /activity
```

### 4. 對話命令

在與助手對話時，可以使用以下命令：

- `/help` - 查看助手幫助訊息
- `/workflows` - 查看所有可用工作流程（部分助手支援）
- `/clear` - 清空對話歷史
- `/export` - 匯出對話記錄
- `/quit` - 返回主選單

### 5. 工作流程快速指令

每個助手都有專屬的快速指令，可以快速啟動特定工作流程。例如：

**Manager：**
- `/daily` - 每日工作規劃
- `/social` - 社群內容快速產出
- `/ad` - 廣告投放決策

**人員 A：**
- `/activity` - 活動企劃
- `/copy` - 文案撰寫
- `/ip` - IP 授權專案

詳細的快速指令請參考各助手的歡迎訊息或使用 `/help` 查看。

## AI 框架說明

本系統整合多種專業 AI 提示框架：

### 策略規劃類
- **CoT (Chain of Thought)** - 鏈式思考，適合複雜決策
- **CO-STAR** - 完整專案規劃框架
- **SCQA** - 情境-衝突-問題-解答，適合品牌故事

### 創意執行類
- **TAG (Task-Action-Goal)** - 任務-行動-目標，快速執行
- **AIDA (Attention-Interest-Desire-Action)** - 經典行銷漏斗
- **IDEA (Interest-Detail-Evidence-Action)** - 文案創作框架

### 評估優化類
- **RODES (Role-Objective-Details-Engagement-Structure)** - 內容品質評估
- **RISE (Recap-Insights-Suggestions-Execution)** - 績效評估
- **ERA (Envision-Roadmap-Alignment)** - 年度規劃

### 合作協調類
- **PARTNER** - 網紅合作專用框架

## API 整合

本系統整合以下 AI 服務：

- **Anthropic Claude 3.5 Sonnet** - 主要 AI 模型，用於所有助手
- **OpenAI GPT-4o** - 備用 AI 模型（可選）
- **DALL-E 3** - 圖片生成（文案助手，可選）
- **Google Search API** - 網頁搜尋（可選）

## 使用範例

查看 `examples/` 目錄中的範例檔案：

- `manager_usage.py` - Manager 助手完整使用範例
- `api_usage.py` - API 客戶端使用範例
- `basic_usage.py` - 基本對話使用範例

## 配置說明

### config/config.yaml

系統配置文件，包含：
- 助手配置（模型、溫度、Token 限制）
- API 配置（超時、重試）
- 日誌配置
- 輸出配置

### .env

環境變數文件，包含敏感資訊（不會提交到 Git）：
- API 金鑰
- 搜尋引擎配置

## 對話歷史

系統會自動保存對話歷史到 `conversations/` 目錄：
- 每個助手有獨立的歷史文件
- 支援匯出為 JSON 或 Markdown 格式
- 可用於訓練或分析

## 開發與貢獻

### 目錄結構說明

- `src/assistants/` - 各個 AI 助手的實現
- `src/api/` - 第三方 API 整合
- `src/utils/` - 工具函數和配置載入
- `config/` - 配置文件
- `examples/` - 使用範例
- `tests/` - 單元測試

### 新增助手

1. 在 `src/assistants/` 創建新的助手文件
2. 繼承 `BaseAssistant` 類別
3. 實現 `get_welcome_message()` 和 `get_help_message()` 方法
4. 在 `config/config.yaml` 添加助手配置
5. 在 `src/assistants/__init__.py` 導出助手類別
6. 在 `src/main.py` 註冊助手

### 運行測試

```bash
pytest tests/
```

## 品牌資訊

**弘爺漢堡**
- 品牌定位：現做現煎、台式口味、平價美味
- 品牌個性：親切、有溫度、接地氣
- 溝通風格：輕鬆、有梗、貼近生活

## 授權

MIT License

## 聯絡方式

如有問題或建議，歡迎聯繫開發團隊。

---

**版本：** 2.0.0 (Role-Based Architecture)
**最後更新：** 2025-01-24
