#!/bin/bash

# 弘爺漢堡 AI 行銷助手 - 打包腳本（Linux/Mac）

echo "====================================="
echo "  弘爺漢堡 AI 行銷助手 - 打包工具"
echo "====================================="
echo ""

# 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "錯誤: 未找到 Python 3"
    exit 1
fi

# 啟動虛擬環境（如果存在）
if [ -d "venv" ]; then
    echo "啟動虛擬環境..."
    source venv/bin/activate
fi

# 安裝 PyInstaller
echo "安裝打包工具..."
pip install pyinstaller

# 執行打包
echo ""
echo "開始打包程式..."
python build_exe.py

echo ""
echo "打包完成！"
echo ""
echo "執行檔位置："
echo "  - Linux: dist/弘爺漢堡AI行銷助手"
echo "  - 可攜版: dist/portable/"
