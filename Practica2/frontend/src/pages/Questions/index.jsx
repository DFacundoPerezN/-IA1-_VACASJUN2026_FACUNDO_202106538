import { useEffect, useState } from "react";
import api from "../../services/api";
import Layout from "../../components/Layout";

import "./styles.css";

export default function Questions() {

    const [questions, setQuestions] =
        useState([]);

    const [categories, setCategories] =
        useState([]);

    const [editingId, setEditingId] =
        useState(null);

    const [form, setForm] =
        useState({
            question: "",
            answer: "",
            category_id: ""
        });

    useEffect(() => {

        loadQuestions();
        loadCategories();

    }, []);

    async function loadQuestions() {

        const response =
            await api.get(
                "/questions/with-category"
            );

        setQuestions(
            response.data
        );
    }

    async function loadCategories() {

        const response =
            await api.get(
                "/categories"
            );

        setCategories(
            response.data
        );
    }

    async function handleSubmit(event) {

        event.preventDefault();

        if (editingId) {

            await api.put(
                `/questions/${editingId}`,
                form
            );

        } else {

            await api.post(
                "/questions",
                form
            );
        }

        resetForm();

        loadQuestions();
    }

    function resetForm() {

        setEditingId(null);

        setForm({
            question: "",
            answer: "",
            category_id: ""
        });
    }

    async function deleteQuestion(id) {

        if (
            !window.confirm(
                "¿Eliminar pregunta?"
            )
        ) {
            return;
        }

        await api.delete(
            `/questions/${id}`
        );

        loadQuestions();
    }

    async function editQuestion(id) {

        const response =
            await api.get(
                `/questions/${id}`
            );

        setEditingId(id);

        setForm(response.data);
    }

    return (
    <Layout>
        <div className="questions-container">

            <h1>
                Preguntas
            </h1>

            <form
                onSubmit={handleSubmit}
                className="question-form"
            >

                <input
                    type="text"
                    placeholder="Pregunta"
                    value={form.question}
                    onChange={(e) =>
                        setForm({
                            ...form,
                            question:
                                e.target.value
                        })
                    }
                />

                <textarea
                    placeholder="Respuesta"
                    value={form.answer}
                    onChange={(e) =>
                        setForm({
                            ...form,
                            answer:
                                e.target.value
                        })
                    }
                />

                <select
                    value={
                        form.category_id
                    }
                    onChange={(e) =>
                        setForm({
                            ...form,
                            category_id:
                                e.target.value
                        })
                    }
                >

                    <option value="">
                        Seleccione
                    </option>

                    {
                        categories.map(
                            (category) => (

                                <option
                                    key={
                                        category.id
                                    }
                                    value={
                                        category.id
                                    }
                                >

                                    {
                                        category.name
                                    }

                                </option>

                            )
                        )
                    }

                </select>

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
                            Pregunta
                        </th>

                        <th>
                            Categoría
                        </th>

                        <th>
                            Acciones
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {
                        questions.map(
                            (question) => (

                                <tr
                                    key={
                                        question.id
                                    }
                                >

                                    <td>
                                        {
                                            question.question
                                        }
                                    </td>

                                    <td>
                                        {
                                            question.category
                                        }
                                    </td>

                                    <td>

                                        <button
                                            onClick={() =>
                                                editQuestion(
                                                    question.id
                                                )
                                            }
                                        >
                                            Editar
                                        </button>

                                        <button
                                            onClick={() =>
                                                deleteQuestion(
                                                    question.id
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

    </Layout>
    );
}