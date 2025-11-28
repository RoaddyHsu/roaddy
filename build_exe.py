"""
打包成執行檔的腳本
使用 PyInstaller 將程式打包成獨立執行檔
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def check_pyinstaller():
    """檢查 PyInstaller 是否已安裝"""
    try:
        import PyInstaller
        print("✓ PyInstaller 已安裝")
        return True
    except ImportError:
        print("✗ PyInstaller 未安裝")
        return False


def install_pyinstaller():
    """安裝 PyInstaller"""
    print("\n正在安裝 PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    print("✓ PyInstaller 安裝完成")


def build_executable():
    """打包成執行檔"""
    print("\n開始打包程式...")
    
    # 基本設定
    app_name = "弘爺漢堡AI行銷助手"
    main_script = "src/main.py"
    icon_file = "icon.ico" if os.path.exists("icon.ico") else None
    
    # PyInstaller 命令
    cmd = [
        "pyinstaller",
        "--name", app_name,
        "--onedir",  # 打包成資料夾（相容性更好）
        "--console",  # 顯示命令列視窗
        "--clean",
        "--noconfirm",
    ]
    
    # 添加圖示（如果存在）
    if icon_file:
        cmd.extend(["--icon", icon_file])
    
    # 添加資料檔案
    cmd.extend([
        "--add-data", f"config{os.pathsep}config",
        "--add-data", f".env{os.pathsep}.",
    ])
    
    # 隱藏導入
    cmd.extend([
        "--hidden-import", "anthropic",
        "--hidden-import", "openai",
        "--hidden-import", "rich",
        "--hidden-import", "prompt_toolkit",
        "--hidden-import", "click",
        "--hidden-import", "yaml",
    ])
    
    # 主程式
    cmd.append(main_script)
    
    # 執行打包
    print(f"執行命令: {' '.join(cmd)}")
    subprocess.check_call(cmd)
    
    print("\n✓ 打包完成！")
    print(f"\n執行檔位置: dist/{app_name}.exe")
    print(f"大小: {os.path.getsize(f'dist/{app_name}.exe') / 1024 / 1024:.1f} MB")


def create_portable_package():
    """創建可攜式版本（包含所有檔案）"""
    print("\n創建可攜式版本...")
    
    portable_dir = Path("dist/portable")
    portable_dir.mkdir(parents=True, exist_ok=True)
    
    # 複製必要檔案
    files_to_copy = [
        ".env.example",
        "config/config.yaml",
        "README.md",
        "requirements.txt",
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            dest = portable_dir / file
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, dest)
    
    # 創建啟動說明
    readme = portable_dir / "使用說明.txt"
    readme.write_text("""
弘爺漢堡 AI 行銷助手 - 可攜式版本
=====================================

使用步驟：

1. 複製 .env.example 到 .env
2. 編輯 .env 檔案，填入您的 Anthropic API Key
3. 執行 弘爺漢堡AI行銷助手.exe

注意事項：
- 首次執行可能需要較長時間載入
- 請確保網路連線正常
- API Key 請妥善保管

支援：
如有問題，請參考 README.md
""", encoding='utf-8')
    
    print(f"✓ 可攜式版本已創建: {portable_dir}")


def main():
    """主函數"""
    print("=" * 50)
    print("  弘爺漢堡 AI 行銷助手 - 打包工具")
    print("=" * 50)
    
    # 檢查並安裝 PyInstaller
    if not check_pyinstaller():
        install_pyinstaller()
    
    # 打包執行檔
    try:
        build_executable()
        create_portable_package()
        
        print("\n" + "=" * 50)
        print("  打包完成！")
        print("=" * 50)
        print("\n輸出檔案：")
        print("  1. dist/弘爺漢堡AI行銷助手.exe - 單一執行檔")
        print("  2. dist/portable/ - 可攜式版本（含設定檔）")
        print("\n使用方式：")
        print("  1. 將 .env.example 複製為 .env")
        print("  2. 填入 API Key")
        print("  3. 執行 exe 檔案")
        
    except Exception as e:
        print(f"\n✗ 打包失敗: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
