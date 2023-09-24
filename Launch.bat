@echo off
title YouTube Video Downloader

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

:: Check if the pytube library is installed
python -c "import pytube" >nul 2>&1
if errorlevel 1 (
    echo Installing pytube...
    pip install pytube
)

:: Prompt the user for the YouTube URL
set /p youtube_url=Enter the YouTube URL: 

:: Launch the Python script
python PYYTDownloader.py %youtube_url%

pause
