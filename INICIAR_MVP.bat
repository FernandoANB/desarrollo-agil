@echo off
REM Script para iniciar el MVP en Windows

echo.
echo ================================
echo   INICIANDO MVP - Sistema de Reservas
echo ================================
echo.

REM Cambiar a la raíz del proyecto
cd /d "%~dp0"

REM Activar entorno virtual
echo [1/2] Activando entorno virtual...
call .venv\Scripts\activate.bat

REM Cambiar a backend
cd backend

REM Iniciar servidor
echo [2/2] Iniciando servidor FastAPI...
echo.
echo.
echo ================================
echo ✓ Servidor iniciado en: http://localhost:8000
echo ✓ Documentación en: http://localhost:8000/docs
echo ================================
echo.

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause