"""
Asana API 客戶端
"""

import os
import requests
from typing import List, Dict, Optional, Any
from src.utils.logger import logger


class AsanaClient:
    """Asana API 客戶端"""

    BASE_URL = "https://app.asana.com/api/1.0"

    def __init__(self, access_token: Optional[str] = None):
        """
        初始化 Asana 客戶端

        Args:
            access_token: Asana Personal Access Token
        """
        self.access_token = access_token or os.getenv("ASANA_ACCESS_TOKEN")
        if not self.access_token:
            raise ValueError("請設定 ASANA_ACCESS_TOKEN 環境變數")

        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        logger.info("Asana 客戶端初始化完成")

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """
        發送 API 請求

        Args:
            method: HTTP 方法
            endpoint: API 端點
            **kwargs: 請求參數

        Returns:
            API 回應資料
        """
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.request(
                method, url, headers=self.headers, **kwargs
            )
            response.raise_for_status()
            return response.json().get("data", {})
        except requests.exceptions.HTTPError as e:
            logger.error(f"Asana API 請求失敗: {e}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Asana API 連線錯誤: {e}")
            raise

    # === 使用者 ===

    def get_me(self) -> Dict[str, Any]:
        """取得目前登入的使用者資訊"""
        return self._request("GET", "users/me")

    # === 工作區 ===

    def get_workspaces(self) -> List[Dict[str, Any]]:
        """取得所有工作區"""
        return self._request("GET", "workspaces")

    # === 專案 ===

    def get_projects(self, workspace_gid: str) -> List[Dict[str, Any]]:
        """
        取得工作區中的所有專案

        Args:
            workspace_gid: 工作區 GID
        """
        return self._request(
            "GET", "projects", params={"workspace": workspace_gid}
        )

    def get_project(self, project_gid: str) -> Dict[str, Any]:
        """
        取得專案詳細資訊

        Args:
            project_gid: 專案 GID
        """
        return self._request("GET", f"projects/{project_gid}")

    def create_project(
        self,
        workspace_gid: str,
        name: str,
        notes: str = "",
        color: str = "light-green",
        layout: str = "list",
    ) -> Dict[str, Any]:
        """
        建立新專案

        Args:
            workspace_gid: 工作區 GID
            name: 專案名稱
            notes: 專案描述
            color: 專案顏色
            layout: 版面配置 (list/board/calendar/timeline)
        """
        data = {
            "data": {
                "workspace": workspace_gid,
                "name": name,
                "notes": notes,
                "color": color,
                "default_view": layout,
            }
        }
        return self._request("POST", "projects", json=data)

    # === 任務 ===

    def get_tasks(
        self,
        project_gid: Optional[str] = None,
        assignee: Optional[str] = None,
        workspace_gid: Optional[str] = None,
        completed_since: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        取得任務列表

        Args:
            project_gid: 專案 GID（依專案篩選）
            assignee: 負責人（依負責人篩選）
            workspace_gid: 工作區 GID（搭配 assignee 使用）
            completed_since: 完成時間篩選（ISO 8601 格式）
        """
        params = {}
        if project_gid:
            params["project"] = project_gid
        if assignee:
            params["assignee"] = assignee
        if workspace_gid:
            params["workspace"] = workspace_gid
        if completed_since:
            params["completed_since"] = completed_since

        return self._request("GET", "tasks", params=params)

    def get_task(self, task_gid: str) -> Dict[str, Any]:
        """
        取得任務詳細資訊

        Args:
            task_gid: 任務 GID
        """
        return self._request("GET", f"tasks/{task_gid}")

    def create_task(
        self,
        project_gid: str,
        name: str,
        notes: str = "",
        assignee: Optional[str] = None,
        due_on: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        建立新任務

        Args:
            project_gid: 專案 GID
            name: 任務名稱
            notes: 任務描述
            assignee: 負責人 GID
            due_on: 截止日期 (YYYY-MM-DD)
        """
        data = {
            "data": {
                "projects": [project_gid],
                "name": name,
                "notes": notes,
            }
        }
        if assignee:
            data["data"]["assignee"] = assignee
        if due_on:
            data["data"]["due_on"] = due_on

        return self._request("POST", "tasks", json=data)

    def update_task(self, task_gid: str, **fields) -> Dict[str, Any]:
        """
        更新任務

        Args:
            task_gid: 任務 GID
            **fields: 要更新的欄位
        """
        data = {"data": fields}
        return self._request("PUT", f"tasks/{task_gid}", json=data)

    def complete_task(self, task_gid: str) -> Dict[str, Any]:
        """
        將任務標記為完成

        Args:
            task_gid: 任務 GID
        """
        return self.update_task(task_gid, completed=True)

    # === 區段 (Section) ===

    def get_sections(self, project_gid: str) -> List[Dict[str, Any]]:
        """
        取得專案中的所有區段

        Args:
            project_gid: 專案 GID
        """
        return self._request("GET", f"projects/{project_gid}/sections")

    def create_section(
        self, project_gid: str, name: str
    ) -> Dict[str, Any]:
        """
        在專案中建立新區段

        Args:
            project_gid: 專案 GID
            name: 區段名稱
        """
        data = {"data": {"name": name}}
        return self._request(
            "POST", f"projects/{project_gid}/sections", json=data
        )

    # === 子任務 ===

    def get_subtasks(self, task_gid: str) -> List[Dict[str, Any]]:
        """
        取得任務的子任務

        Args:
            task_gid: 任務 GID
        """
        return self._request("GET", f"tasks/{task_gid}/subtasks")

    def create_subtask(
        self,
        parent_task_gid: str,
        name: str,
        notes: str = "",
        assignee: Optional[str] = None,
        due_on: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        建立子任務

        Args:
            parent_task_gid: 父任務 GID
            name: 子任務名稱
            notes: 子任務描述
            assignee: 負責人 GID
            due_on: 截止日期 (YYYY-MM-DD)
        """
        data = {"data": {"name": name, "notes": notes}}
        if assignee:
            data["data"]["assignee"] = assignee
        if due_on:
            data["data"]["due_on"] = due_on

        return self._request(
            "POST", f"tasks/{parent_task_gid}/subtasks", json=data
        )

    # === 留言 ===

    def add_comment(self, task_gid: str, text: str) -> Dict[str, Any]:
        """
        在任務中新增留言

        Args:
            task_gid: 任務 GID
            text: 留言內容
        """
        data = {"data": {"text": text}}
        return self._request(
            "POST", f"tasks/{task_gid}/stories", json=data
        )

    # === 標籤 ===

    def get_tags(self, workspace_gid: str) -> List[Dict[str, Any]]:
        """
        取得工作區中的所有標籤

        Args:
            workspace_gid: 工作區 GID
        """
        return self._request(
            "GET", "tags", params={"workspace": workspace_gid}
        )

    def add_tag_to_task(
        self, task_gid: str, tag_gid: str
    ) -> Dict[str, Any]:
        """
        為任務新增標籤

        Args:
            task_gid: 任務 GID
            tag_gid: 標籤 GID
        """
        data = {"data": {"tag": tag_gid}}
        return self._request(
            "POST", f"tasks/{task_gid}/addTag", json=data
        )

    # === 搜尋 ===

    def search_tasks(
        self,
        workspace_gid: str,
        text: Optional[str] = None,
        assignee: Optional[str] = None,
        projects: Optional[List[str]] = None,
        completed: Optional[bool] = None,
    ) -> List[Dict[str, Any]]:
        """
        搜尋任務

        Args:
            workspace_gid: 工作區 GID
            text: 搜尋文字
            assignee: 負責人 GID
            projects: 專案 GID 列表
            completed: 是否已完成
        """
        params = {}
        if text:
            params["text"] = text
        if assignee:
            params["assignee.any"] = assignee
        if projects:
            params["projects.any"] = ",".join(projects)
        if completed is not None:
            params["completed"] = str(completed).lower()

        return self._request(
            "GET",
            f"workspaces/{workspace_gid}/tasks/search",
            params=params,
        )
