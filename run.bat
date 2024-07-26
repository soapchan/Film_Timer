REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Installing Python...
    REM Download Python installer
    curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
    REM Install Python silently
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    REM Clean up installer
    del python-installer.exe
)

pip install -r c:/path/to/requirements.txt
echo Running the film timer...

python src\main.py

pause