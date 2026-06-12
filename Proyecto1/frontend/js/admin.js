const URL = "http://127.0.0.1:8000/doctor";

export const admin = {
    // Inicializa la interfaz cargando todos los datos actuales
    async inicializar() {
        try {
            // Endpoints 1, 10
            const sintomas = await fetch(`${URL}/sintomas`).then(r => r.json());
            const fallas = await fetch(`${URL}/all_fallas`).then(r => r.json());

            // Llenar listas de administracion con botones de accion
            document.getElementById('lista-sintomas-admin').innerHTML = sintomas.map(s => `
                <li class="flex justify-between items-center bg-slate-700/40 p-2 rounded border border-slate-700">
                    <span class="capitalize text-sm">${s.replace(/_/g, ' ')}</span>
                    <div class="flex gap-1">
                        <button onclick="admin.editar('sintoma', '${s}')" class="text-xs bg-amber-600 px-2 py-1 rounded hover:bg-amber-700">Editar</button>
                        <button onclick="admin.borrar('sintoma', '${s}')" class="text-xs bg-rose-600 px-2 py-1 rounded hover:bg-rose-700">Borrar</button>
                    </div>
                </li>
            `).join('');

            document.getElementById('lista-fallas-admin').innerHTML = fallas.map(f => `
                <li class="flex justify-between items-center bg-slate-700/40 p-2 rounded border border-slate-700">
                    <span class="capitalize text-sm">${f.replace(/_/g, ' ')}</span>
                    <div class="flex gap-1">
                        <button onclick="admin.editar('falla', '${f}')" class="text-xs bg-amber-600 px-2 py-1 rounded hover:bg-amber-700">Editar</button>
                        <button onclick="admin.borrar('falla', '${f}')" class="text-xs bg-rose-600 px-2 py-1 rounded hover:bg-rose-700">Borrar</button>
                    </div>
                </li>
            `).join('');

            // Llenar los Selects de la conexion (Relaciones)
            document.getElementById('select-sintoma').innerHTML = 
                '<option value="" disabled selected>Selecciona sintoma...</option>' +
                sintomas.map(s => `<option value="${s}">${s.replace(/_/g, ' ')}</option>`).join('');

            document.getElementById('select-falla').innerHTML = 
                '<option value="" disabled selected>Selecciona falla...</option>' +
                fallas.map(f => `<option value="${f}">${f.replace(/_/g, ' ')}</option>`).join('');

        } catch (e) {
            console.error("Error cargando los datos de administracion:", e);
        }
    },

    // Crear nuevo elemento (Endpoints 5, 6)
    async agregar(tipo) {
        const input = document.getElementById(`input-${tipo}`);
        const valor = input.value.trim().toLowerCase().replace(/ /g, '_');
        if (!valor) return;

        await fetch(`${URL}/${tipo}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ [tipo]: valor })
        });
        
        input.value = "";
        this.inicializar();
    },

    // Eliminar elemento (Endpoints 12, 13)
    async borrar(tipo, valor) {
        if (!confirm(`¿Seguro que deseas eliminar el ${tipo}: ${valor.replace(/_/g, ' ')}?`)) return;

        try {
            await fetch(`${URL}/delete_${tipo}`, {
                method: 'DELETE',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ [tipo]: valor })
            });
            this.inicializar();
        } catch (e) {
            alert("No se pudo eliminar el elemento.");
        }
    },

    // Editar nombre de un elemento (Endpoints 15, 16)
    async editar(tipo, valorViejo) {
        const nuevoValor = prompt(`Editar ${tipo}:`, valorViejo.replace(/_/g, ' '));
        if (!nuevoValor || nuevoValor.trim() === "") return;
        
        const valorFormateado = nuevoValor.trim().toLowerCase().replace(/ /g, '_');

        try {
            await fetch(`${URL}/${tipo}`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    viejo: valorViejo,
                    nuevo: valorFormateado
                })
            });
            this.inicializar();
        } catch (e) {
            alert("No se pudo actualizar el elemento.");
        }
    },

    // Conectar falla con sintoma (Endpoint 8)
    async conectar() {
        const falla = document.getElementById('select-falla').value;
        const sintoma = document.getElementById('select-sintoma').value;

        if (!falla || !sintoma) return alert("Selecciona ambos campos.");

        await fetch(`${URL}/falla_sintoma`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ falla, sintoma })
        });
        alert("Relacion guardada exitosamente");
    }
};

window.admin = admin;
document.addEventListener('DOMContentLoaded', () => admin.inicializar());