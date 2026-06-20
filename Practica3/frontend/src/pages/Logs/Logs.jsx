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

            <table>

                <thead>
                    <tr>
                        <th>Fecha</th>
                        <th>Estado</th>
                        <th>Resultado</th>
                    </tr>
                </thead>

                <tbody>

                    {logs.map(log => (

                        <tr key={log.id}>

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