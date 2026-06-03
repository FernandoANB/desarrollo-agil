# Estructura del backend

Para el backend se va a desarrollar usando python, fast api y supabase para el almacenamiento 


El flujo lógico interno de esta arquitectura sigueria el siguiente patrón:

> Cliente → Router → Service → Database → Response

Los componentes principales que definen esta arquitectura son:

Routers (app/routers/): Gestionan las peticiones HTTP (Endpoints) y delegan la lógica a la capa de servicios.

Servicios (app/services/): Contienen la lógica de negocio, centralizando las operaciones para mantener el main.py limpio y modular.


## Instrucciones de Ejecución

1. **Preparar el entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configurar variables de entorno:**
   Crea un archivo `.env` en la carpeta `backend/` con el siguiente formato:
   ```bash
   DATABASE_URL="postgresql+psycopg://usuario:password@host:puerto/postgres"
   ```
4. **Ejecutar el servidor:**
   ```bash
   uvicorn app.main:app --reload
   ```
