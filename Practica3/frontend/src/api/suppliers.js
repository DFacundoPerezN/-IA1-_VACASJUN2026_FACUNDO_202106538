const API_URL = import.meta.env.VITE_API_URL;

const getToken = () =>
    localStorage.getItem("token");

export const getSuppliers = async () => {

    const response = await fetch(
        `${API_URL}/suppliers`,
        {
            headers: {
                Authorization:
                    `Bearer ${getToken()}`
            }
        }
    );

    return response.json();
};

export const createSupplier = async (
    supplier
) => {

    const response = await fetch(
        `${API_URL}/suppliers`,
        {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/json",
                Authorization:
                    `Bearer ${getToken()}`
            },
            body: JSON.stringify(
                supplier
            )
        }
    );

    return response.json();
};

export const updateSupplier = async (
    id,
    supplier
) => {

    const response = await fetch(
        `${API_URL}/suppliers/${id}`,
        {
            method: "PUT",
            headers: {
                "Content-Type":
                    "application/json",
                Authorization:
                    `Bearer ${getToken()}`
            },
            body: JSON.stringify(
                supplier
            )
        }
    );

    return response.json();
};

export const deleteSupplier = async (
    id
) => {

    await fetch(
        `${API_URL}/suppliers/${id}`,
        {
            method: "DELETE",
            headers: {
                Authorization:
                    `Bearer ${getToken()}`
            }
        }
    );
};