import { Link } from "react-router-dom";

import "./styles.css";

export default function Dashboard() {

    return (
        <div className="dashboard-container">

            <div className="dashboard-card">

                <h1>SmartBot Admin</h1>

                <p>
                    Panel de administración del sistema.
                </p>

                <div className="dashboard-links">

                    <Link
                        to="/categories"
                        className="dashboard-button"
                    >
                        Categorías
                    </Link>

                    <Link
                        to="/questions"
                        className="dashboard-button"
                    >
                        Preguntas
                    </Link>

                    <Link
                        to="/telegram"
                        className="dashboard-button"
                    >
                        Configuración Telegram
                    </Link>

                </div>

            </div>

        </div>
    );
}