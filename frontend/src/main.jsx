import React from "react";
import { createRoot } from "react-dom/client";

function App() {
  return (
    <main style={{ fontFamily: "Arial", padding: "40px" }}>
      <h1>RAG Evaluation Platform</h1>
      <p>Plataforma de evaluación reproducible de sistemas RAG.</p>

      <h2>Servicios</h2>
      <ul>
        <li><a href="http://51.83.6.61:8000/docs" target="_blank">Backend API</a></li>
        <li><a href="http://51.83.6.61:5000" target="_blank">MLflow</a></li>
        <li><a href="http://51.83.6.61:3001" target="_blank">Metabase</a></li>
        <li><a href="http://51.83.6.61:8001" target="_blank">ChromaDB</a></li>
        <li><a href="http://51.83.6.61:11435" target="_blank">Ollama</a></li>
      </ul>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);