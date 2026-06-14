import { useEffect, useState } from "react";

import api from "../../services/api";
import Layout from "../../components/Layout";

export default function TelegramConfig() {

    const [chatId, setChatId] =
        useState("");

    useEffect(() => {

        loadConfig();

    }, []);

    async function loadConfig() {

        const response =
            await api.get(
                "/telegram/chat"
            );

        setChatId(
            response.data.chat_id
        );
    }

    async function saveConfig() {

        await api.put(
            "/telegram/chat",
            {
                chat_id: chatId
            }
        );

        alert(
            "Configuración guardada"
        );
    }

    return (
    <Layout>

        <div
            style={{
                maxWidth: "600px",
                margin: "auto",
                padding: "2rem"
            }}
        >

            <h1>
                Configuración Telegram
            </h1>

            <input
                type="text"
                value={chatId}
                onChange={(e) =>
                    setChatId(
                        e.target.value
                    )
                }
                placeholder="Chat ID"
                style={{
                    width: "100%",
                    padding: "10px"
                }}
            />

            <button
                onClick={saveConfig}
                style={{
                    marginTop: "1rem"
                }}
            >
                Guardar
            </button>

        </div>
        </Layout>  
    );
}