import { getSintomas, diagnosticar, getRecomendaciones } from './api.js';

const listaSintomasDiv = document.getElementById('lista-sintomas');
const btnDiagnosticar = document.getElementById('btn-diagnosticar');
const divResultado = document.getElementById('resultado');
const ulRecomendaciones = document.getElementById('recomendaciones');

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

    try {
        // 3. Llamadas concurrentes a la API
        const [resFalla, resRec] = await Promise.all([
            diagnosticar(seleccionados),
            getRecomendaciones(seleccionados)
        ]);

        // 4. Mostrar Resultados
        divResultado.innerText = resFalla.falla 
            ? `Falla detectada: ${resFalla.falla.replace(/_/g, ' ')}` 
            : "No se pudo identificar una falla específica.";

        ulRecomendaciones.innerHTML = resRec.recommendations?.map(rec => 
            `<li class="mb-1 capitalize">${rec.replace(/_/g, ' ')}</li>`
        ).join('') || "<li>No hay recomendaciones disponibles.</li>";

    } catch (e) {
        divResultado.innerText = "Error en el diagnóstico.";
        console.error(e);
    }
});

// Inicializar
document.addEventListener('DOMContentLoaded', cargarSintomas);