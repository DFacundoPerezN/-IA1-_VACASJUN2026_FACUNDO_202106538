const API_URL = "http://localhost:5000";

export const getInvoices = async () => {

    const token = localStorage.getItem("token");

    const response = await fetch(
        `${API_URL}/invoices`,
        {
            headers: {
                Authorization: `Bearer ${token}`
            }
        }
    );

    return response.json();
};

export const processInvoice = async (file) => {

    const token = localStorage.getItem("token");

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch(
        `${API_URL}/invoices/process`,
        {
            method: "POST",
            headers: {
                Authorization: `Bearer ${token}`
            },
            body: formData
        }
    );

    return response.json();
};