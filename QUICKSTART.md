# 🚀 QUICKSTART - MVP EN 5 MINUTOS

## Paso 1: Abre PowerShell
```powershell
cd "C:\Users\fabia\Desktop\Universidad\9no Semestre\Desarrollo Agil\desarrollo-agil"
```

## Paso 2: Activa el Entorno
```powershell
.\.venv\Scripts\Activate.ps1
```

Deberías ver: `(.venv) PS C:\...>`

## Paso 3: Instala Dependencias (solo la primera vez)
```powershell
cd backend
pip install -r requirements.txt
```

## Paso 4: Inicia el Servidor
```powershell
uvicorn app.main:app --reload
```

Verás:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

## Paso 5: Abre el Navegador

🌐 **http://localhost:8000/docs**

---

## 🎮 Pruebas Rápidas

### Crear Empresa
1. En Swagger, busca `POST /empresas/`
2. Haz clic en "Try it out"
3. Llena: nombre, descripción, dirección, teléfono, email
4. Ejecuta → Copia el `id_empresa`

### Configurar Horarios
1. Abre: `frontend/html/gestion_horarios.html`
2. Cambia `let empresaId = 1` a tu ID
3. Configura horarios
4. Haz clic: "Guardar Cambios"

### Bloquear Fechas
1. Abre: `frontend/html/gestion_fechas_bloqueadas.html`
2. Cambia `let empresaId = 1` a tu ID
3. Selecciona fecha, ingresa motivo
4. Haz clic: "Bloquear Fecha"

### Configurar Marca
1. Abre: `frontend/html/gestion_marca.html`
2. Cambia `let empresaId = 1` a tu ID
3. Logo, colores, fotos
4. Observa preview
5. Haz clic: "Guardar Cambios de Marca"

### Gestionar Servicios
1. Abre: `frontend/html/gestion_servicios.html`
2. Cambia `let empresaId = 1` a tu ID
3. Crea nuevos servicios/platos
4. Define duración y capacidad
5. Activa o desactiva servicios

### Crear Reserva (exitosa)
En Swagger, `POST /reservas/`:
```json
{
  "id_servicio": 1,
  "nombre_cliente": "Juan",
  "email_cliente": "juan@mail.com",
  "fecha": "2024-12-23",
  "hora": "19:00:00",
  "cantidad_personas": 4
}
```

### Crear Reserva (debe fallar)
Mismo JSON pero con `"fecha": "2024-12-22"` (domingo cerrado)

**Resultado**: Error 400 ❌

---

## 📁 Archivos Clave

- **Backend**: `backend/app/main.py`
- **BD**: PostgreSQL Supabase (ver `.env`)
- **Interfaces**: `frontend/html/*.html`
- **Docs API**: http://localhost:8000/docs
- **Documentación**: `PASOS_PARA_EJECUTAR_MVP.md`

---

## ⚡ Alternativa Aún Más Fácil

En lugar de pasos 1-4, simplemente:

1. Haz **doble clic** en: `INICIAR_MVP.bat`
2. Se abre la terminal automáticamente
3. Abre navegador en: http://localhost:8000/docs

---

## 🛑 Detener el Servidor

En la terminal donde está corriendo:
```
Ctrl + C
```

---

## ✅ ¿Preguntas?

- Lee: `PASOS_PARA_EJECUTAR_MVP.md`
- Lee: `RESUMEN_FINAL_MVP_LISTO.md`
- Consulta: `EJEMPLOS_API_US_12_13_14.json`

---

**¡Listo! Ahora a ejecutar.** 🎉