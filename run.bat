@echo off
REM AI 行銷顧問系統啟動腳本 (Windows)

echo ===================================
echo    AI 行銷顧問系統
echo ===================================
echo.

REM 檢查 Python 是否安裝
python --version >nul 2>&1
if errorlevel 1 (
    echo 錯誤: 未找到 Python
    echo 請先安裝 Python 3.8 或更高版本
    pause
    exit /b 1
)

REM 檢查虛擬環境
if not exist "venv" (
    echo 創建虛擬環境...
    python -m venv venv
)

REM 啟動虛擬環境
echo 啟動虛擬環境...
call venv\Scripts\activate.bat

REM 安裝依賴
if not exist "venv\.installed" (
    echo 安裝依賴套件...
    pip install -r requirements.txt
    type nul > venv\.installed
)

REM 檢查 .env 文件
if not exist ".env" (
    echo.
    echo 警告: 未找到 .env 文件
    echo 請複製 .env.example 到 .env 並填入您的 API 金鑰
    echo.
    set /p create_env="是否現在創建 .env 文件? (y/n) "
    if /i "%create_env%"=="y" (
        copy .env.example .env
        echo 已創建 .env 文件，請編輯並填入 API 金鑰後重新運行
        pause
        exit /b 0
    )
)

REM 創建必要目錄
if not exist "logs" mkdir logs
if not exist "conversations" mkdir conversations

REM 運行程式
echo.
echo 啟動 AI 行銷顧問系統...
echo.
python src\main.py %*

REM 退出虛擬環境
call deactivate

pause
