#!/bin/bash
# Script de inicialización para MVP del Proyecto

echo "================================"
echo "Inicializando MVP del Proyecto"
echo "================================"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Verificar que Python está instalado
echo -e "${YELLOW}[1/5]${NC} Verificando Python..."
if command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    echo -e "${GREEN}✓${NC} Python encontrado: $PYTHON_VERSION"
else
    echo -e "${RED}✗${NC} Python no encontrado. Por favor instala Python 3.9+"
    exit 1
fi

# 2. Verificar/crear venv
echo ""
echo -e "${YELLOW}[2/5]${NC} Verificando entorno virtual..."
if [ -d "backend/.venv" ]; then
    echo -e "${GREEN}✓${NC} Entorno virtual encontrado"
    source backend/.venv/bin/activate
else
    echo -e "${YELLOW}⚠${NC} Creando entorno virtual..."
    python -m venv backend/.venv
    source backend/.venv/bin/activate
fi

# 3. Instalar dependencias
echo ""
echo -e "${YELLOW}[3/5]${NC} Instalando dependencias..."
cd backend
pip install -r requirements.txt -q
echo -e "${GREEN}✓${NC} Dependencias instaladas"

# 4. Crear .env si no existe
echo ""
echo -e "${YELLOW}[4/5]${NC} Verificando configuración..."
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠${NC} Creando archivo .env desde .env.example..."
    cp .env.example .env
    echo -e "${GREEN}✓${NC} Archivo .env creado"
    echo -e "${YELLOW}  ⚠ Por favor, actualiza los valores en .env${NC}"
else
    echo -e "${GREEN}✓${NC} Archivo .env encontrado"
fi

# 5. Resumen
echo ""
echo -e "${YELLOW}[5/5]${NC} Resumen de configuración"
echo -e "${GREEN}✓${NC} Proyecto listo para ejecutarse"
echo ""
echo -e "${YELLOW}Próximos pasos:${NC}"
echo "1. Actualiza los valores en: backend/.env"
echo "2. Inicia el servidor: cd backend && uvicorn app.main:app --reload"
echo "3. Accede a la API: http://localhost:8000/docs"
echo ""
echo "================================"