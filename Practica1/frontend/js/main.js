import { fetchCiudades, postCiudad, postRuta, fetchMejorRuta, fetchTodasLasRutas } from './api.js';

// Elementos - Dom
const listaCiudades = document.getElementById('lista-ciudades');
const formCiudad = document.getElementById('form-ciudad');
const inputCiudad = document.getElementById('input-ciudad');
const formRuta = document.getElementById('form-ruta');
const inputDistancia = document.getElementById('input-distancia');

// Elementos Selects (Ahora son 4 en total)
const selects = [
    document.getElementById('select-origen'),
    document.getElementById('select-destino'),
    document.getElementById('search-origen'),
    document.getElementById('search-destino')
];

// Botones de Búsqueda y Resultados
const btnMejor = document.getElementById('btn-buscar-mejor');
const btnTodas = document.getElementById('btn-buscar-todas');
const contenedorResultados = document.getElementById('contenedor-resultados');

/**
 * Renderiza la lista y llena todos los dropdowns del sistema
 */
async function actualizarInterfaz() {
    try {
        const ciudades = await fetchCiudades();
        
        // 1. Dibujar lista lateral
        listaCiudades.innerHTML = ciudades.map(c => 
            `<li class="py-2 capitalize flex items-center font-medium border-b">${c.replace(/_/g, ' ')}</li>`
        ).join('') || `<li class="py-2 text-sm">Sin datos.</li>`;

        // 2. Llenar los 4 Selects manteniendo la selección previa si aplica
        selects.forEach(select => {
            const valorPrevio = select.value;
            select.innerHTML = '<option value="" disabled selected>Selecciona...</option>';
            ciudades.forEach(c => {
                select.insertAdjacentHTML('beforeend', `<option value="${c}">${c.replace(/_/g, ' ')}</option>`);
            });
            if (ciudades.includes(valorPrevio)) select.value = valorPrevio;
        });

    } catch (e) {
        console.error(e);
        listaCiudades.innerHTML = `<li class="py-2 text-red-400 text-sm">⚠️ Error de conexión</li>`;
    }
}

/**
 * Pinta de forma estética un array de caminos en el contenedor
 */
function mostrarResultadosHtml(titulo, datosRutas, esListaMultiple = false) {
    contenedorResultados.classList.remove('hidden');
    contenedorResultados.innerHTML = `<h3 class="text-sm font-semibold text-indigo-400 uppercase tracking-wider">${titulo}</h3>`;

    const rutas = esListaMultiple ? datosRutas : [datosRutas];

    if (!rutas || rutas.length === 0 || (rutas[0] && !rutas[0].cities)) {
        contenedorResultados.insertAdjacentHTML('beforeend', `<div class="p-4 bg-slate-900 border border-slate-700 text-slate-400 italic rounded">No se encontraron caminos lógicos entre estas ciudades en Prolog.</div>`);
        return;
    }

    rutas.forEach((ruta, index) => {
        const flechasCamino = ruta.cities.map(c => `<span class="capitalize font-semibold">${c.replace(/_/g, ' ')}</span>`).join(' -> ');
        const htmlCard = `
            <div class="p-4 rounded-lg border shadow-inner flex flex-col gap-2">
                <div class="text-xs flex justify-between">
                    <span>Opcion #${index + 1}</span>
                    <span class="font-mono font-bold text-emerald-400">${ruta.distance} km total</span>
                </div>
                <div class="text-sm tracking-wide p-2.5 rounded border overflow-x-auto">${flechasCamino}</div>
            </div>`;
        contenedorResultados.insertAdjacentHTML('beforeend', htmlCard);
    });
}

// --- ESCUCHADORES DE EVENTOS ---

formCiudad.addEventListener('submit', async (e) => {
    e.preventDefault();
    const nueva = inputCiudad.value.trim().toLowerCase().replace(/ /g, '_');
    const res = await postCiudad(nueva);
    alert(res.message);
    if (res.success) { inputCiudad.value = ""; actualizarInterfaz(); }
});

formRuta.addEventListener('submit', async (e) => {
    e.preventDefault();
    const [orig, dest] = [selects[0].value, selects[1].value];
    if (orig === dest) return alert("Origen y Destino idénticos.");
    
    const res = await postRuta(orig, dest, inputDistancia.value);
    alert(res.message);
    if (res.success) { inputDistancia.value = ""; selects[0].value = ""; selects[1].value = ""; }
});

btnMejor.addEventListener('click', async () => {
    const [o, d] = [selects[2].value, selects[3].value];
    if (!o || !d) return alert("Selecciona origen y destino para buscar.");
    try {
        const datos = await fetchMejorRuta(o, d);
        mostrarResultadosHtml("🏆 Ruta Óptima Detectada (Menor Distancia)", datos, false);
    } catch { alert("Error al procesar la mejor ruta."); }
});

btnTodas.addEventListener('click', async () => {
    const [o, d] = [selects[2].value, selects[3].value];
    if (!o || !d) return alert("Selecciona origen y destino para buscar.");
    try {
        const datos = await fetchTodasLasRutas(o, d);
        // Manejamos si el json viene envuelto en un objeto o es la lista directa
        const listaRutas = Array.isArray(datos) ? datos : (datos.recorridos || Object.values(datos)[0]);
        mostrarResultadosHtml("🔀 Todos los Caminos Alternativos Encontrados", listaRutas, true);
    } catch { alert("Error al procesar los caminos de Prolog."); }
});

document.addEventListener('DOMContentLoaded', actualizarInterfaz);