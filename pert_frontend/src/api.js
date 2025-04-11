// src/api.js

import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000", // adresa backenda
});


// API pozivi
export const getProjects = () => api.get("/projects");
export const getProjectPert = (projectId) => api.get(`/tasks/projects/${projectId}/pert`)
export const createTask = (data) => api.post("/tasks", data);
export const createProject = (data) => api.post("/projects", data);

export default api;
