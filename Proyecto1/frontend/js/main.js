import { getSintomas, diagnosticar, getRecomendaciones } from './api.js';

const listaSintomasDiv = document.getElementById('lista-sintomas');
const btnDiagnosticar = document.getElementById('btn-diagnosticar');
const divResultado = document.getElementById('resultado');
const ulRecomendaciones = document.getElementById('recomendaciones');
const ulHistorial = document.getElementById('lista-historial');
const btnLimpiarHistorial = document.getElementById('btn-limpiar-historial');

/**
 * Carga los síntomas desde la API y crea checkboxes
 */
async function cargarSintomas() {
    try {
        const sintomas = await getSintomas();
        listaSintomasDiv.innerHTML = sintomas.map(s => `
            <label class="flex items-center space-x-2 cursor-pointer p-1">
                <input type="checkbox" value="${s}" class="form-checkbox h-5 w-5 text-indigo-600">
                <span class="capitalize">${s.replace(/_/g, ' ')}</span>
            </label>
        `).join('');
    } catch (e) {
        listaSintomasDiv.innerHTML = `<p class="text-red-400">Error al cargar síntomas.</p>`;
    }
}
/**
 * Renderiza el historial almacenado en LocalStorage
 */
function mostrarHistorial() {
    const historial = JSON.parse(localStorage.getItem('doctor_byte_history')) || [];
    
    if (historial.length === 0) {
        ulHistorial.innerHTML = `<li class="text-slate-500 italic">No hay consultas recientes.</li>`;
        return;
    }

    ulHistorial.innerHTML = historial.map(item => `
        <li class="bg-slate-800/60 p-2.5 rounded border border-slate-700/50 flex flex-col gap-1">
            <div class="flex justify-between text-xs text-slate-400 font-mono">
                <span>${item.fecha}</span>
                <span class="text-green-400 font-bold">${item.falla}</span>
            </div>
            <div class="text-slate-300 capitalize text-xs">
                Síntomas: ${item.sintomas.join(', ').replace(/_/g, ' ')}
            </div>
        </li>
    `).join('');
}

/**
 * Guarda una nueva entrada en el historial local
 */
function guardarEnHistorial(sintomas, fallaDetectada) {
    const historial = JSON.parse(localStorage.getItem('doctor_byte_history')) || [];
    
    const nuevaConsulta = {
        fecha: new Date().toLocaleString(),
        sintomas: sintomas,
        falla: fallaDetectada ? fallaDetectada.replace(/_/g, ' ') : "Falla Desconocida"
    };

    // Agregar al inicio y mantener un límite máximo de 10 registros
    historial.unshift(nuevaConsulta);
    if (historial.length > 10) historial.pop();

    localStorage.setItem('doctor_byte_history', JSON.stringify(historial));
    mostrarHistorial();
}

/**
 * Ejecuta el diagnóstico y obtiene recomendaciones
 */
btnDiagnosticar.addEventListener('click', async () => {
    // 1. Obtener síntomas marcados
    const seleccionados = Array.from(
        document.querySelectorAll('#lista-sintomas input:checked')
    ).map(el => el.value);

    if (seleccionados.length === 0) return alert("Selecciona al menos un síntoma.");

    // 2. Limpiar UI
    divResultado.innerText = "Analizando...";
    ulRecomendaciones.innerHTML = "";

    // Capturamos el booleano del interruptor
    const enviarNotificacion = document.getElementById('switch-notificar').checked;

    try {
        // 3. Llamadas concurrentes a la API
        const [resFalla, resRec] = await Promise.all([
            diagnosticar(seleccionados, enviarNotificacion),
            getRecomendaciones(seleccionados, enviarNotificacion)
        ]);

        // 4. Mostrar Resultados
        divResultado.innerText = resFalla.falla 
            ? `Falla detectada: ${resFalla.falla.replace(/_/g, ' ')}` 
            : "No se pudo identificar una falla específica.";

        ulRecomendaciones.innerHTML = resRec.recommendations?.map(rec => 
            `<li class="mb-1 capitalize">${rec.replace(/_/g, ' ')}</li>`
        ).join('') || "<li>No hay recomendaciones disponibles.</li>";

        guardarEnHistorial(seleccionados, resFalla.falla);

    } catch (e) {
        divResultado.innerText = "Error en el diagnóstico.";
        console.error(e);
    }
});

// Inicializar
document.addEventListener('DOMContentLoaded', () => {
    cargarSintomas();
    mostrarHistorial();
});