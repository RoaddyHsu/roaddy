#!/bin/bash

# 確保已登入 GitHub CLI
gh auth status || gh auth login

REPO="RoaddyHsu/roaddy"

echo "🚀 開始建立 12 個 Issues..."

# Issue 1
gh issue create --repo $REPO \
  --title "🔧 將預設分支改名為 main" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
將目前的預設分支改名為 `main`

## 📝 實作步驟
1. 建立 main 分支：`git checkout -b main && git push origin main`
2. 在 GitHub Settings 設定預設分支為 main
3. 更新所有 workflows 的分支引用
4. 刪除舊分支（可選）

## ✅ 檢查清單
- [ ] 建立 main 分支
- [ ] 設定為預設分支
- [ ] 更新 GitHub Actions
- [ ] 測試 CI/CD

## 📚 參考
- [GitHub 官方文檔](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository)
EOF

echo "✅ Issue 1 已建立"

# Issue 2
gh issue create --repo $REPO \
  --title "📊 新增單元測試覆蓋率報告" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
建立自動化測試與覆蓋率報告

## 📝 實作步驟

### 1. 安裝依賴
```txt
pytest>=7.4.0
pytest-cov>=4.1.0
```

### 2. 建立測試檔案
```
tests/
├── test_assistants.py          # 基礎測試（已存在）
├── test_workflows.py           # 工作流程邏輯測試
├── test_api_clients.py         # API 客戶端測試
├── test_config.py              # 配置載入測試
├── conftest.py                 # pytest 固件
└── fixtures/                   # 測試數據
    ├── mock_responses.json
    └── sample_configs.yaml
```

### 3. 執行覆蓋率測試
```bash
pytest tests/ --cov=src --cov-report=html --cov-report=term
```

### 4. 新增 GitHub Actions
在 `.github/workflows/test.yml` 中加入覆蓋率報告上傳

## ✅ 檢查清單
- [ ] 安裝 pytest-cov
- [ ] 建立測試檔案結構
- [ ] 設定覆蓋率門檻（建議 80%）
- [ ] 整合 GitHub Actions
- [ ] 新增覆蓋率徽章到 README

## 📚 參考
- [pytest-cov 文檔](https://pytest-cov.readthedocs.io/)
EOF

echo "✅ Issue 2 已建立"

# Issue 3
gh issue create --repo $REPO \
  --title "🔒 新增 API 重試與速率限制機制" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
實作 API 客戶端的重試邏輯與速率限制處理

## 📝 實作步驟

### 1. 安裝 tenacity
```bash
pip install tenacity>=8.0.0
```

### 2. 在 API 客戶端加入重試邏輯
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
def chat(self, messages, ...):
    # API 呼叫
```

### 3. 處理速率限制錯誤
- Anthropic API: 429 錯誤
- OpenAI API: RateLimitError

## ✅ 檢查清單
- [ ] 安裝 tenacity 套件
- [ ] 更新 OpenAIClient
- [ ] 更新 AnthropicClient
- [ ] 新增重試日誌記錄
- [ ] 測試重試機制

## 📚 參考
- [tenacity 文檔](https://tenacity.readthedocs.io/)
EOF

echo "✅ Issue 3 已建立"

# Issue 4
gh issue create --repo $REPO \
  --title "🐳 新增 Docker 支援" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
建立 Docker 容器化部署方案

## 📝 實作步驟

### 1. 建立 Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY config/ ./config/
RUN mkdir -p logs conversations
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python", "src/main.py"]
CMD ["-a", "1"]
```

### 2. 建立 docker-compose.yml
支援多個助手服務同時運行

### 3. 建立 .dockerignore
排除不必要的檔案

## ✅ 檢查清單
- [ ] 建立 Dockerfile
- [ ] 建立 docker-compose.yml
- [ ] 建立 .dockerignore
- [ ] 測試 Docker build
- [ ] 更新文檔說明

## 📚 參考
- [Docker 官方文檔](https://docs.docker.com/)
EOF

echo "✅ Issue 4 已建立"

# Issue 5
gh issue create --repo $REPO \
  --title "📝 新增工作流程測試" \
  --label "enhancement,testing" \
  --body-file - <<'EOF'
## 📋 目標
為各助手的工作流程建立完整測試

## 📝 實作步驟

### 1. 建立 tests/test_workflows.py
測試各助手的工作流程：
- Manager: daily_planning, social_content, ad_campaign 等
- 人員 A: activity_planning, copywriting 等
- 人員 B-E: 各自的工作流程

### 2. 使用 Mock 模擬 API 回應
```python
from unittest.mock import Mock, patch

def test_manager_daily_workflow(monkeypatch):
    mock_response = "每日工作規劃結果..."
    monkeypatch.setattr("anthropic.Anthropic.messages.create", 
                        Mock(return_value=mock_response))
    
    assistant = ManagerAssistant()
    result = assistant.start_workflow("daily_planning", "今日任務...")
    assert "優先級" in result
```

### 3. 測試快速指令
確保 `/daily`, `/social` 等指令正確映射到工作流程

## ✅ 檢查清單
- [ ] 建立 test_workflows.py
- [ ] 測試 Manager 工作流程
- [ ] 測試所有人員 A-E 工作流程
- [ ] 測試快速指令映射
- [ ] 測試錯誤處理

## 📚 參考
- [pytest 文檔](https://docs.pytest.org/)
EOF

echo "✅ Issue 5 已建立"

# Issue 6
gh issue create --repo $REPO \
  --title "🌐 新增多語言支援框架" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
建立多語言支援架構（i18n）

## 📝 實作步驟

### 1. 在 config.yaml 新增語言設定
```yaml
language: "zh-TW"  # zh-TW, en-US, ja-JP
```

### 2. 建立語言檔案結構
```
config/
└── locales/
    ├── zh-TW.yaml
    ├── en-US.yaml
    └── ja-JP.yaml
```

### 3. 調整系統提示詞
根據語言設定動態載入對應的提示詞

### 4. UI 訊息國際化
更新 main.py 中的所有 UI 字串

## ✅ 檢查清單
- [ ] 建立語言配置結構
- [ ] 建立繁體中文語言檔
- [ ] 建立英文語言檔
- [ ] 更新系統提示詞
- [ ] 測試語言切換

## 📚 參考
- [i18n 最佳實踐](https://phrase.com/blog/posts/i18n-best-practices/)
EOF

echo "✅ Issue 6 已建立"

# Issue 7
gh issue create --repo $REPO \
  --title "🔍 新增向量資料庫整合 (RAG)" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
整合向量資料庫支援 RAG（檢索增強生成）

## 📝 實作步驟

### 1. 選擇向量資料庫
建議選項：
- **Chroma**：輕量級，適合單機部署
- **Pinecone**：雲端服務，適合生產環境
- **Weaviate**：開源，支援混合搜尋

### 2. 建立知識庫管理模組
```python
# src/utils/knowledge_base.py
class KnowledgeBase:
    def __init__(self):
        # 初始化向量資料庫
        pass
    
    def add_document(self, text, metadata):
        # 新增文檔
        pass
    
    def search(self, query, top_k=5):
        # 檢索相關文檔
        pass
```

### 3. 整合到助手系統
在回答問題前先檢索品牌知識庫

## ✅ 檢查清單
- [ ] 選擇並安裝向量資料庫
- [ ] 建立 knowledge_base.py
- [ ] 整合到 BaseAssistant
- [ ] 匯入品牌知識文檔
- [ ] 測試 RAG 功能

## 📚 參考
- [Chroma 文檔](https://docs.trychroma.com/)
- [LangChain RAG](https://python.langchain.com/docs/use_cases/question_answering/)
EOF

echo "✅ Issue 7 已建立"

# Issue 8
gh issue create --repo $REPO \
  --title "🚀 新增 CI/CD 工作流程" \
  --label "enhancement,ci/cd" \
  --body-file - <<'EOF'
## 📋 目標
建立完整的 CI/CD 自動化流程

## 📝 實作步驟

### 1. 建立測試工作流程
`.github/workflows/test.yml`
- 在 PR 時自動執行測試
- 檢查程式碼覆蓋率
- 執行 linting

### 2. 建立發布工作流程
`.github/workflows/release.yml`
- 自動建立可執行檔
- 生成 release notes
- 發布到 GitHub Releases

### 3. 建立部署工作流程
`.github/workflows/deploy.yml`
- 自動部署到生產環境
- 支援 Docker 部署

## ✅ 檢查清單
- [ ] 建立 test.yml
- [ ] 建立 release.yml
- [ ] 建立 deploy.yml
- [ ] 設定 GitHub Secrets
- [ ] 測試 CI/CD 流程

## 📚 參考
- [GitHub Actions 文檔](https://docs.github.com/en/actions)
EOF

echo "✅ Issue 8 已建立"

# Issue 9
gh issue create --repo $REPO \
  --title "💬 新增串流回應支援" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
實作 AI 回應的串流輸出，提升用戶體驗

## 📝 實作步驟

### 1. 更新 API 客戶端
使用 Anthropic/OpenAI 的 streaming API：
```python
def chat_stream(self, messages, **kwargs):
    with self.client.messages.stream(...) as stream:
        for text in stream.text_stream:
            yield text
```

### 2. 更新 UI 顯示
使用 Rich 的 Live 元件即時顯示：
```python
from rich.live import Live

with Live(console=console, refresh_per_second=4) as live:
    for chunk in assistant.chat_stream(message):
        live.update(chunk)
```

### 3. 測試串流功能
確保長回應能即時顯示

## ✅ 檢查清單
- [ ] 更新 AnthropicClient
- [ ] 更新 OpenAIClient
- [ ] 更新 BaseAssistant
- [ ] 更新 UI 顯示邏輯
- [ ] 測試串流回應

## 📚 參考
- [Anthropic Streaming](https://docs.anthropic.com/claude/reference/messages-streaming)
EOF

echo "✅ Issue 9 已建立"

# Issue 10
gh issue create --repo $REPO \
  --title "🌐 新增 Web 介面" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
建立 Web 應用介面，提供瀏覽器存取

## 📝 實作步驟

### 選項 A：Streamlit（快速原型）
```python
# app.py
import streamlit as st
from src.assistants import ManagerAssistant

st.title("弘爺漢堡 AI 行銷助手")
assistant = ManagerAssistant()

if prompt := st.chat_input("輸入訊息"):
    response = assistant.chat(prompt)
    st.markdown(response)
```

### 選項 B：FastAPI + React（生產級）
- 後端：FastAPI WebSocket 支援串流回應
- 前端：React + Tailwind CSS
- 認證：JWT + OAuth2

## ✅ 檢查清單
- [ ] 選擇 Web 框架
- [ ] 建立前端介面
- [ ] 建立後端 API
- [ ] 實作使用者認證
- [ ] 部署到雲端

## 📚 參考
- [Streamlit 文檔](https://docs.streamlit.io/)
- [FastAPI 文檔](https://fastapi.tiangolo.com/)
EOF

echo "✅ Issue 10 已建立"

# Issue 11
gh issue create --repo $REPO \
  --title "🔌 新增外部 API 整合" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
整合常用的外部 API 服務

## 📝 實作步驟

### 1. 社群平台 API
- Facebook Graph API（自動發文）
- Instagram API（內容發布）
- Twitter/X API（推文發布）

### 2. 分析工具 API
- Google Analytics Data API（數據追蹤）
- Meta Business Suite API（廣告數據）

### 3. 設計工具 API
- Canva API（自動生成視覺素材）
- Figma API（設計檔案管理）

### 4. 電商平台 API
- Shopify API（商品資料同步）
- WooCommerce API（訂單管理）

## 實作模式
參考現有 `src/api/google_search.py`，每個 API 獨立一個客戶端類別

## ✅ 檢查清單
- [ ] 選擇要整合的 API
- [ ] 建立 API 客戶端類別
- [ ] 整合到相關助手
- [ ] 撰寫使用文檔
- [ ] 測試 API 整合

## 📚 參考
- [Meta for Developers](https://developers.facebook.com/)
- [Google Analytics API](https://developers.google.com/analytics)
EOF

echo "✅ Issue 11 已建立"

# Issue 12
gh issue create --repo $REPO \
  --title "👥 新增助手協作機制" \
  --label "enhancement" \
  --body-file - <<'EOF'
## 📋 目標
實作多個助手協同工作的機制

## 📝 實作步驟

### 1. 建立協作管理器
```python
# src/utils/collaboration.py
class AssistantCollaboration:
    def __init__(self):
        self.assistants = {}
    
    def collaborate(self, task, assistants_list):
        """多個助手協作完成任務"""
        results = []
        for assistant_type in assistants_list:
            assistant = self.assistants[assistant_type]
            result = assistant.chat(task)
            results.append(result)
        return self._synthesize(results)
    
    def _synthesize(self, results):
        """整合多個助手的回應"""
        # TODO: 實作回應整合邏輯
        pass
```

### 2. 使用案例
- Manager + 人員 A：活動策劃與執行
- 人員 A + 人員 C：文案與視覺整合
- 人員 B + 人員 D：社群內容製作

### 3. 建立協作工作流程
定義標準的協作模式與流程

## ✅ 檢查清單
- [ ] 建立 collaboration.py
- [ ] 實作協作邏輯
- [ ] 定義協作工作流程
- [ ] 整合到主程式
- [ ] 測試協作功能

## 📚 參考
- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
EOF

echo "✅ Issue 12 已建立"

echo ""
echo "🎉 所有 12 個 Issues 已成功建立！"
echo "📋 請前往 GitHub 查看：https://github.com/$REPO/issues"
