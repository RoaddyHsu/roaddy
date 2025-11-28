# 使用指南

## 快速開始

### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

### 2. 配置 API 金鑰 ⚠️ 重要

#### 步驟 1：取得 API 金鑰

**Anthropic Claude API（必須）：**
1. 前往 [Anthropic Console](https://console.anthropic.com/)
2. 註冊並登入
3. 進入 **API Keys** 頁面創建金鑰
4. 複製金鑰（格式：`sk-ant-api03-xxxxx...`）

**OpenAI API（選填，用於圖片生成）：**
1. 前往 [OpenAI Platform](https://platform.openai.com/)
2. 進入 **API Keys** 頁面創建金鑰
3. 複製金鑰（格式：`sk-xxxxx...`）

#### 步驟 2：設定環境變數

複製範例檔案：
```bash
cp .env.example .env
```

編輯 `.env` 文件並填入**真實的** API 金鑰：
```bash
nano .env
```

**必填項目：**
```env
# Anthropic API 配置（必須）
ANTHROPIC_API_KEY=sk-ant-api03-你的實際金鑰在這裡
```

**選填項目：**
```env
# OpenAI API 配置（選用，用於圖片生成）
OPENAI_API_KEY=sk-你的實際金鑰在這裡

# Google API 配置（選用，用於搜尋功能）
GOOGLE_API_KEY=your-google-api-key
GOOGLE_SEARCH_ENGINE_ID=your-search-engine-id
```

⚠️ **注意：** 請將 `your-anthropic-api-key-here` 替換成真實的 API 金鑰！

#### 步驟 3：驗證設定

測試 API 金鑰是否正確：
```bash
cd /workspaces/roaddy
python -m pytest tests/test_assistants.py::TestAssistants::test_manager_init -v
```

如果看到 `PASSED`，表示設定成功！

### 3. 運行程式

#### 方式 1：使用啟動腳本（推薦）

```bash
cd /workspaces/roaddy
./run.sh              # 互動式選單
./run.sh -a 1         # 直接啟動 Manager
```

啟動腳本會自動：
- 創建並啟動虛擬環境
- 安裝所有依賴套件
- 設定正確的路徑
- 檢查 .env 配置

#### 方式 2：手動執行

```bash
# 設定 Python 路徑（重要！）
export PYTHONPATH=/workspaces/roaddy:$PYTHONPATH

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

## 功能說明

### 1. 內容行銷助手

**功能：** SEO 優化與內容策略

**適用場景：**
- 網站 SEO 優化
- 關鍵字研究與分析
- 內容策略規劃
- 技術面 SEO 檢查

**使用方式：**
1. 選擇「1. 內容行銷助手」
2. 提供網站基本資訊
3. 獲取 SEO 優化建議

### 2. 文案撰寫助手

**功能：** 跨平台文案創作

**支援平台：**
- Facebook（長篇內容，500-1000字）
- Instagram（中短篇，300-500字）
- Threads（短篇，300字以內）
- 部落格（長篇，1000字以上）
- LinkedIn（專業內容，400-600字）

**使用方式：**
1. 選擇「2. 文案撰寫助手」
2. 指定目標平台和主題
3. 獲取客製化文案

**範例：**
```
用戶: 請為我的咖啡店寫一篇 Instagram 文案，主題是新品上市，風格輕鬆活潑
```

### 3. 社群行銷助手

**功能：** 社群策略規劃

**提供服務：**
- 社群平台配置建議
- 內容策略規劃
- 營運時程表
- 廣告投放策略

**使用方式：**
1. 選擇「3. 社群行銷助手」
2. 提供品牌資訊和目標
3. 獲取完整社群行銷策略

### 4. 品牌策略顧問

**功能：** 品牌定位分析

**諮詢流程：**
1. 品牌基礎探索
2. 競爭優勢分析
3. 策略定位制定
4. 策略活動規劃

**使用方式：**
1. 選擇「4. 品牌策略顧問」
2. 按照引導回答問題
3. 獲取品牌策略規劃建議書

### 5. 創意行銷助手

**功能：** 創意發想系統

**特色：**
- 提供 3-5 個創意點子
- 即時互動討論
- 可行性分析
- 執行方案規劃

**使用方式：**
1. 選擇「5. 創意行銷助手」
2. 描述行銷目標和需求
3. 從多個創意方案中選擇

### 6. 電商行銷助手

**功能：** 電商策略規劃

**涵蓋範圍：**
- 全通路銷售策略
- 社群行銷規劃
- KOL 合作計畫
- 團購與口碑行銷

**預算配置建議：**
- 社群行銷：25%
- KOL 合作：20%
- 團購經營：20%
- 口碑行銷：15%
- 直播銷售：10%
- 其他策略：10%

### 7. 廣告投手

**功能：** 廣告投放策略

**服務內容：**
- 平台配置建議
- 廣告素材規劃
- 投放策略規劃
- 數據追蹤與優化

**預算配置：**

**B2B 市場：**
- LinkedIn Ads: 40%
- Google Ads: 35%
- 專業媒體: 15%
- 其他平台: 10%

**B2C 市場：**
- Meta Ads: 35%
- Google Ads: 30%
- TikTok Ads: 20%
- 其他平台: 15%

## 對話命令

在與助手對話時，可以使用以下命令：

- `/help` - 查看助手幫助訊息
- `/clear` - 清空對話歷史
- `/export` - 匯出對話記錄（JSON 和 Markdown 格式）
- `/quit` - 返回主選單

## 進階功能

### 對話歷史

系統會自動保存對話歷史，下次使用時可以透過鍵盤上下鍵瀏覽歷史輸入。

歷史文件位置：`conversations/{assistant_type}_history.txt`

### 對話匯出

使用 `/export` 命令可以將對話匯出為：
- JSON 格式：包含完整對話結構
- Markdown 格式：適合閱讀和分享

匯出文件位置：`conversations/`

### 自訂配置

編輯 `config/config.yaml` 可以調整：
- 各助手的模型選擇
- 溫度參數
- Token 上限
- 圖片生成設定

## 常見問題

### Q1: API 金鑰認證錯誤 ⚠️

**錯誤訊息：**
```
Error code: 401 - authentication_error: invalid x-api-key
```

**原因：** API 金鑰無效或未正確設定

**解決方法：**
1. 確認 `.env` 文件存在：
   ```bash
   ls -la .env
   ```

2. 檢查是否已填入真實的 API 金鑰（不是範例值）：
   ```bash
   cat .env | grep ANTHROPIC_API_KEY
   ```
   
3. 如果看到 `your_anthropic_api_key_here`，表示還沒填入真實金鑰！

4. 編輯 `.env` 並填入從 Anthropic Console 獲得的真實金鑰：
   ```bash
   nano .env
   ```

5. 重新啟動程式：
   ```bash
   ./run.sh
   ```

### Q2: 模組導入錯誤

**錯誤訊息：**
```
ModuleNotFoundError: No module named 'anthropic'
ImportError: attempted relative import beyond top-level package
```

**解決方法：**

**方法 1：使用啟動腳本（推薦）**
```bash
./run.sh
```

**方法 2：安裝依賴並設定路徑**
```bash
# 安裝依賴
pip install -r requirements.txt

# 設定 Python 路徑
export PYTHONPATH=/workspaces/roaddy:$PYTHONPATH

# 執行程式
python src/main.py
```

### Q3: 測試失敗

**錯誤訊息：** 測試無法執行或失敗

**解決方法：**
```bash
# 使用 pytest 模組方式執行
cd /workspaces/roaddy
python -m pytest tests/ -v

# 執行特定測試
python -m pytest tests/test_assistants.py::TestAssistants::test_manager_init -v
```

### Q4: 虛擬環境問題

**解決方法：**
```bash
# 刪除舊的虛擬環境
rm -rf venv

# 重新執行啟動腳本（會自動創建虛擬環境）
./run.sh
```

## 技術支援

如有問題或建議，請提交 Issue 到：
cd /workspaces/roaddy
pytest tests/test_assistants.py
