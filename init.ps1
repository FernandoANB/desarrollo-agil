# Script de inicialización para MVP del Proyecto (Windows)

Write-Host "================================"
Write-Host "Inicializando MVP del Proyecto"
Write-Host "================================"
Write-Host ""

# Color codes
$ErrorForegroundColor = "Red"
$SuccessForegroundColor = "Green"
$WarningForegroundColor = "Yellow"

# 1. Verificar que Python está instalado
Write-Host "[1/5] Verificando Python..." -ForegroundColor $WarningForegroundColor
$pythonVersion = python --version 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Python encontrado: $pythonVersion" -ForegroundColor $SuccessForegroundColor
} else {
    Write-Host "✗ Python no encontrado. Por favor instala Python 3.9+" -ForegroundColor $ErrorForegroundColor
    exit 1
}

# 2. Verificar/crear venv
Write-Host ""
Write-Host "[2/5] Verificando entorno virtual..." -ForegroundColor $WarningForegroundColor
if (Test-Path "backend\.venv") {
    Write-Host "✓ Entorno virtual encontrado" -ForegroundColor $SuccessForegroundColor
    & "backend\.venv\Scripts\Activate.ps1"
} else {
    Write-Host "⚠ Creando entorno virtual..." -ForegroundColor $WarningForegroundColor
    python -m venv "backend\.venv"
    & "backend\.venv\Scripts\Activate.ps1"
}

# 3. Instalar dependencias
Write-Host ""
Write-Host "[3/5] Instalando dependencias..." -ForegroundColor $WarningForegroundColor
cd backend
pip install -r requirements.txt -q
Write-Host "✓ Dependencias instaladas" -ForegroundColor $SuccessForegroundColor

# 4. Crear .env si no existe
Write-Host ""
Write-Host "[4/5] Verificando configuración..." -ForegroundColor $WarningForegroundColor
if (!(Test-Path ".env")) {
    Write-Host "⚠ Creando archivo .env desde .env.example..." -ForegroundColor $WarningForegroundColor
    Copy-Item ".env.example" ".env"
    Write-Host "✓ Archivo .env creado" -ForegroundColor $SuccessForegroundColor
    Write-Host "  ⚠ Por favor, actualiza los valores en .env" -ForegroundColor $WarningForegroundColor
} else {
    Write-Host "✓ Archivo .env encontrado" -ForegroundColor $SuccessForegroundColor
}

# 5. Resumen
Write-Host ""
Write-Host "[5/5] Resumen de configuración" -ForegroundColor $WarningForegroundColor
Write-Host "✓ Proyecto listo para ejecutarse" -ForegroundColor $SuccessForegroundColor
Write-Host ""
Write-Host "Próximos pasos:" -ForegroundColor $WarningForegroundColor
Write-Host "1. Actualiza los valores en: backend\.env"
Write-Host "2. Inicia el servidor: cd backend && uvicorn app.main:app --reload"
Write-Host "3. Accede a la API: http://localhost:8000/docs"
Write-Host ""
Write-Host "================================"