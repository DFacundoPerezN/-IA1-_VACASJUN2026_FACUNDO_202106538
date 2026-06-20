import { useEffect, useState } from "react";

import { getLogs } from "../../api/logs";

import "../../styles/table.css";
function Logs() {

    const [logs, setLogs] =
        useState([]);

    useEffect(() => {

        const loadLogs = async () => {

            const data =
                await getLogs();

            setLogs(data);
        };

        loadLogs();

    }, []);

    return (
        <div>

            <h1>Bitácora</h1>

            <table className="table">

                <thead>
                    <tr>
                        <th>ID Usuario Responsable</th>
                        <th>ID Factura</th>
                        <th>Fecha y Hora</th>
                        <th>Estado</th>
                        <th>Resultado</th>
                    </tr>
                </thead>

                <tbody>

                    {logs.map(log => (

                        <tr key={log.id}>

                            <td>
                                {log.user_id}
                            </td>

                            <td>
                                {log.invoice_id}
                            </td>

                            <td>
                                {log.processed_at}
                            </td>

                            <td>
                                {log.status}
                            </td>

                            <td>
                                {log.result}
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}

export default Logs;