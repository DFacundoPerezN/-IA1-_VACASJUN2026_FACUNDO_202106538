import axios from "axios";

const client = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const runSearch = (payload) => client.post("/search", payload);
export const compareAlgorithms = (payload) => client.post("/compare", payload);