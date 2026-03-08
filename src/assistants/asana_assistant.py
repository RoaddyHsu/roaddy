"""
Asana 專案管理助手
"""

import os
from .base_assistant import BaseAssistant
from src.api.asana_client import AsanaClient
from src.utils.logger import logger
from typing import Dict, Optional


class AsanaAssistant(BaseAssistant):
    """Asana 專案管理助手 - 整合 Asana 進行任務與專案管理"""

    # 工作流程類型
    WORKFLOW_PROJECT_OVERVIEW = "project_overview"  # 專案總覽
    WORKFLOW_TASK_MANAGEMENT = "task_management"  # 任務管理
    WORKFLOW_TASK_BREAKDOWN = "task_breakdown"  # 任務拆解
    WORKFLOW_PROGRESS_REPORT = "progress_report"  # 進度報告
    WORKFLOW_SPRINT_PLANNING = "sprint_planning"  # 衝刺規劃
    WORKFLOW_TEAM_WORKLOAD = "team_workload"  # 團隊工作量

    def __init__(self):
        # 主系統提示詞
        system_prompt = """你是弘爺漢堡的 Asana 專案管理助手。

## 核心職責
- 協助使用者透過 Asana 管理專案與任務
- 提供專案進度追蹤與分析
- 協助任務拆解與分配
- 產出專案狀態報告
- 協助衝刺規劃與工作量分析

## 整合能力
- 可直接操作 Asana API（建立/更新/查詢專案與任務）
- 支援專案總覽、任務管理、進度追蹤等功能
- 可將 AI 分析結果轉化為 Asana 任務

## 工作原則
- 任務拆解要具體、可執行、可衡量
- 時程規劃要考慮資源限制與依賴關係
- 主動提醒逾期與風險任務
- 數據驅動的進度分析

## 品牌背景
- 弘爺漢堡: 台式早餐連鎖品牌
- 團隊涵蓋行銷企劃、數位行銷、視覺設計、美編、團購PM

## 可用指令
- /projects - 查看所有專案
- /tasks - 查看任務列表
- /create - 建立新任務
- /status - 專案狀態報告
- /breakdown - 任務拆解
- /sprint - 衝刺規劃
- /workload - 團隊工作量分析
- /workflows - 查看所有工作流程

根據用戶的需求，提供專業的專案管理建議，並可直接操作 Asana 執行任務。"""

        super().__init__(
            assistant_type="asana",
            system_prompt=system_prompt,
            use_anthropic=True,
        )

        # 初始化 Asana 客戶端
        self._asana_client = None
        self._workspace_gid = None

    @property
    def asana(self) -> Optional[AsanaClient]:
        """延遲初始化 Asana 客戶端"""
        if self._asana_client is None:
            try:
                self._asana_client = AsanaClient()
                logger.info("Asana 客戶端連線成功")
            except ValueError:
                logger.warning("Asana 未設定 Access Token，僅提供建議模式")
                return None
        return self._asana_client

    @property
    def workspace_gid(self) -> Optional[str]:
        """取得預設工作區 GID"""
        if self._workspace_gid is None:
            gid = os.getenv("ASANA_WORKSPACE_GID")
            if gid:
                self._workspace_gid = gid
            elif self.asana:
                try:
                    workspaces = self.asana.get_workspaces()
                    if workspaces:
                        self._workspace_gid = workspaces[0]["gid"]
                except Exception:
                    pass
        return self._workspace_gid

    def get_welcome_message(self) -> str:
        """獲取歡迎訊息"""
        # 檢查 Asana 連線狀態
        connection_status = ""
        if self.asana:
            try:
                me = self.asana.get_me()
                user_name = me.get("name", "使用者")
                connection_status = f"\n**Asana 帳號：** {user_name} (已連線)"
            except Exception:
                connection_status = "\n**Asana 狀態：** 連線失敗，請確認 Access Token"
        else:
            connection_status = "\n**Asana 狀態：** 未設定 Token，僅提供建議模式"

        return f"""
# 歡迎使用 Asana 專案管理助手

我是弘爺漢堡的 Asana 專案管理助手！可以幫您管理專案、追蹤任務、分析進度。
{connection_status}

## 我能協助您

### 專案管理
**1. 專案總覽** - 查看所有專案與狀態
**2. 任務管理** - 建立、更新、查詢任務
**3. 任務拆解** - 將大目標拆解為可執行任務

### 進度追蹤
**4. 狀態報告** - 產出專案進度報告
**5. 衝刺規劃** - 規劃週期性工作計畫
**6. 工作量分析** - 團隊負載分析

## 快速指令

**專案操作：**
- `/projects` - 查看所有專案
- `/tasks` - 查看任務列表
- `/create` - 建立新任務

**分析報告：**
- `/status` - 專案狀態報告
- `/breakdown` - 任務拆解
- `/sprint` - 衝刺規劃
- `/workload` - 團隊工作量

**查看所有：**
- `/workflows` - 查看所有工作流程

或直接描述您的需求，我會提供專業建議！
"""

    def get_help_message(self) -> str:
        """獲取幫助訊息"""
        return """
# Asana 專案管理助手使用指南

## 支援的工作流程

### 1. 專案總覽
**使用時機：** 快速了解所有專案狀態
**輸入指令：** `/projects`
**功能：**
- 列出所有 Asana 專案
- 顯示專案進度概況
- 標示逾期或風險項目

---

### 2. 任務管理
**使用時機：** 查看、建立或更新任務
**輸入指令：** `/tasks` 或 `/create`
**功能：**
- 依專案查看任務列表
- 建立新任務（含負責人、截止日）
- 更新任務狀態
- 標記任務完成

---

### 3. 任務拆解
**使用時機：** 將大目標拆解為具體任務
**輸入指令：** `/breakdown`
**輸入資訊：**
- 目標或專案描述
- 時間範圍
- 可用資源

**輸出內容：**
- 結構化任務清單
- 時程安排建議
- 負責人建議
- 可直接匯入 Asana

---

### 4. 專案狀態報告
**使用時機：** 產出專案進度報告
**輸入指令：** `/status`
**輸出內容：**
- 整體完成率
- 各階段任務統計
- 逾期任務清單
- 風險項目提示
- 下一步建議

---

### 5. 衝刺規劃
**使用時機：** 規劃下一個工作週期
**輸入指令：** `/sprint`
**輸入資訊：**
- 衝刺期間（通常 1-2 週）
- 團隊成員
- 待辦任務池

**輸出內容：**
- 衝刺目標
- 任務分配建議
- 每日工作計畫
- 風險評估

---

### 6. 團隊工作量
**使用時機：** 了解團隊成員工作負載
**輸入指令：** `/workload`
**輸出內容：**
- 各成員任務數量
- 工作量分佈
- 瓶頸分析
- 調配建議

---

## 使用技巧

### Asana 操作指令
- `/projects` - 列出專案
- `/tasks` - 查看任務
- `/create` - 建立任務

### 自然對話
您也可以直接描述需求，例如：
- "幫我看一下本週有哪些任務要完成"
- "把這個行銷活動拆解成 Asana 任務"
- "產出本月專案進度報告"
- "建立一個新的社群行銷專案"

## 設定方式

1. 取得 Asana Personal Access Token
2. 在 `.env` 中設定 `ASANA_ACCESS_TOKEN`
3. （選填）設定 `ASANA_WORKSPACE_GID` 指定預設工作區
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
            self.WORKFLOW_PROJECT_OVERVIEW: self._get_project_overview_prompt,
            self.WORKFLOW_TASK_MANAGEMENT: self._get_task_management_prompt,
            self.WORKFLOW_TASK_BREAKDOWN: self._get_task_breakdown_prompt,
            self.WORKFLOW_PROGRESS_REPORT: self._get_progress_report_prompt,
            self.WORKFLOW_SPRINT_PLANNING: self._get_sprint_planning_prompt,
            self.WORKFLOW_TEAM_WORKLOAD: self._get_team_workload_prompt,
        }

        prompt_func = workflows.get(workflow_type)
        if prompt_func:
            return prompt_func(context or {})
        return ""

    def _get_project_overview_prompt(self, context: Dict) -> str:
        """專案總覽提示詞"""
        # 嘗試取得即時 Asana 資料
        asana_data = ""
        if self.asana and self.workspace_gid:
            try:
                projects = self.asana.get_projects(self.workspace_gid)
                if projects:
                    asana_data = "\n**目前 Asana 專案：**\n"
                    for p in projects:
                        asana_data += f"- {p.get('name', '未命名')} (GID: {p.get('gid', '')})\n"
            except Exception as e:
                asana_data = f"\n（無法取得 Asana 資料: {e}）\n"

        return f"""請提供專案總覽分析。
{asana_data}

**專案總覽架構：**

**1. 專案清單**
- 進行中的專案
- 即將開始的專案
- 已完成的專案

**2. 各專案狀態**
- 完成進度（%）
- 待辦 / 進行中 / 已完成任務數
- 逾期任務數
- 風險等級

**3. 重點關注**
- 逾期或高風險專案
- 即將到期的里程碑
- 需要決策的事項

**4. 建議行動**
- 優先處理事項
- 資源調配建議
- 風險緩解措施

請根據以上架構提供專案總覽報告。如果有 Asana 即時資料，請整合分析。"""

    def _get_task_management_prompt(self, context: Dict) -> str:
        """任務管理提示詞"""
        return """請協助管理 Asana 任務。

**任務管理功能：**

**1. 查看任務**
- 依專案查看
- 依負責人查看
- 依狀態篩選（待辦/進行中/已完成）
- 依截止日篩選

**2. 建立任務**
- 任務名稱
- 任務描述
- 負責人指派
- 截止日期
- 所屬專案

**3. 更新任務**
- 修改任務資訊
- 變更負責人
- 調整截止日
- 標記完成

請告訴我您想進行什麼任務管理操作？

【請提供以下資訊】
- 操作類型：查看 / 建立 / 更新 / 完成
- 專案名稱或 GID：
- 任務詳細資訊："""

    def _get_task_breakdown_prompt(self, context: Dict) -> str:
        """任務拆解提示詞"""
        return """請幫我將目標拆解為 Asana 任務。

**任務拆解架構：**

**1. 目標分析**
- 最終目標
- 關鍵成果 (KR)
- 時間範圍

**2. 任務拆解**
- 主任務（Phase/階段）
- 子任務（具體行動項目）
- 依賴關係
- 里程碑

**3. 資源配置**
- 負責人建議
- 時程安排
- 所需資源

**4. Asana 結構建議**
- 專案結構（清單/看板/時間軸）
- 區段（Section）規劃
- 標籤（Tag）建議
- 自訂欄位建議

請根據以下資訊進行任務拆解：

【請在此描述您的目標】
- 目標描述：
- 期望完成時間：
- 可用團隊成員：
- 預算或資源限制：
- 是否要直接建立到 Asana：

我將為您提供：
- 結構化的任務清單（主任務 + 子任務）
- 各任務的建議負責人與截止日
- 依賴關係圖
- Asana 專案結構建議
- 可選：直接在 Asana 中建立所有任務"""

    def _get_progress_report_prompt(self, context: Dict) -> str:
        """進度報告提示詞"""
        # 嘗試取得即時資料
        asana_data = ""
        if self.asana and self.workspace_gid:
            try:
                projects = self.asana.get_projects(self.workspace_gid)
                if projects:
                    asana_data = "\n**Asana 專案任務統計：**\n"
                    for p in projects[:5]:  # 最多取 5 個專案
                        try:
                            tasks = self.asana.get_tasks(project_gid=p["gid"])
                            total = len(tasks) if isinstance(tasks, list) else 0
                            asana_data += f"- {p.get('name', '未命名')}: {total} 個任務\n"
                        except Exception:
                            asana_data += f"- {p.get('name', '未命名')}: (無法取得任務)\n"
            except Exception as e:
                asana_data = f"\n（無法取得 Asana 資料: {e}）\n"

        return f"""請產出專案進度報告。
{asana_data}

**進度報告架構：**

**1. 整體摘要**
- 報告期間
- 整體完成率
- 關鍵里程碑達成

**2. 各專案進度**
- 專案名稱
- 完成率
- 本期完成任務
- 剩餘任務
- 預計完成日

**3. 風險與問題**
- 逾期任務清單
- 阻塞事項
- 風險評估

**4. 下一步計畫**
- 下期重點任務
- 資源需求
- 需要的決策或支援

**5. 團隊表現**
- 各成員完成率
- 工作負載分析

請提供專案進度報告，如果有 Asana 即時資料，請整合分析。

【請提供以下資訊（選填）】
- 報告期間：
- 關注的專案：
- 特別關注的議題："""

    def _get_sprint_planning_prompt(self, context: Dict) -> str:
        """衝刺規劃提示詞"""
        return """請幫我規劃下一個工作衝刺。

**衝刺規劃架構：**

**1. 衝刺設定**
- 衝刺期間（建議 1-2 週）
- 衝刺目標
- 團隊成員與可用時間

**2. 任務選擇**
- 從待辦清單中選擇
- 依優先級排序
- 考慮依賴關係
- 估算工作量

**3. 任務分配**
- 依成員專長分配
- 平衡工作量
- 預留緩衝時間

**4. 每日計畫**
- 每日重點任務
- 站立會議議程
- 檢查點設定

**5. 風險管理**
- 潛在風險
- 備案計畫
- 升級機制

請根據以下資訊規劃衝刺：

【請在此描述衝刺需求】
- 衝刺期間：
- 團隊成員：
- 待辦任務清單：
- 本期目標：
- 特殊考量：

我將為您提供：
- 衝刺目標與承諾
- 任務分配表
- 每日工作計畫
- 風險評估與備案
- 可選：在 Asana 中建立衝刺看板"""

    def _get_team_workload_prompt(self, context: Dict) -> str:
        """團隊工作量提示詞"""
        return """請分析團隊工作量。

**工作量分析架構：**

**1. 成員工作量**
- 各成員進行中的任務數
- 各成員即將到期的任務
- 工作量評估（低/適中/高/超載）

**2. 工作量分佈**
- 依專案分佈
- 依任務類型分佈
- 時間軸分佈

**3. 瓶頸分析**
- 工作量過重的成員
- 閒置的資源
- 技能缺口

**4. 調配建議**
- 任務重新分配建議
- 優先級調整
- 外部資源需求

請根據以下資訊分析團隊工作量：

【請在此描述團隊狀況】
- 團隊成員：
- 各成員目前任務：
- 分析期間：
- 特別關注事項：

我將為您提供：
- 各成員工作量評估
- 工作量分佈圖（文字版）
- 瓶頸與風險分析
- 具體調配建議"""

    def start_workflow(self, workflow_type: str, user_input: str = "") -> str:
        """
        啟動特定工作流程

        Args:
            workflow_type: 工作流程類型
            user_input: 用戶輸入

        Returns:
            助手回應
        """
        workflow_prompt = self.get_workflow_prompt(workflow_type)

        if not workflow_prompt:
            return "抱歉，不支援此工作流程。請輸入 /workflows 查看所有可用的工作流程。"

        full_message = f"{workflow_prompt}\n\n{user_input}" if user_input else workflow_prompt
        return self.chat(full_message)

    def list_workflows(self) -> str:
        """列出所有可用的工作流程"""
        return """
# Asana 專案管理助手 可用工作流程

## 專案管理類
1. **專案總覽** (`/projects`)
   - 查看所有專案狀態
   - 風險與進度概覽

2. **任務管理** (`/tasks` 或 `/create`)
   - 查看、建立、更新任務
   - 支援直接操作 Asana

3. **任務拆解** (`/breakdown`)
   - 將目標拆解為可執行任務
   - 可直接匯入 Asana

## 進度追蹤類
4. **狀態報告** (`/status`)
   - 專案進度報告
   - 風險與問題追蹤

5. **衝刺規劃** (`/sprint`)
   - 週期性工作計畫
   - 任務分配與排程

6. **工作量分析** (`/workload`)
   - 團隊負載分析
   - 資源調配建議

---

**快速使用：** 直接輸入指令（如 `/projects`）或描述您的需求！
"""

    # === Asana 直接操作方法 ===

    def list_projects(self) -> str:
        """列出 Asana 專案"""
        if not self.asana or not self.workspace_gid:
            return "無法連線 Asana，請確認 ASANA_ACCESS_TOKEN 已正確設定。"

        try:
            projects = self.asana.get_projects(self.workspace_gid)
            if not projects:
                return "目前沒有任何專案。"

            result = "# Asana 專案列表\n\n"
            for p in projects:
                result += f"- **{p.get('name', '未命名')}** (GID: `{p.get('gid', '')}`)\n"
            return result
        except Exception as e:
            return f"取得專案列表失敗: {e}"

    def list_tasks_for_project(self, project_gid: str) -> str:
        """列出專案中的任務"""
        if not self.asana:
            return "無法連線 Asana，請確認 ASANA_ACCESS_TOKEN 已正確設定。"

        try:
            tasks = self.asana.get_tasks(project_gid=project_gid)
            if not tasks:
                return "此專案目前沒有任何任務。"

            result = "# 任務列表\n\n"
            for t in tasks:
                status = "completed" if t.get("completed") else "pending"
                icon = "[v]" if status == "completed" else "[ ]"
                result += f"- {icon} **{t.get('name', '未命名')}** (GID: `{t.get('gid', '')}`)\n"
            return result
        except Exception as e:
            return f"取得任務列表失敗: {e}"

    def create_task_in_asana(
        self,
        project_gid: str,
        name: str,
        notes: str = "",
        assignee: Optional[str] = None,
        due_on: Optional[str] = None,
    ) -> str:
        """在 Asana 中建立任務"""
        if not self.asana:
            return "無法連線 Asana，請確認 ASANA_ACCESS_TOKEN 已正確設定。"

        try:
            task = self.asana.create_task(
                project_gid=project_gid,
                name=name,
                notes=notes,
                assignee=assignee,
                due_on=due_on,
            )
            return f"任務已建立: **{task.get('name', name)}** (GID: `{task.get('gid', '')}`)"
        except Exception as e:
            return f"建立任務失敗: {e}"
