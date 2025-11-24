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

from assistants import (
    ContentMarketingAssistant,
    CopywritingAssistant,
    SocialMediaAssistant,
    BrandStrategyAssistant,
    CreativeMarketingAssistant,
    EcommerceAssistant,
    AdManagerAssistant,
)
from utils.logger import logger

console = Console()


# 助手類別映射
ASSISTANTS = {
    "1": ("內容行銷助手", ContentMarketingAssistant),
    "2": ("文案撰寫助手", CopywritingAssistant),
    "3": ("社群行銷助手", SocialMediaAssistant),
    "4": ("品牌策略顧問", BrandStrategyAssistant),
    "5": ("創意行銷助手", CreativeMarketingAssistant),
    "6": ("電商行銷助手", EcommerceAssistant),
    "7": ("廣告投手", AdManagerAssistant),
}


def show_welcome():
    """顯示歡迎訊息"""
    welcome_text = """
# 🚀 AI 行銷顧問系統

歡迎使用 AI 行銷顧問系統！這是一套完整的智能行銷助手，包含以下功能：

1. **內容行銷助手** - SEO 優化與內容策略
2. **文案撰寫助手** - 跨平台文案創作
3. **社群行銷助手** - 社群策略規劃
4. **品牌策略顧問** - 品牌定位分析
5. **創意行銷助手** - 創意發想系統
6. **電商行銷助手** - 電商策略規劃
7. **廣告投手** - 廣告投放策略

請選擇您需要的助手開始使用！
"""
    console.print(Panel(Markdown(welcome_text), title="歡迎", border_style="green"))


def show_menu():
    """顯示選單"""
    menu_text = """
請選擇您需要的助手：

[1] 內容行銷助手 - SEO 優化與內容策略
[2] 文案撰寫助手 - 跨平台文案創作
[3] 社群行銷助手 - 社群策略規劃
[4] 品牌策略顧問 - 品牌定位分析
[5] 創意行銷助手 - 創意發想系統
[6] 電商行銷助手 - 電商策略規劃
[7] 廣告投手 - 廣告投放策略

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

    console.print("\n[yellow]輸入 '/help' 查看幫助，'/export' 匯出對話，'/clear' 清空歷史，'/quit' 返回選單[/yellow]\n")

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

        console.print(f"\n[green]✓ 對話已匯出：[/green]")
        console.print(f"  - JSON: {json_file}")
        console.print(f"  - Markdown: {md_file}")

    except Exception as e:
        console.print(f"[red]匯出失敗: {e}[/red]")
        logger.error(f"匯出對話錯誤: {e}")


@click.command()
@click.option("--assistant", "-a", type=click.Choice(["1", "2", "3", "4", "5", "6", "7"]), help="直接選擇助手")
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

            choice = Prompt.ask("請選擇", choices=["0", "1", "2", "3", "4", "5", "6", "7"])

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
