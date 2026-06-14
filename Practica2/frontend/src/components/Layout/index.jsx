import { Link } from "react-router-dom";

import "./styles.css";

export default function Layout({ children }) {

    return (
        <div className="layout">

            <aside className="sidebar">

                <h2>SmartBot</h2>

                <Link to="/dashboard">
                    Dashboard
                </Link>

                <Link to="/categories">
                    Categorías
                </Link>

                <Link to="/questions">
                    Preguntas
                </Link>

                <Link to="/telegram">
                    Telegram
                </Link>

                <button
                    onClick={() => {
                        localStorage.removeItem(
                            "token"
                        );

                        window.location.href = "/";
                    }}
                >
                    Cerrar sesión
                </button>

            </aside>

            <main className="content">
                {children}
            </main>

        </div>
    );
}