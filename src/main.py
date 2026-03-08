"""
AI 行銷顧問系統主程式
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from pathlib import Path
import json

from src.assistants import (
    ManagerAssistant,
    PersonnelAAssistant,
    PersonnelBAssistant,
    PersonnelCAssistant,
    PersonnelDAssistant,
    PersonnelEAssistant,
    AsanaAssistant,
)
from src.utils.logger import logger

console = Console()


# 助手類別映射
ASSISTANTS = {
    "1": ("Manager (主管)", ManagerAssistant),
    "2": ("人員 A (行銷企劃)", PersonnelAAssistant),
    "3": ("人員 B (數位行銷)", PersonnelBAssistant),
    "4": ("人員 C (視覺設計)", PersonnelCAssistant),
    "5": ("人員 D (美編專員)", PersonnelDAssistant),
    "6": ("人員 E (團購PM)", PersonnelEAssistant),
    "7": ("Asana 專案管理", AsanaAssistant),
}


def show_welcome():
    """顯示歡迎訊息"""
    welcome_text = """
# 🚀 弘爺漢堡 AI 行銷團隊系統

歡迎使用弘爺漢堡 AI 行銷團隊系統！這是一套完整的智能行銷助手團隊，包含以下角色：

1. **Manager (主管)** - 策略規劃與決策支援、團隊管理
2. **人員 A (行銷企劃)** - 活動企劃、文案創作、IP 授權、異業合作
3. **人員 B (數位行銷)** - 社群經營、廣告投放、數據分析、網紅合作
4. **人員 C (視覺設計)** - 品牌視覺、活動設計、包裝設計、空間設計
5. **人員 D (美編專員)** - 設計執行、簡報製作、社群圖文、印刷製作
6. **人員 E (團購PM)** - 團購企劃、廠商管理、物流配送、客服處理
7. **Asana 專案管理** - 任務管理、進度追蹤、衝刺規劃、工作量分析

請選擇您需要的助手開始使用！
"""
    console.print(Panel(Markdown(welcome_text), title="歡迎", border_style="green"))


def show_menu():
    """顯示選單"""
    menu_text = """
請選擇您需要的助手：

[1] Manager (主管) - 策略規劃與決策支援、團隊管理
[2] 人員 A (行銷企劃) - 活動企劃、文案創作、IP 授權、異業合作
[3] 人員 B (數位行銷) - 社群經營、廣告投放、數據分析、網紅合作
[4] 人員 C (視覺設計) - 品牌視覺、活動設計、包裝設計、空間設計
[5] 人員 D (美編專員) - 設計執行、簡報製作、社群圖文、印刷製作
[6] 人員 E (團購PM) - 團購企劃、廠商管理、物流配送、客服處理
[7] Asana 專案管理 - 任務管理、進度追蹤、衝刺規劃、工作量分析

[0] 退出系統
"""
    console.print(Panel(menu_text, title="功能選單", border_style="blue"))


def chat_with_assistant(assistant, assistant_name: str):
    """
    與助手對話

    Args:
        assistant: 助手實例
        assistant_name: 助手名稱
    """
    # 顯示歡迎訊息
    welcome = assistant.get_welcome_message()
    console.print(Panel(Markdown(welcome), title=assistant_name, border_style="cyan"))

    # 創建對話歷史文件
    project_root = Path(__file__).parent.parent
    history_dir = project_root / "conversations"
    history_dir.mkdir(exist_ok=True)
    history_file = history_dir / f"{assistant.assistant_type}_history.txt"

    # 創建對話會話
    session = PromptSession(history=FileHistory(str(history_file)))

    # Manager 助手額外說明
    extra_commands = ""
    if isinstance(assistant, ManagerAssistant):
        extra_commands = ", '/workflows' 查看工作流程"

    console.print(f"\n[yellow]輸入 '/help' 查看幫助{extra_commands}，'/export' 匯出對話，'/clear' 清空歷史，'/quit' 返回選單[/yellow]\n")

    while True:
        try:
            # 獲取用戶輸入
            user_input = session.prompt("\n您: ").strip()

            if not user_input:
                continue

            # 處理命令
            if user_input.lower() == "/quit":
                console.print("[yellow]返回主選單...[/yellow]")
                break

            elif user_input.lower() == "/help":
                help_msg = assistant.get_help_message()
                console.print(Panel(Markdown(help_msg), title="幫助", border_style="green"))
                continue

            elif user_input.lower() == "/clear":
                assistant.clear_history()
                console.print("[green]✓ 對話歷史已清空[/green]")
                continue

            elif user_input.lower() == "/export":
                export_conversation(assistant, assistant_name)
                continue

            # Asana 助手特殊命令
            elif isinstance(assistant, AsanaAssistant):
                if user_input.lower() == "/workflows":
                    response = assistant.list_workflows()
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/projects":
                    console.print("[cyan]載入 Asana 專案...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_PROJECT_OVERVIEW)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() in ("/tasks", "/create"):
                    console.print("[cyan]啟動任務管理...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_TASK_MANAGEMENT)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/breakdown":
                    console.print("[cyan]啟動任務拆解...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_TASK_BREAKDOWN)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/status":
                    console.print("[cyan]產出專案狀態報告...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_PROGRESS_REPORT)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/sprint":
                    console.print("[cyan]啟動衝刺規劃...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_SPRINT_PLANNING)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/workload":
                    console.print("[cyan]分析團隊工作量...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_TEAM_WORKLOAD)
                    console.print(Markdown(response))
                    continue

            # Manager 助手特殊命令
            elif isinstance(assistant, ManagerAssistant):
                if user_input.lower() == "/workflows":
                    response = assistant.list_workflows()
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/daily":
                    console.print("[cyan]啟動每日工作規劃...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_DAILY_PLANNING)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/social":
                    console.print("[cyan]啟動社群內容產出...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_SOCIAL_CONTENT)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/ad":
                    console.print("[cyan]啟動廣告投放決策...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_AD_STRATEGY)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/decide":
                    console.print("[cyan]啟動專案決策分析...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_PROJECT_DECISION)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/qa":
                    console.print("[cyan]啟動內容品質把關...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_CONTENT_QA)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/weekly":
                    console.print("[cyan]啟動週會準備與記錄...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_WEEKLY_MEETING)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/monthly":
                    console.print("[cyan]啟動月度績效評估...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_MONTHLY_REVIEW)
                    console.print(Markdown(response))
                    continue
                elif user_input.lower() == "/annual":
                    console.print("[cyan]啟動年度規劃...[/cyan]")
                    response = assistant.start_workflow(assistant.WORKFLOW_ANNUAL_PLANNING)
                    console.print(Markdown(response))
                    continue

            # 發送訊息並獲取回應
            console.print(f"\n[cyan]{assistant_name}:[/cyan] ", end="")
            with console.status("[bold green]思考中..."):
                response = assistant.chat(user_input)

            # 顯示回應
            console.print(Markdown(response))

        except KeyboardInterrupt:
            console.print("\n[yellow]按 Ctrl+D 或輸入 /quit 返回選單[/yellow]")
            continue

        except EOFError:
            console.print("\n[yellow]返回主選單...[/yellow]")
            break

        except Exception as e:
            console.print(f"\n[red]錯誤: {e}[/red]")
            logger.error(f"對話錯誤: {e}")


def export_conversation(assistant, assistant_name: str):
    """
    匯出對話記錄

    Args:
        assistant: 助手實例
        assistant_name: 助手名稱
    """
    try:
        project_root = Path(__file__).parent.parent
        export_dir = project_root / "conversations"
        export_dir.mkdir(exist_ok=True)

        # 匯出為 JSON
        json_file = export_dir / f"{assistant.assistant_type}_conversation.json"
        json_data = assistant.export_conversation("json")
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

        # 匯出為 Markdown
        md_file = export_dir / f"{assistant.assistant_type}_conversation.md"
        md_content = assistant.export_conversation("markdown")
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md_content)

        console.print("\n[green]✓ 對話已匯出：[/green]")
        console.print(f"  - JSON: {json_file}")
        console.print(f"  - Markdown: {md_file}")

    except Exception as e:
        console.print(f"[red]匯出失敗: {e}[/red]")
        logger.error(f"匯出對話錯誤: {e}")


@click.command()
@click.option("--assistant", "-a", type=click.Choice(["1", "2", "3", "4", "5", "6", "7", "8"]), help="直接選擇助手")
def main(assistant):
    """AI 行銷顧問系統"""
    try:
        # 顯示歡迎訊息
        show_welcome()

        # 如果指定了助手，直接啟動
        if assistant:
            assistant_name, assistant_class = ASSISTANTS[assistant]
            console.print(f"\n[green]啟動 {assistant_name}...[/green]\n")
            assistant_instance = assistant_class()
            chat_with_assistant(assistant_instance, assistant_name)
            return

        # 主循環
        while True:
            show_menu()

            choice = Prompt.ask("請選擇", choices=["0", "1", "2", "3", "4", "5", "6", "7", "8"])

            if choice == "0":
                console.print("\n[green]感謝使用 AI 行銷顧問系統！再見！[/green]\n")
                break

            # 啟動選定的助手
            assistant_name, assistant_class = ASSISTANTS[choice]
            console.print(f"\n[green]啟動 {assistant_name}...[/green]\n")

            try:
                assistant_instance = assistant_class()
                chat_with_assistant(assistant_instance, assistant_name)
            except Exception as e:
                console.print(f"\n[red]啟動助手失敗: {e}[/red]")
                logger.error(f"啟動助手錯誤: {e}")
                console.print("[yellow]請檢查配置文件和 API 金鑰設定[/yellow]\n")

    except KeyboardInterrupt:
        console.print("\n\n[green]感謝使用 AI 行銷顧問系統！再見！[/green]\n")

    except Exception as e:
        console.print(f"\n[red]系統錯誤: {e}[/red]")
        logger.error(f"系統錯誤: {e}")


if __name__ == "__main__":
    main()
