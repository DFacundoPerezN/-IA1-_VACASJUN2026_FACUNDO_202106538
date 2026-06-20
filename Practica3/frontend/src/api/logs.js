const API_URL = "http://localhost:5000";

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