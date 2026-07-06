from fastapi import FastAPI

app = FastAPI(
    title="RAG Evaluation Platform",
    description="API principal para la plataforma de evaluación de sistemas RAG",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "RAG Evaluation Platform",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/architecture")
def architecture():
    return {
        "core_concept": "Experiment",
        "formula": "Corpus + Configuration + Dataset = Experiment",
        "components": [
            "Project Manager",
            "Corpus Manager",
            "Document Manager",
            "Configuration Manager",
            "Pixie RAG",
            "Text RAG",
            "Visual RAG",
            "Hybrid RAG",
            "Evaluation Engine",
            "MLflow",
            "Metabase",
        ],
    }