#!/bin/bash

# AI 行銷顧問系統啟動腳本

echo "==================================="
echo "   AI 行銷顧問系統"
echo "==================================="
echo ""

# 檢查 Python 是否安裝
if ! command -v python3 &> /dev/null; then
    echo "錯誤: 未找到 Python 3"
    echo "請先安裝 Python 3.8 或更高版本"
    exit 1
fi

# 檢查虛擬環境
if [ ! -d "venv" ]; then
    echo "創建虛擬環境..."
    python3 -m venv venv
fi

# 啟動虛擬環境
echo "啟動虛擬環境..."
source venv/bin/activate

# 安裝依賴
if [ ! -f "venv/.installed" ]; then
    echo "安裝依賴套件..."
    pip install -r requirements.txt
    touch venv/.installed
fi

# 檢查 .env 文件
if [ ! -f ".env" ]; then
    echo ""
    echo "警告: 未找到 .env 文件"
    echo "請複製 .env.example 到 .env 並填入您的 API 金鑰："
    echo "  cp .env.example .env"
    echo ""
    read -p "是否現在創建 .env 文件? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp .env.example .env
        echo "已創建 .env 文件，請編輯並填入 API 金鑰後重新運行"
        exit 0
    fi
fi

# 創建必要目錄
mkdir -p logs
mkdir -p conversations

# 運行程式
echo ""
echo "啟動 AI 行銷顧問系統..."
echo ""
python src/main.py "$@"

# 退出虛擬環境
deactivate
