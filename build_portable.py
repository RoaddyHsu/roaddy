"""
創建可攜式 Python 應用程式套件
不需要 PyInstaller，使用 zipapp 和腳本包裝
"""

import os
import sys
import shutil
import zipfile
from pathlib import Path


def create_portable_package():
    """創建可攜式套件"""
    print("=" * 60)
    print("  弘爺漢堡 AI 行銷助手 - 可攜式套件打包工具")
    print("=" * 60)
    print()
    
    # 創建輸出目錄
    output_dir = Path("dist/portable")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("✓ 創建輸出目錄")
    
    # 複製源碼
    src_dest = output_dir / "src"
    if src_dest.exists():
        shutil.rmtree(src_dest)
    shutil.copytree("src", src_dest)
    print("✓ 複製源碼")
    
    # 複製配置文件
    config_dest = output_dir / "config"
    if config_dest.exists():
        shutil.rmtree(config_dest)
    shutil.copytree("config", config_dest)
    print("✓ 複製配置文件")
    
    # 複製環境變數範例
    shutil.copy2(".env.example", output_dir / ".env.example")
    print("✓ 複製環境變數範例")
    
    # 複製必要文件
    files_to_copy = [
        "requirements.txt",
        "README.md",
        "QUICKSTART.md",
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, output_dir / file)
    
    print("✓ 複製文件")
    
    # 創建啟動腳本 (Windows)
    launch_bat = output_dir / "啟動.bat"
    launch_bat.write_text("""@echo off
chcp 65001 >nul
echo =====================================
echo   弘爺漢堡 AI 行銷助手
echo =====================================
echo.

REM 檢查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo 錯誤: 未安裝 Python
    echo 請從 https://www.python.org/ 下載並安裝 Python 3.8 或更高版本
    pause
    exit /b 1
)

REM 檢查 .env 文件
if not exist .env (
    echo.
    echo 注意: 未找到 .env 文件
    echo 請複製 .env.example 為 .env 並填入 API Key
    echo.
    pause
    exit /b 1
)

REM 安裝依賴（如果需要）
if not exist ".installed" (
    echo 首次執行，正在安裝依賴套件...
    pip install -r requirements.txt
    if errorlevel 0 (
        echo. > .installed
    )
)

REM 設定 Python 路徑並執行
set PYTHONPATH=%~dp0
python src/main.py %*

pause
""", encoding='utf-8')
    
    print("✓ 創建 Windows 啟動腳本")
    
    # 創建啟動腳本 (Linux/Mac)
    launch_sh = output_dir / "啟動.sh"
    launch_sh.write_text("""#!/bin/bash

echo "====================================="
echo "  弘爺漢堡 AI 行銷助手"
echo "====================================="
echo ""

# 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "錯誤: 未安裝 Python 3"
    echo "請安裝 Python 3.8 或更高版本"
    exit 1
fi

# 檢查 .env 文件
if [ ! -f ".env" ]; then
    echo ""
    echo "注意: 未找到 .env 文件"
    echo "請複製 .env.example 為 .env 並填入 API Key"
    echo ""
    read -p "按 Enter 繼續..."
    exit 1
fi

# 安裝依賴（如果需要）
if [ ! -f ".installed" ]; then
    echo "首次執行，正在安裝依賴套件..."
    pip3 install -r requirements.txt
    if [ $? -eq 0 ]; then
        touch .installed
    fi
fi

# 設定 Python 路徑並執行
export PYTHONPATH="$(pwd)"
python3 src/main.py "$@"
""", encoding='utf-8')
    
    # 設定執行權限
    os.chmod(launch_sh, 0o755)
    
    print("✓ 創建 Linux/Mac 啟動腳本")
    
    # 創建使用說明
    readme = output_dir / "使用說明.txt"
    readme.write_text("""
弘爺漢堡 AI 行銷助手 - 可攜式版本
=====================================

📋 系統需求：
  - Python 3.8 或更高版本
  - 網路連線
  - Anthropic API Key

🚀 快速開始：

步驟 1：安裝 Python
  如果還沒安裝，請從 https://www.python.org/ 下載

步驟 2：設定 API Key
  1. 複製 .env.example 為 .env
  2. 用記事本開啟 .env
  3. 填入您的 Anthropic API Key：
     ANTHROPIC_API_KEY=sk-ant-api03-你的金鑰

步驟 3：執行程式
  Windows: 雙擊 "啟動.bat"
  Linux/Mac: 執行 "./啟動.sh"

💡 使用提示：
  - 首次執行會自動安裝依賴套件（需要幾分鐘）
  - 選擇助手後可使用快速指令，如 /daily、/social 等
  - 輸入 /help 查看詳細幫助
  - 輸入 /quit 返回主選單

📖 詳細文件：
  - README.md - 完整說明
  - QUICKSTART.md - 快速開始指南

❓ 常見問題：

Q: 如何取得 API Key？
A: 前往 https://console.anthropic.com/ 註冊並創建 API Key

Q: 程式無法啟動？
A: 檢查：
   1. Python 是否已安裝（執行 python --version）
   2. .env 文件是否存在且填入正確的 API Key
   3. 網路連線是否正常

Q: 顯示模組錯誤？
A: 刪除 .installed 文件，重新執行程式讓它重新安裝依賴

🆘 需要協助？
  請參考 README.md 或提交 Issue 到 GitHub

版本：1.0.0
""", encoding='utf-8')
    
    print("✓ 創建使用說明")
    
    # 創建安裝指令檔
    install_bat = output_dir / "安裝依賴.bat"
    install_bat.write_text("""@echo off
chcp 65001 >nul
echo 正在安裝依賴套件...
echo.
pip install -r requirements.txt
echo.
echo 安裝完成！
pause
""", encoding='utf-8')
    
    install_sh = output_dir / "安裝依賴.sh"
    install_sh.write_text("""#!/bin/bash
echo "正在安裝依賴套件..."
echo ""
pip3 install -r requirements.txt
echo ""
echo "安裝完成！"
read -p "按 Enter 繼續..."
""", encoding='utf-8')
    os.chmod(install_sh, 0o755)
    
    print("✓ 創建安裝腳本")
    
    # 計算大小
    total_size = sum(f.stat().st_size for f in output_dir.rglob('*') if f.is_file())
    
    print()
    print("=" * 60)
    print("  ✓ 打包完成！")
    print("=" * 60)
    print()
    print(f"輸出位置: {output_dir.absolute()}")
    print(f"套件大小: {total_size / 1024 / 1024:.2f} MB")
    print()
    print("📦 套件內容：")
    print("  - src/          源碼目錄")
    print("  - config/       配置文件")
    print("  - 啟動.bat      Windows 啟動程式")
    print("  - 啟動.sh       Linux/Mac 啟動程式")
    print("  - 使用說明.txt  快速開始指南")
    print()
    print("📝 使用方式：")
    print("  1. 將整個 portable 資料夾複製到目標電腦")
    print("  2. 複製 .env.example 為 .env 並填入 API Key")
    print("  3. 執行啟動腳本")
    print()
    print("💡 注意：目標電腦需要安裝 Python 3.8+")
    print()


if __name__ == "__main__":
    try:
        create_portable_package()
    except Exception as e:
        print(f"\n✗ 打包失敗: {e}")
        sys.exit(1)
