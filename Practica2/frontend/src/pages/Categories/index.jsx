import { useEffect, useState } from "react";

import api from "../../services/api";

import "./styles.css";

export default function Categories() {

    const [categories, setCategories] =
        useState([]);

    const [name, setName] =
        useState("");

    const [editingId, setEditingId] =
        useState(null);

    async function loadCategories() {

        try {

            const response =
                await api.get("/categories");

            setCategories(
                response.data
            );

        } catch (error) {

            console.error(error);

        }
    }

    useEffect(() => {

        loadCategories();

    }, []);

    async function handleSubmit(event) {

        event.preventDefault();

        try {

            if (editingId) {

                await api.put(
                    `/categories/${editingId}`,
                    { name }
                );

            } else {

                await api.post(
                    "/categories",
                    { name }
                );

            }

            setName("");

            setEditingId(null);

            loadCategories();

        } catch (error) {

            console.error(error);

        }
    }

    async function deleteCategory(id) {

        if (
            !window.confirm(
                "¿Eliminar categoría?"
            )
        ) {
            return;
        }

        try {

            await api.delete(
                `/categories/${id}`
            );

            loadCategories();

        } catch (error) {

            console.error(error);

        }
    }

    function editCategory(category) {

        setEditingId(
            category.id
        );

        setName(
            category.name
        );
    }

    return (
        <div className="categories-container">

            <h1>
                Categorías
            </h1>

            <form
                onSubmit={handleSubmit}
                className="category-form"
            >

                <input
                    type="text"
                    placeholder="Nombre"
                    value={name}
                    onChange={(e) =>
                        setName(
                            e.target.value
                        )
                    }
                />

                <button type="submit">

                    {
                        editingId
                            ? "Actualizar"
                            : "Crear"
                    }

                </button>

            </form>

            <table>

                <thead>

                    <tr>

                        <th>
                            Nombre
                        </th>

                        <th>
                            Acciones
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {
                        categories.map(
                            (category) => (

                                <tr
                                    key={
                                        category.id
                                    }
                                >

                                    <td>
                                        {
                                            category.name
                                        }
                                    </td>

                                    <td>

                                        <button
                                            onClick={() =>
                                                editCategory(
                                                    category
                                                )
                                            }
                                        >
                                            Editar
                                        </button>

                                        <button
                                            onClick={() =>
                                                deleteCategory(
                                                    category.id
                                                )
                                            }
                                        >
                                            Eliminar
                                        </button>

                                    </td>

                                </tr>

                            )
                        )
                    }

                </tbody>

            </table>

        </div>
    );
}