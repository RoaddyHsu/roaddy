# AI 行銷顧問系統 (AI Marketing Consultant System)

一套完整的 AI 行銷助手系統，整合多個專業行銷顧問功能。

## 功能特色

### 1. 內容行銷助手 (Content Marketing Assistant)
- SEO 優化建議
- 技術面與內容面分析
- 關鍵字研究與佈局
- 數據追蹤與分析

### 2. 文案撰寫助手 (Copywriting Assistant)
- 跨平台文案生成（Facebook、Instagram、Threads、部落格、LinkedIn）
- 平台特性優化
- 自動生成配圖（DALL-E 3）
- HashTag 和 Emoji 智能配置

### 3. 社群行銷助手 (Social Media Marketing Assistant)
- 社群平台配置建議
- 內容策略規劃
- 營運時程表
- 廣告投放策略

### 4. 品牌策略顧問 (Brand Strategy Consultant)
- 競爭優勢分析
- 策略定位建議
- 策略活動系統（SAS）
- 執行路徑規劃

### 5. 創意行銷助手 (Creative Marketing Assistant)
- AI 輔助創意發想
- 即時互動討論
- 執行方案規劃
- 資源配置建議

### 6. 電商行銷助手 (E-commerce Marketing Assistant)
- 全通路銷售策略
- KOL 合作計畫
- 團購與口碑行銷
- 數據追蹤與優化

### 7. 廣告投手 (Ad Manager)
- 跨平台廣告策略
- 預算配置建議
- 目標受眾定位
- ROI 優化

## 技術架構

```
roaddy/
├── src/
│   ├── assistants/          # 各類助手模組
│   ├── api/                 # API 整合層
│   ├── utils/               # 工具函數
│   └── main.py             # 主程式入口
├── config/                  # 配置文件
├── tests/                   # 測試文件
└── examples/               # 使用範例
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
```

#### 3. 運行程式

```bash
# 互動式選單
python src/main.py

# 直接啟動指定助手
python src/main.py -a 1  # 內容行銷助手
python src/main.py -a 2  # 文案撰寫助手
# ... 依此類推
```

## 對話命令

在與助手對話時，可以使用以下命令：

- `/help` - 查看助手幫助訊息
- `/clear` - 清空對話歷史
- `/export` - 匯出對話記錄
- `/quit` - 返回主選單

## API 整合

本系統整合以下 API：
- **OpenAI API** - GPT-4o、DALL-E 3
- **Anthropic API** - Claude 3.5 Sonnet
- **Google Search API** - 網頁搜尋、新聞搜尋、圖片搜尋（選用）

## 文檔

- [使用指南](docs/USAGE.md) - 詳細的功能說明和使用方式
- [API 文檔](docs/API.md) - API 接口說明和範例
- [使用範例](examples/) - 程式碼範例

## 專案結構

```
roaddy/
├── src/                    # 原始碼
│   ├── assistants/        # 助手模組
│   ├── api/              # API 整合層
│   ├── utils/            # 工具函數
│   └── main.py          # 主程式
├── config/               # 配置文件
├── docs/                # 文檔
├── examples/            # 使用範例
├── tests/              # 測試文件
├── conversations/      # 對話記錄（自動生成）
└── logs/              # 日誌文件（自動生成）
```

## 開發

### 運行測試

```bash
pytest tests/ -v
```

### 查看範例

```bash
python examples/basic_usage.py
python examples/api_usage.py
```

## 常見問題

### API 金鑰設定錯誤

確認 `.env` 文件存在並包含有效的 API 金鑰。

### 模組導入錯誤

運行 `pip install -r requirements.txt` 安裝所有依賴。

### 圖片生成失敗

檢查 OpenAI API 額度，或在配置中停用圖片生成功能。

## 授權

MIT License

## 貢獻

歡迎提交 Issue 和 Pull Request！

## 支援

如有問題或建議，請在 GitHub 上提交 Issue。
