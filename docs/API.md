# API 文檔

## 概述

本系統提供三類 API 客戶端：
1. OpenAI API 客戶端（GPT-4o、DALL-E 3）
2. Anthropic API 客戶端（Claude 3.5 Sonnet）
3. Google Search API 客戶端

## OpenAI API 客戶端

### 初始化

```python
from api import OpenAIClient

client = OpenAIClient(
    api_key="your-api-key",  # 可選，默認從環境變數讀取
    model="gpt-4o"           # 默認模型
)
```

### 聊天

```python
messages = [
    {"role": "user", "content": "你好"}
]

response = client.chat(
    messages=messages,
    temperature=0.7,    # 可選，默認 0.7
    max_tokens=4096     # 可選，默認 4096
)

print(response)
```

### 圖片生成（DALL-E 3）

```python
image_urls = client.generate_image(
    prompt="A modern office",
    size="1024x1024",      # 可選：1024x1024, 1024x1792, 1792x1024
    quality="standard",    # 可選：standard, hd
    n=1                    # 生成數量
)

print(image_urls[0])
```

## Anthropic API 客戶端

### 初始化

```python
from api import AnthropicClient

client = AnthropicClient(
    api_key="your-api-key",                    # 可選
    model="claude-3-5-sonnet-20241022"        # 默認模型
)
```

### 聊天

```python
messages = [
    {"role": "user", "content": "你好"}
]

response = client.chat(
    messages=messages,
    system="你是一位專業的助手",  # 可選，系統提示詞
    temperature=0.7,              # 可選
    max_tokens=4096               # 可選
)

print(response)
```

## Google Search API 客戶端

### 初始化

```python
from api import GoogleSearchClient

client = GoogleSearchClient(
    api_key="your-google-api-key",
    search_engine_id="your-search-engine-id"
)
```

### 網頁搜尋

```python
results = client.search(
    query="AI marketing",
    num=10,        # 結果數量
    start=1        # 起始位置
)

for result in results:
    print(result['title'])
    print(result['link'])
    print(result['snippet'])
```

### 新聞搜尋

```python
news = client.search_news(
    query="AI marketing trends",
    num=5
)
```

### 圖片搜尋

```python
images = client.search_images(
    query="marketing dashboard",
    num=10
)

for img in images:
    print(img['image_url'])
```

## 助手 API

### 基礎助手類別

所有助手都繼承自 `BaseAssistant`：

```python
from assistants import ContentMarketingAssistant

# 創建助手
assistant = ContentMarketingAssistant()

# 發送訊息
response = assistant.chat("我想優化 SEO")

# 獲取對話歷史
history = assistant.get_history()

# 清空歷史
assistant.clear_history()

# 匯出對話
json_data = assistant.export_conversation("json")
md_content = assistant.export_conversation("markdown")
```

### 可用助手

```python
from assistants import (
    ContentMarketingAssistant,   # 內容行銷助手
    CopywritingAssistant,        # 文案撰寫助手
    SocialMediaAssistant,        # 社群行銷助手
    BrandStrategyAssistant,      # 品牌策略顧問
    CreativeMarketingAssistant,  # 創意行銷助手
    EcommerceAssistant,          # 電商行銷助手
    AdManagerAssistant,          # 廣告投手
)
```

### 助手方法

所有助手都支持以下方法：

#### `chat(user_message: str) -> str`

發送訊息並獲取回應。

**參數：**
- `user_message`: 用戶訊息

**返回：**
- 助手回應字符串

#### `get_welcome_message() -> str`

獲取歡迎訊息。

**返回：**
- 歡迎訊息字符串

#### `get_help_message() -> str`

獲取幫助訊息。

**返回：**
- 幫助訊息字符串

#### `add_message(role: str, content: str) -> None`

手動添加訊息到對話歷史。

**參數：**
- `role`: "user" 或 "assistant"
- `content`: 訊息內容

#### `clear_history() -> None`

清空對話歷史。

#### `get_history() -> List[Dict[str, str]]`

獲取對話歷史。

**返回：**
- 對話歷史列表

#### `export_conversation(format: str) -> Any`

匯出對話記錄。

**參數：**
- `format`: "json" 或 "markdown"

**返回：**
- JSON 字典或 Markdown 字符串

## 配置 API

### 讀取配置

```python
from utils import config

# 獲取配置值
model = config.get("assistants.content_marketing.model")

# 獲取助手配置
assistant_config = config.get_assistant_config("content_marketing")

# 獲取 API 金鑰
openai_key = config.get_api_key("OPENAI")
```

### 配置載入器

```python
from utils import ConfigLoader

# 創建自訂配置載入器
custom_config = ConfigLoader(config_path="/path/to/config.yaml")

# 使用自訂配置
value = custom_config.get("some.key", default="default_value")
```

## 日誌 API

```python
from utils import logger, setup_logger

# 使用默認日誌記錄器
logger.info("訊息")
logger.error("錯誤")
logger.warning("警告")

# 創建自訂日誌記錄器
custom_logger = setup_logger(
    name="my_logger",
    level="DEBUG",
    log_file="logs/custom.log"
)

custom_logger.debug("除錯訊息")
```

## 提示詞 API

```python
from utils import get_prompt

# 獲取助手提示詞
prompt = get_prompt("content_marketing")
```

## 錯誤處理

所有 API 調用都可能拋出異常，建議使用 try-except：

```python
try:
    response = assistant.chat("你好")
except ValueError as e:
    print(f"配置錯誤: {e}")
except Exception as e:
    print(f"其他錯誤: {e}")
```

## 速率限制

請注意各 API 的速率限制：

- **OpenAI**: 根據您的訂閱計劃
- **Anthropic**: 根據您的訂閱計劃
- **Google Search**: 免費配額有限

建議實施適當的錯誤處理和重試機制。
