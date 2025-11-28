# 🚀 快速開始指南

## 📦 方式 1：使用執行檔（推薦給非技術人員）

### 步驟 1：打包成執行檔

**Windows：**
```bash
build.bat
```

**Linux/Mac：**
```bash
chmod +x build.sh
./build.sh
```

等待 2-3 分鐘打包完成。

### 步驟 2：設定 API Key

1. 進入 `dist/portable/` 資料夾
2. 複製 `.env.example` 為 `.env`
3. 用記事本打開 `.env`，填入您的 Anthropic API Key：
   ```env
   ANTHROPIC_API_KEY=sk-ant-api03-你的金鑰
   ```

### 步驟 3：執行程式

- **Windows**: 雙擊 `弘爺漢堡AI行銷助手.exe`
- **Mac**: 雙擊 `弘爺漢堡AI行銷助手`
- **Linux**: 在終端機執行 `./弘爺漢堡AI行銷助手`

---

## 💻 方式 2：命令列執行（推薦給開發者）

### 步驟 1：設定環境

```bash
# 複製環境變數範例
cp .env.example .env

# 編輯 .env 填入 API Key
nano .env  # 或使用任何文字編輯器
```

### 步驟 2：執行程式

**使用啟動腳本（自動安裝依賴）：**
```bash
./run.sh      # Linux/Mac
run.bat       # Windows
```

**或手動執行：**
```bash
# 設定路徑
export PYTHONPATH=/workspaces/roaddy:$PYTHONPATH

# 安裝依賴
pip install -r requirements.txt

# 執行程式
python src/main.py
```

---

## 🎯 使用程式

啟動後會看到選單：

```
╭─── 功能選單 ────╮
│ [1] Manager (主管)
│ [2] 人員 A (行銷企劃)
│ [3] 人員 B (數位行銷)
│ [4] 人員 C (視覺設計)
│ [5] 人員 D (美編專員)
│ [6] 人員 E (團購PM)
│ [0] 退出系統
╰─────────────────╯
```

### 快速指令

選擇助手後可使用快速指令：

**Manager 主管：**
- `/daily` - 每日工作規劃
- `/social` - 社群內容產出
- `/ad` - 廣告投放決策
- `/workflows` - 查看所有工作流程

**或直接對話：**
```
您: 幫我規劃今天的工作
您: 寫一篇母親節活動的社群貼文
您: 分析要不要推出新口味漢堡
```

---

## ❓ 常見問題

### Q: 如何取得 API Key？

1. 前往 [Anthropic Console](https://console.anthropic.com/)
2. 註冊並登入
3. 進入 **API Keys** 創建金鑰
4. 複製金鑰（格式：`sk-ant-api03-xxxxx...`）

### Q: API Key 錯誤怎麼辦？

**錯誤訊息：** `401 - authentication_error`

**解決方法：**
1. 檢查 `.env` 檔案中的 API Key 是否正確
2. 確認金鑰沒有過期
3. 重新啟動程式

### Q: 模型不存在錯誤？

**錯誤訊息：** `404 - not_found_error: model`

**解決方法：**
目前系統使用 `claude-3-haiku-20240307` 模型。如果要使用其他模型，編輯 `config/config.yaml`：

```yaml
assistants:
  manager:
    model: "claude-3-haiku-20240307"  # 或其他可用模型
```

### Q: 執行檔無法開啟？

**Windows：**
- 右鍵點擊執行檔 → 內容 → 解除封鎖
- 加入防毒軟體信任清單

**Mac：**
```bash
chmod +x 弘爺漢堡AI行銷助手
xattr -d com.apple.quarantine 弘爺漢堡AI行銷助手
```

---

## 📚 更多資訊

- **完整使用說明**：[docs/USAGE.md](docs/USAGE.md)
- **打包詳細指南**：[docs/BUILD.md](docs/BUILD.md)
- **API 文件**：[docs/API.md](docs/API.md)
- **開發指南**：[.github/copilot-instructions.md](.github/copilot-instructions.md)

---

## 🆘 需要協助？

如有問題，請檢查：
1. Python 版本 >= 3.8
2. API Key 是否正確設定
3. 網路連線是否正常

或提交 Issue 到 GitHub！
