document.getElementById('form-paso-2').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const btnSubmit = document.getElementById('btn-submit');
    btnSubmit.innerText = "PROCESANDO...";
    btnSubmit.disabled = true;

    // 1. Armar el objeto JSON con datos de ambos pasos
    const payload = {
        id_servicio: 1, // NOTA: Debe existir el servicio con ID 1 en tu Base de Datos
        cantidad_personas: parseInt(localStorage.getItem('reserva_invitados')),
        fecha: localStorage.getItem('reserva_fecha'),
        hora: localStorage.getItem('reserva_hora'),
        nombre_cliente: document.getElementById('nombre').value,
        rut: document.getElementById('rut').value,
        email_cliente: document.getElementById('email').value,
        telefono: document.getElementById('telefono').value,
        notas: document.getElementById('notas').value
    };

    try {
        // 2. Hacer la petición POST al backend
        const response = await fetch('http://localhost:8000/reservas/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            // 3. Si todo sale bien, limpiar datos temporales y mostrar éxito
            localStorage.clear();
            window.location.href = 'confirmacion.html';
        } else {
            // Manejar errores de validación del backend
            const errorData = await response.json();
            console.error("Error de BD:", errorData);
            alert("No se pudo confirmar la reserva. Revisa los datos.");
            btnSubmit.innerText = "CONFIRMAR RESERVA";
            btnSubmit.disabled = false;
        }
    } catch (error) {
        console.error("Error de conexión:", error);
        alert("Error al conectar con el servidor.");
        btnSubmit.innerText = "CONFIRMAR RESERVA";
        btnSubmit.disabled = false;
    }
});