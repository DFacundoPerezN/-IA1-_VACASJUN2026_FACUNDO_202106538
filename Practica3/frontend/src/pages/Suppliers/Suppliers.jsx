import {
    useEffect,
    useState
} from "react";

import {
    getSuppliers,
    createSupplier,
    updateSupplier,
    deleteSupplier
} from "../../api/suppliers";

import "../../styles/table.css";

function Suppliers() {

    const [suppliers,setSuppliers] = useState([]);
    const [name,setName] = useState("");
    const [nit,setNit] = useState("");
    const [email, setEmail] = useState("");
    const [phone, setPhone] = useState("");

    const [editingId,setEditingId] = useState(null);

    const loadSuppliers =
        async () => {

        const data =
            await getSuppliers();

        setSuppliers(data);
    };

    useEffect(() => {

        loadSuppliers();

    }, []);

    const handleSubmit =
        async () => {

        const supplier = {
            name,
            nit,
            email,
            phone
        };

        if (editingId) {

            await updateSupplier(
                editingId,
                supplier
            );

        } else {

            await createSupplier(
                supplier
            );
        }
        setName("");
        setNit("");
        setEmail("");
        setPhone("");
        setEditingId(null);

        loadSuppliers();
    };

    const handleEdit =
        (supplier) => {

        setEditingId(supplier.id );

        setName(  supplier.name);

        setNit( supplier.nit);

        setEmail(supplier.email || "");

        setPhone(supplier.phone || "");
    };

    const handleDelete =
        async (id) => {

        if (
            !window.confirm(
                "¿Eliminar proveedor?"
            )
        ) return;

        await deleteSupplier(id);

        loadSuppliers();
    };

    return (
        <div>

            <h1>
                Proveedores
            </h1>

            <div
                className="form-group"
            >

                <input
                    placeholder="Nombre"
                    value={name}
                    onChange={(e) =>
                        setName(
                            e.target.value
                        )
                    }
                />

            </div>

            <div
                className="form-group"
            >

                <input
                    placeholder="NIT"
                    value={nit}
                    onChange={(e) =>
                        setNit(
                            e.target.value
                        )
                    }
                />
                <input
                    placeholder="Correo"
                    value={email}
                    onChange={(e) =>
                        setEmail(e.target.value)
                    }
                />

                <input
                    placeholder="Teléfono"
                    value={phone}
                    onChange={(e) =>
                        setPhone(e.target.value)
                    }
                />

            </div>

            <button
                className="btn btn-success"
                onClick={handleSubmit}
            >
                {
                    editingId
                    ? "Actualizar"
                    : "Crear"
                }
            </button>

            <div
                className="table-container"
            >

                <table
                    className="table"
                >

                    <thead>

                        <tr>

                            <th>ID</th>
                            <th>Nombre</th>
                            <th>NIT</th>
                            <th>Acciones</th>

                        </tr>

                    </thead>

                    <tbody>

                        {
                            suppliers.map(
                                supplier => (

                            <tr
                                key={
                                    supplier.id
                                }
                            >

                                <td>
                                    {supplier.id}
                                </td>

                                <td>
                                    {supplier.name}
                                </td>

                                <td>
                                    {supplier.nit}
                                </td>

                                <td>

                                    <button
                                        className="btn btn-warning"
                                        onClick={() =>
                                            handleEdit(
                                                supplier
                                            )
                                        }
                                    >
                                        Editar
                                    </button>

                                    {" "}

                                    <button
                                        className="btn btn-danger"
                                        onClick={() =>
                                            handleDelete(
                                                supplier.id
                                            )
                                        }
                                    >
                                        Eliminar
                                    </button>

                                </td>

                            </tr>

                        ))}
                    </tbody>

                </table>

            </div>

        </div>
    );
}

export default Suppliers;