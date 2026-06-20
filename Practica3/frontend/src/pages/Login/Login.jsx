import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { login } from "../../api/auth";

function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await login(
                username,
                password
            );

            if (response.token) {

                localStorage.setItem(
                    "token",
                    response.token
                );

                navigate("/dashboard");

                return;
            }

            alert(
                response.message ||
                "Credenciales inválidas"
            );

        } catch (error) {

            alert(
                "Error al iniciar sesión"
            );

            console.error(error);
        }
    };

    return (
        <div className="login-container">

            <form
                className="login-form"
                onSubmit={handleLogin}
            >

                <h2>
                    Invoice OCR
                </h2>

                <input
                    type="text"
                    placeholder="Usuario"
                    value={username}
                    onChange={(e) =>
                        setUsername(
                            e.target.value
                        )
                    }
                />

                <input
                    type="password"
                    placeholder="Contraseña"
                    value={password}
                    onChange={(e) =>
                        setPassword(
                            e.target.value
                        )
                    }
                />

                <button type="submit">
                    Iniciar Sesión
                </button>

            </form>

        </div>
    );
}

export default Login;