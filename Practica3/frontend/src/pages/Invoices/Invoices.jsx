import { useEffect, useState } from "react";

import {
    getInvoices,
    processInvoice
} from "../../api/invoices";

import "../../styles/table.css";

function Invoices() {

    const [invoices, setInvoices] = useState([]);

    const [file, setFile] = useState(null);

    const loadInvoices = async () => {

        const data = await getInvoices();

        setInvoices(data);
    };

    useEffect(() => {
        loadInvoices();
    }, []);

    const handleUpload = async () => {

        if (!file) {
            alert("Seleccione un archivo");
            return;
        }

        await processInvoice(file);

        alert("Factura procesada");

        loadInvoices();
    };

    return (
        <div>

            <h1>Facturas</h1>

            <input
                type="file"
                onChange={(e) =>
                    setFile(e.target.files[0])
                }
            />

            <button
                onClick={handleUpload}
            >
                Procesar
            </button>

            <table className="table">

                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Factura</th>
                        <th>NIT</th>
                        <th>Total</th>
                        <th>Estado</th>
                    </tr>
                </thead>

                <tbody>

                    {invoices.map(invoice => (

                        <tr key={invoice.id}>

                            <td>{invoice.id}</td>

                            <td>
                                {invoice.invoice_number}
                            </td>

                            <td>
                                {invoice.nit}
                            </td>

                            <td>
                                {invoice.total}
                            </td>

                            <td>
                                {invoice.status}
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}

export default Invoices;