const API_URL = "http://127.0.0.1:8000";

export async function fetchCiudades() {
    const response = await fetch(`${API_URL}/ciudades/`);
    if (!response.ok) throw new Error("Error al obtener ciudades");
    return await response.json();
}

export async function postCiudad(nombreCiudad) {
    const response = await fetch(`${API_URL}/ciudades/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ city: nombreCiudad })
    });
    return await response.json();
}

export async function postRuta(ciudad1, ciudad2, distancia) {
    const response = await fetch(`${API_URL}/ciudades/ruta`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ city1: ciudad1, city2: ciudad2, distance: parseInt(distancia) })
    });
    return await response.json();
}

export async function fetchMejorRuta(c1, c2) {
    const response = await fetch(`${API_URL}/ciudades/mejor_ruta?city1=${c1}&city2=${c2}`);
    if (!response.ok) throw new Error("Error al consultar la mejor ruta");
    return await response.json();
}

export async function fetchTodasLasRutas(c1, c2) {
    const response = await fetch(`${API_URL}/ciudades/recorridos?city1=${c1}&city2=${c2}`);
    if (!response.ok) throw new Error("Error al consultar recorridos");
    return await response.json();
}