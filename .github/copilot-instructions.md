# Roaddy - 弘爺漢堡 AI 行銷團隊系統

這是一個完整的 AI 行銷團隊系統，模擬真實行銷部門的角色分工與協作流程。系統採用角色導向架構，每個角色配備專業工作流程與 AI 提示框架。

## 核心架構

### 角色系統設計模式
所有助手繼承 `BaseAssistant` 抽象類別，必須實現：
- `get_welcome_message()` - 顯示角色介紹與功能
- `get_help_message()` - 提供詳細使用指南
- `chat(user_message)` - 處理用戶對話

**範例：** 參考 `src/assistants/manager.py` 或 `src/assistants/personnel_a.py`

### AI 框架系統
每個角色配備特定 AI 提示框架：
- **CoT (Chain of Thought)** - 鏈式思考，適合複雜決策（Manager）
- **TAG (Task-Action-Goal)** - 快速執行框架（Manager 社群內容）
- **AIDA (Attention-Interest-Desire-Action)** - 經典行銷漏斗（人員 A 活動企劃）
- **IDEA (Interest-Detail-Evidence-Action)** - 文案創作（人員 A 文案撰寫）
- **CO-STAR** - 完整專案規劃（Manager 廣告投放、人員 A IP 授權）
- **SCQA (Situation-Complication-Question-Answer)** - 情境分析（品牌故事、週會）
- **RODES (Role-Objective-Details-Engagement-Structure)** - 內容品質評估
- **RISE/ERA** - 績效評估與年度規劃

框架提示詞定義在各助手的 `_get_*_prompt()` 私有方法中。

### 工作流程系統
每個助手定義工作流程常數（如 `WORKFLOW_DAILY_PLANNING`），並透過：
- `get_workflow_prompt(workflow_type)` - 獲取框架提示詞
- `start_workflow(workflow_type, user_input)` - 啟動特定工作流程
- 快速指令（如 `/daily`, `/social`）- 在 `main.py` 中映射到工作流程

## 配置管理

### 環境變數 (.env)
- `ANTHROPIC_API_KEY` - 主要 AI 服務（必須）
- `OPENAI_API_KEY` - 備用服務（可選，用於圖片生成）
- `GOOGLE_API_KEY` / `GOOGLE_CSE_ID` - 搜尋功能（可選）

### 配置文件 (config/config.yaml)
使用 `ConfigLoader` 類別載入，支援點號分隔的多層級鍵：
```python
from utils.config_loader import config
model = config.get("assistants.manager.model")
assistant_config = config.get_assistant_config("manager")
```

每個助手配置包含：`model`, `temperature`, `max_tokens`

## 開發工作流程

### 新增助手的步驟
1. 在 `src/assistants/` 建立新檔案（如 `new_assistant.py` 或 `personnel_template.py`）
2. 繼承 `BaseAssistant`，定義 `system_prompt` 與工作流程常數
3. 實現 `get_welcome_message()` 和 `get_help_message()`
4. 定義 `_get_*_prompt()` 方法提供框架提示詞
5. 在 `config/config.yaml` 新增助手配置區塊
6. 在 `src/assistants/__init__.py` 導出助手類別
7. 在 `src/main.py` 的 `ASSISTANTS` 字典中註冊
8. 若有快速指令，在 `chat_with_assistant()` 中新增命令處理邏輯

### 啟動與測試
```bash
# 開發環境快速啟動
python src/main.py -a 1  # 直接啟動 Manager (數字對應選單)

# 互動式選單
python src/main.py

# 使用啟動腳本（會自動建立虛擬環境）
./run.sh  # Linux/Mac
run.bat   # Windows
```

### 對話歷史與匯出
- 對話歷史自動儲存至 `conversations/{assistant_type}_history.txt`
- 使用 `/export` 匯出 JSON 和 Markdown 格式
- `BaseAssistant.export_conversation(format)` 處理匯出邏輯

## 品牌特定規範

### 弘爺漢堡品牌調性
所有文案與決策建議必須符合：
- **定位**：現做現煎、台式口味、平價美味
- **個性**：親切、有溫度、接地氣
- **風格**：輕鬆、有梗、貼近生活
- **避免**：過度正式、老派用語、浮誇不實

這些原則硬編碼在各助手的 `system_prompt` 中。

## API 客戶端架構

### 統一介面
`OpenAIClient` 和 `AnthropicClient` 提供一致的 `chat()` 介面：
- **Anthropic**：`messages` + `system` 參數分離
- **OpenAI**：`system` 作為第一條訊息插入

`BaseAssistant.chat()` 會根據 `use_anthropic` 旗標自動處理差異。

### 日誌記錄
所有 API 呼叫透過 `src/utils/logger.py` 記錄，使用標準 Python logging。

## UI/UX 慣例

### Rich 元件使用
- `Panel` + `Markdown` - 顯示助手訊息與說明
- `PromptSession` + `FileHistory` - 提供歷史記錄的輸入體驗
- `console.status()` - 顯示「思考中...」載入狀態

### 命令系統
標準命令（所有助手通用）：
- `/help` - 顯示助手幫助
- `/clear` - 清空對話歷史
- `/export` - 匯出對話記錄
- `/quit` - 返回主選單

角色特定命令（如 Manager 的 `/workflows`, `/daily`）：
- 在 `chat_with_assistant()` 中使用 `isinstance()` 檢查助手類型
- 呼叫 `start_workflow()` 或自定義方法處理

## 常見陷阱

1. **新增助手忘記註冊**：必須同時更新 `__init__.py`, `main.py`, 和 `config.yaml`
2. **工作流程提示詞格式不一致**：參考現有 `_get_*_prompt()` 方法的結構與標記風格
3. **中英文混用**：UI 使用繁體中文，程式碼註解可中英文，但變數/函數名稱使用英文
4. **API 金鑰檢查**：客戶端初始化時會立即驗證金鑰，避免執行到一半才失敗

## 錯誤處理模式

### API 客戶端層
所有 API 客戶端（`OpenAIClient`, `AnthropicClient`）遵循統一模式：
```python
try:
    response = self.client.chat.completions.create(...)
    logger.info(f"API 回應成功，使用 tokens: {response.usage.total_tokens}")
    return content
except Exception as e:
    logger.error(f"API 請求失敗: {e}")
    raise  # 向上層拋出，由助手層處理
```

### 助手層
`BaseAssistant.chat()` 捕捉並記錄錯誤，然後重新拋出供 UI 層處理：
```python
except Exception as e:
    logger.error(f"{self.assistant_type} 聊天失敗: {e}")
    raise
```

### UI 層
`main.py` 的 `chat_with_assistant()` 顯示友善錯誤訊息：
```python
except Exception as e:
    console.print(f"\n[red]錯誤: {e}[/red]")
    logger.error(f"對話錯誤: {e}")
```

**新增錯誤處理時**：遵循此三層模式，確保錯誤被記錄但不中斷用戶體驗。

## API 速率限制與重試

### 當前實作
- **超時設定**：`config.yaml` 中 `api.timeout: 30` 秒（僅用於 Google Search API）
- **重試機制**：配置中定義 `max_retries: 3` 和 `retry_delay: 1`，但**尚未實作**
- **速率限制**：依賴 SDK 內建處理（Anthropic/OpenAI SDK）

### 改進建議
若遇到速率限制問題，在 API 客戶端中加入重試邏輯：
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
def chat(self, messages, ...):
    # API 呼叫
```

並在 `requirements.txt` 新增 `tenacity>=8.0.0`。

## 測試策略

### 當前測試覆蓋
`tests/test_assistants.py` 提供基礎架構測試：
- ✅ 助手初始化
- ✅ 訊息歷史管理（add/clear/get）
- ✅ 對話匯出（JSON/Markdown）
- ✅ 歡迎與幫助訊息

### 測試缺口
❌ 未測試：
- API 實際呼叫（需模擬）
- 工作流程邏輯
- 命令處理
- 配置載入錯誤
- 錯誤恢復機制

### 測試指南

**1. 單元測試（模擬 API）**
```python
from unittest.mock import Mock, patch

def test_manager_daily_workflow(monkeypatch):
    # 模擬 Anthropic 客戶端
    mock_response = "每日工作規劃結果..."
    monkeypatch.setattr("anthropic.Anthropic.messages.create", 
                        Mock(return_value=mock_response))
    
    assistant = ManagerAssistant()
    result = assistant.start_workflow("daily_planning", "今日任務...")
    assert "優先級" in result
```

**2. 整合測試（真實 API，需金鑰）**
```python
@pytest.mark.integration  # 標記為整合測試
def test_real_api_call():
    assistant = ManagerAssistant()
    response = assistant.chat("測試訊息")
    assert response != ""
```

執行：`pytest tests/ -m "not integration"` （跳過整合測試）

**3. 手動測試**
```bash
# 快速驗證特定助手
python src/main.py -a 1

# 測試特定工作流程（在對話中輸入）
/daily
/social
/workflows
```

**4. 新增測試檔案結構**
```
tests/
├── test_assistants.py          # 基礎測試（已存在）
├── test_workflows.py           # 工作流程邏輯測試（建議新增）
├── test_api_clients.py         # API 客戶端測試（建議新增）
├── test_config.py              # 配置載入測試（建議新增）
├── conftest.py                 # pytest 固件（建議新增）
└── fixtures/                   # 測試數據（建議新增）
    ├── mock_responses.json
    └── sample_configs.yaml
```

**5. 測試覆蓋率檢查**
```bash
pip install pytest-cov
pytest tests/ --cov=src --cov-report=html
```

## 部署流程

### 開發環境
使用啟動腳本（自動建立虛擬環境）：
```bash
./run.sh           # Linux/Mac
run.bat            # Windows
```

### 生產環境部署

**選項 1：Docker 部署（推薦）**

創建 `Dockerfile`：
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案檔案
COPY src/ ./src/
COPY config/ ./config/

# 創建必要目錄
RUN mkdir -p logs conversations

# 設定環境變數
ENV PYTHONUNBUFFERED=1

# 啟動指令（需傳入助手編號）
ENTRYPOINT ["python", "src/main.py"]
CMD ["-a", "1"]
```

創建 `docker-compose.yml`：
```yaml
version: '3.8'

services:
  roaddy-manager:
    build: .
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./conversations:/app/conversations
      - ./logs:/app/logs
    command: ["-a", "1"]  # Manager 助手

  roaddy-personnel-a:
    build: .
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    volumes:
      - ./conversations:/app/conversations
      - ./logs:/app/logs
    command: ["-a", "2"]  # 人員 A
```

啟動：`docker-compose up -d roaddy-manager`

**選項 2：傳統部署**
```bash
# 1. 複製專案到伺服器
git clone https://github.com/your-org/roaddy.git
cd roaddy

# 2. 建立虛擬環境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 設定環境變數
cp .env.example .env
nano .env  # 填入 API 金鑰

# 5. 啟動服務（使用 systemd）
sudo nano /etc/systemd/system/roaddy-manager.service
```

Systemd 服務檔範例：
```ini
[Unit]
Description=Roaddy AI Marketing Manager
After=network.target

[Service]
Type=simple
User=roaddy
WorkingDirectory=/opt/roaddy
Environment="PATH=/opt/roaddy/venv/bin"
ExecStart=/opt/roaddy/venv/bin/python src/main.py -a 1
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

啟動：`sudo systemctl start roaddy-manager`

**選項 3：CI/CD 自動化**

創建 `.github/workflows/deploy.yml`：
```yaml
name: Deploy Roaddy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run tests
        run: pytest tests/ -m "not integration"
      
      - name: Build Docker image
        run: docker build -t roaddy:latest .
      
      - name: Deploy to server
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          # 部署腳本（SSH 到伺服器執行更新）
          echo "部署邏輯"
```

### 環境變數管理
- **開發**：使用 `.env` 檔案
- **生產**：使用環境變數或 Secret 管理工具（AWS Secrets Manager, Vault）
- **Docker**：透過 `docker-compose.yml` 或 Kubernetes ConfigMap/Secret

## 未來擴充建議

### 1. 多模型支援架構
目前架構已為多模型準備好基礎，可輕鬆擴充：

**新增 Gemini 支援**：
```python
# src/api/gemini_client.py
import os
import google.generativeai as genai
from src.utils.logger import logger

class GeminiClient:
    def __init__(self, api_key=None, model="gemini-pro"):
        genai.configure(api_key=api_key or os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel(model)
    
    def _convert_messages(self, messages) -> str:
        """
        將 OpenAI/Anthropic 訊息格式（list of dicts with 'role' and 'content'）轉換為 Gemini 所需格式。
        這裡僅作為範例，實際可根據 Gemini API 需求調整。
        """
        # 將每則訊息以 "{role}: {content}" 格式串接，保留角色資訊
        return "\n".join([f"{msg.get('role', 'user')}: {msg.get('content', '')}" for msg in messages])
    def chat(self, messages, **kwargs) -> str:
        """
        Generate a response from the Gemini model based on the provided messages.

        Args:
            messages (list): A list of message dictionaries, each containing 'role' and 'content' keys.
            **kwargs: Additional keyword arguments for future extensibility (currently unused).

        Returns:
            str: The generated response text from the Gemini model.
        
        Raises:
            Exception: If message conversion or API call fails.
        """
        try:
            # 轉換訊息格式
            prompt = self._convert_messages(messages)
            response = self.model.generate_content(prompt)
            if not response or not getattr(response, "text", None):
                raise ValueError("Empty response from Gemini API")
            logger.info(f"Gemini API 回應成功")
            return response.text
        except Exception as e:
            logger.error(f"Gemini API 請求失敗: {type(e).__name__} - {e}")
            raise  # 向上層拋出，由助手層處理
```

在 `BaseAssistant.__init__()` 新增模型選擇邏輯。

### 2. 向量資料庫整合
支援 RAG（檢索增強生成）用於品牌知識庫：

**建議整合**：
- **Chroma**：輕量級，適合單機部署
- **Pinecone**：雲端服務，適合生產環境
- **Weaviate**：開源，支援混合搜尋

**實作位置**：新增 `src/utils/knowledge_base.py`

### 3. 網頁介面
目前為 CLI 介面，可擴充為 Web 應用：

**選項 A：Streamlit（快速原型）**
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

**選項 B：FastAPI + React（生產級）**
- 後端：FastAPI WebSocket 支援串流回應
- 前端：React + Tailwind CSS
- 認證：JWT + OAuth2

### 4. 多語言支援
在 `config.yaml` 新增語言設定，調整系統提示詞：
```yaml
language: "zh-TW"  # zh-TW, en-US, ja-JP
```

### 5. 外部 API 整合建議
- **社群平台**：Facebook Graph API、Instagram API（自動發文）
- **分析工具**：Google Analytics Data API（數據追蹤）
- **設計工具**：Canva API（自動生成視覺素材）
- **電商平台**：Shopify API（商品資料同步）

**實作模式**：參考現有 `src/api/google_search.py`，每個 API 獨立一個客戶端類別。

### 6. 助手協作機制
實作助手間對話：
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
    def _synthesize(self, results) -> str:
    
    def _synthesize(self, results):
        """
        將多個助手的回應整合成一個有條理的輸出。
        例如：彙總、排序、去重、或以特定格式組合。
        實際實作可依需求調整。
        # 確保所有回應都是字串，避免 join 時出錯
        return "\n\n".join(str(r) if r is not None else "" for r in results)
        # TODO: 實作回應整合邏輯
        return "\n\n".join(results)
```

### 7. 效能優化
- **串流回應**：使用 Anthropic/OpenAI 的 streaming API
- **快取機制**：相似問題的回應快取（使用 Redis）
- **非同步處理**：使用 `asyncio` 處理並發請求
