import { useState } from "react";
import api from "../../services/api";
import { useNavigate } from "react-router-dom";

import "./styles.css";

export default function Login() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const [error, setError] = useState("");

    const navigate = useNavigate();

    async function handleSubmit(event) {

        event.preventDefault();

        try {

            const response = await api.post(
                "/login",
                {
                    username,
                    password
                }
            );

            localStorage.setItem(
                "token",
                response.data.token
            );

            navigate("/categories");

        } catch {

            setError(
                "Usuario o contraseña incorrectos"
            );
        }
    }

    return (
        <div className="login-container">

            <div className="login-card">

                <h1>SmartBot</h1>

                <form onSubmit={handleSubmit}>

                    <input
                        type="text"
                        placeholder="Usuario"
                        value={username}
                        onChange={(e) =>
                            setUsername(e.target.value)
                        }
                    />

                    <input
                        type="password"
                        placeholder="Contraseña"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                    />

                    {
                        error &&
                        <p className="error">
                            {error}
                        </p>
                    }

                    <button type="submit">
                        Iniciar Sesión
                    </button>

                </form>

            </div>

        </div>
    );
}