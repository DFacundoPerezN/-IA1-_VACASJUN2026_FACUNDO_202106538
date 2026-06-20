const API_URL = import.meta.env.VITE_API_URL;

export const getLogs = async () => {

    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_URL}/logs`,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.json();
};