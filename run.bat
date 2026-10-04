@echo off
title MBTI Personality Test
cd /d "%~dp0"
echo Memulai MBTI Personality Test Web App...
python -m streamlit run app.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo Terjadi kendala saat menjalankan aplikasi. Pastikan Python dan dependensi terpasang.
    pause
)
