document.addEventListener("DOMContentLoaded", () => {
    // --- 1. MOTOR DEL CALENDARIO DINÁMICO ---
    const monthYearText = document.getElementById("month-year");
    const calendarGrid = document.getElementById("calendar-grid");
    const prevMonthBtn = document.getElementById("prev-month");
    const nextMonthBtn = document.getElementById("next-month");

    let currentDate = new Date(); // Inicia en el día de hoy

    function renderCalendar(date) {
        const year = date.getFullYear();
        const month = date.getMonth();
        const today = new Date();

        const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
        monthYearText.textContent = `${monthNames[month]} ${year}`;

        // Nombres de los días de la semana
        let html = `
            <div class="day-name">DOM</div><div class="day-name">LUN</div><div class="day-name">MAR</div>
            <div class="day-name">MIE</div><div class="day-name">JUE</div><div class="day-name">VIE</div><div class="day-name">SAB</div>
        `;

        // Calcular el primer día del mes (0 = Domingo, 6 = Sábado)
        const firstDayIndex = new Date(year, month, 1).getDay();
        // Calcular la cantidad de días que tiene el mes actual
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        // Rellenar espacios vacíos antes del primer día del mes
        for (let i = 0; i < firstDayIndex; i++) {
            html += `<div class="day-empty"></div>`;
        }

        // Crear los botones para cada día
        for (let i = 1; i <= daysInMonth; i++) {
            // Formatear la fecha para la base de datos: YYYY-MM-DD
            const dateValue = `${year}-${String(month + 1).padStart(2, '0')}-${String(i).padStart(2, '0')}`;
            
            // Marcar el día actual como seleccionado por defecto
            const isToday = (i === today.getDate() && month === today.getMonth() && year === today.getFullYear());
            const checked = isToday ? "checked" : "";

            html += `
                <input type="radio" name="fecha" id="d${i}" value="${dateValue}" ${checked}>
                <label for="d${i}">${i}</label>
            `;
        }

        calendarGrid.innerHTML = html;
    }

    // Eventos para cambiar de mes
    prevMonthBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar(currentDate);
    });

    nextMonthBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar(currentDate);
    });

    // Dibujar el calendario inicial al cargar la página
    renderCalendar(currentDate);


    // --- 2. LÓGICA DE ENVÍO DE FORMULARIO (La que ya tenías) ---
    document.getElementById('form-paso-1').addEventListener('submit', function(event) {
        event.preventDefault();

        const invitados = document.querySelector('input[name="invitados"]:checked');
        const fecha = document.querySelector('input[name="fecha"]:checked');
        const hora = document.querySelector('input[name="hora"]:checked');

        if (!invitados || !fecha || !hora) {
            alert("Por favor, selecciona invitados, fecha y hora.");
            return;
        }

        // Guardar en almacenamiento local para usar en el paso 2
        localStorage.setItem('reserva_invitados', invitados.value);
        localStorage.setItem('reserva_fecha', fecha.value);
        localStorage.setItem('reserva_hora', hora.value + ":00");

        window.location.href = 'detalles_reserva.html';
    });
});