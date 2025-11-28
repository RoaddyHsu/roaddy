@echo off
REM 弘爺漢堡 AI 行銷助手 - 打包腳本（Windows）

echo =====================================
echo   弘爺漢堡 AI 行銷助手 - 打包工具
echo =====================================
echo.

REM 檢查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo 錯誤: 未找到 Python
    pause
    exit /b 1
)

REM 啟動虛擬環境（如果存在）
if exist venv\Scripts\activate.bat (
    echo 啟動虛擬環境...
    call venv\Scripts\activate.bat
)

REM 安裝 PyInstaller
echo 安裝打包工具...
pip install pyinstaller

REM 執行打包
echo.
echo 開始打包程式...
python build_exe.py

echo.
echo 打包完成！
echo.
echo 執行檔位置：
echo   - Windows: dist\弘爺漢堡AI行銷助手.exe
echo   - 可攜版: dist\portable\
echo.
pause
