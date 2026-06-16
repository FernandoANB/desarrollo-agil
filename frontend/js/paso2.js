document.getElementById('form-paso-2').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const btnSubmit = document.getElementById('btn-submit');
    btnSubmit.innerText = "PROCESANDO...";
    btnSubmit.disabled = true;

    // Tomamos los invitados del Paso 1 (localStorage)
    const invitadosGuardados = localStorage.getItem('reserva_invitados') || "1";

    const payload = {
        id_servicio: 1, 
        cantidad_personas: parseInt(invitadosGuardados), 
        fecha: localStorage.getItem('reserva_fecha'),
        hora: localStorage.getItem('reserva_hora'),
        nombre_cliente: document.getElementById('nombre').value,
        rut: null, 
        email_cliente: document.getElementById('email').value,
        telefono: document.getElementById('telefono').value,
        notas: document.getElementById('notas').value
    };

    try {
        const response = await fetch('http://localhost:8000/reservas/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            // NO limpiamos el localStorage aún, porque confirmacion.html lo necesita para pintar los datos
            window.location.href = 'confirmacion.html';
        } else {
            console.error("Error de BD:", await response.json());
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