document.addEventListener("DOMContentLoaded", () => {
    // --- 1. MOTOR DEL CALENDARIO DINÁMICO ---
    const monthYearText = document.getElementById("month-year");
    const calendarGrid = document.getElementById("calendar-grid");
    const prevMonthBtn = document.getElementById("prev-month");
    const nextMonthBtn = document.getElementById("next-month");

    let currentDate = new Date();

    function renderCalendar(date) {
        const year = date.getFullYear();
        const month = date.getMonth();
        const today = new Date();

        const monthNames = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
        monthYearText.textContent = `${monthNames[month]} ${year}`;

        let html = `
            <div class="day-name">DOM</div><div class="day-name">LUN</div><div class="day-name">MAR</div>
            <div class="day-name">MIE</div><div class="day-name">JUE</div><div class="day-name">VIE</div><div class="day-name">SAB</div>
        `;

        const firstDayIndex = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        for (let i = 0; i < firstDayIndex; i++) {
            html += `<div class="day-empty"></div>`;
        }

        for (let i = 1; i <= daysInMonth; i++) {
            const dateValue = `${year}-${String(month + 1).padStart(2, '0')}-${String(i).padStart(2, '0')}`;
            const isToday = (i === today.getDate() && month === today.getMonth() && year === today.getFullYear());
            const checked = isToday ? "checked" : "";

            html += `
                <input type="radio" name="fecha" id="d${i}" value="${dateValue}" ${checked}>
                <label for="d${i}">${i}</label>
            `;
        }
        calendarGrid.innerHTML = html;
    }

    prevMonthBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar(currentDate);
    });

    nextMonthBtn.addEventListener("click", () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar(currentDate);
    });

    renderCalendar(currentDate);

    // --- 2. CONTROL DEL MODAL DEL MAPA ---
    const modal = document.getElementById("map-modal");
    const openMapBtn = document.getElementById("open-map");
    const closeMapBtn = document.getElementById("close-map");

    openMapBtn.addEventListener("click", () => modal.classList.add("active"));
    closeMapBtn.addEventListener("click", () => modal.classList.remove("active"));
    window.addEventListener("click", (e) => {
        if (e.target === modal) modal.classList.remove("active");
    });

    // --- 3. ENVÍO DE FORMULARIO ---
    document.getElementById('form-paso-1').addEventListener('submit', function(event) {
        event.preventDefault();

        const invitados = document.querySelector('input[name="invitados"]:checked');
        const mesa = document.querySelector('input[name="mesa"]:checked');
        const fecha = document.querySelector('input[name="fecha"]:checked');
        const hora = document.querySelector('input[name="hora"]:checked');

        if (!invitados || !mesa || !fecha || !hora) {
            alert("Por favor, selecciona invitados, mesa, fecha y hora.");
            return;
        }

        localStorage.setItem('reserva_invitados', invitados.value);
        localStorage.setItem('reserva_mesa', mesa.value);
        localStorage.setItem('reserva_fecha', fecha.value);
        localStorage.setItem('reserva_hora', hora.value + ":00");

        window.location.href = 'detalles_reserva.html';
    });
});