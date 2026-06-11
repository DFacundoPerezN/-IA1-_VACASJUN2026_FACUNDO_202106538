const URL = "http://127.0.0.1:8000/doctor";

export const getSintomas = () => fetch(`${URL}/sintomas`).then(r => r.json());

export const diagnosticar = (sintomas) => 
    fetch(`${URL}/obtener_falla`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ sintomas })
    }).then(r => r.json());

export const getRecomendaciones = (sintomas) => 
    fetch(`${URL}/recomendaciones`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ sintomas })
    }).then(r => r.json());