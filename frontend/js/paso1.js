document.getElementById('form-paso-1').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita que la página recargue

    // 1. Capturar los valores
    const invitados = document.querySelector('input[name="invitados"]:checked');
    const fecha = document.getElementById('fecha-reserva').value;
    const hora = document.querySelector('input[name="hora"]:checked');

    // 2. Validar que todo esté seleccionado
    if (!invitados || !fecha || !hora) {
        alert("Por favor, selecciona invitados, fecha y hora.");
        return;
    }

    // 3. Guardar temporalmente en el navegador
    localStorage.setItem('reserva_invitados', invitados.value);
    localStorage.setItem('reserva_fecha', fecha);
    localStorage.setItem('reserva_hora', hora.value + ":00"); // Agregamos los segundos para la BD

    // 4. Ir al siguiente paso
    window.location.href = 'detalles_reserva.html';
});