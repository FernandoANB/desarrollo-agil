document.getElementById('form-paso-1').addEventListener('submit', function(event) {
    event.preventDefault();

    // Capturar los valores de los botones seleccionados (checked)
    const invitados = document.querySelector('input[name="invitados"]:checked');
    const fecha = document.querySelector('input[name="fecha"]:checked');
    const hora = document.querySelector('input[name="hora"]:checked');

    if (!invitados || !fecha || !hora) {
        alert("Por favor, selecciona invitados, fecha y hora.");
        return;
    }

    localStorage.setItem('reserva_invitados', invitados.value);
    localStorage.setItem('reserva_fecha', fecha.value);
    localStorage.setItem('reserva_hora', hora.value + ":00");

    window.location.href = 'detalles_reserva.html';
});