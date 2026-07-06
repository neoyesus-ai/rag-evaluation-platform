# RAG Evaluation Platform

> Plataforma para el diseño, ejecución y evaluación reproducible de sistemas Retrieval-Augmented Generation (RAG).

## Descripción

RAG Evaluation Platform es una plataforma modular orientada a la investigación y experimentación con sistemas Retrieval-Augmented Generation (RAG).

Su objetivo es permitir la configuración, ejecución y comparación de diferentes variantes de un pipeline RAG mediante un entorno reproducible, facilitando la evaluación objetiva de cada configuración sobre un mismo corpus documental y un mismo conjunto de preguntas.

El proyecto constituye el Trabajo Fin de Máster del Máster Universitario en Inteligencia Artificial.

---

# Objetivos

- Diseñar una plataforma modular para experimentación con sistemas RAG.
- Comparar distintas configuraciones de recuperación y generación.
- Evaluar automáticamente los resultados mediante métricas objetivas.
- Registrar todos los experimentos utilizando MLflow.
- Visualizar y comparar resultados mediante dashboards.
- Incorporar capacidades de Visual RAG y generación automática de datasets mediante Pixie RAG.

---

# Arquitectura

La plataforma está formada por los siguientes componentes:

```
Frontend
│
├── Project Manager
├── Corpus Manager
├── Configuration Manager
├── Dataset Manager
├── Experiment Manager
└── Dashboard
            │
            ▼
Backend (FastAPI)
            │
            ▼
Worker
            │
            ├── Ingestion Pipeline
            ├── Text RAG
            ├── Visual RAG
            ├── Pixie RAG
            └── Evaluation Engine
            │
            ▼
Infrastructure
├── PostgreSQL
├── ChromaDB
├── Redis
├── Ollama
├── MLflow
└── Metabase
```

---

# Componentes

## Backend

API REST desarrollada con FastAPI.

Responsabilidades:

- Gestión de proyectos
- Gestión de corpus
- Gestión documental
- Configuración de experimentos
- Evaluación
- Exposición de API

---

## Worker

Procesamiento en segundo plano.

Responsabilidades:

- Ingesta documental
- OCR
- Chunking
- Embeddings
- Visual RAG
- Pixie RAG
- Evaluación

---

## Frontend

Interfaz web para la administración de la plataforma.

Permitirá:

- Crear proyectos
- Gestionar corpus
- Configurar experimentos
- Lanzar evaluaciones
- Comparar resultados

---

# Infraestructura

La plataforma utiliza Docker Compose para desplegar los siguientes servicios:

- PostgreSQL
- Redis
- ChromaDB
- Ollama
- MLflow
- Metabase
- Backend
- Worker
- Frontend

---

# Tecnologías

## Backend

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic

## Frontend

- React
- Material UI

## IA

- Ollama
- ChromaDB
- Sentence Transformers
- Pixie RAG

## Evaluación

- MLflow
- Metabase

---

# Estado del proyecto

Actualmente en desarrollo.

Roadmap inicial:

- [x] Diseño de la arquitectura
- [x] Infraestructura Docker
- [ ] Backend
- [ ] Project Manager
- [ ] Corpus Manager
- [ ] Configuration Manager
- [ ] Text RAG
- [ ] Visual RAG
- [ ] Pixie RAG
- [ ] Evaluation Engine
- [ ] Dashboard

---

# Licencia

Pendiente de definir.

---

# Autor

Jesús Ángel Galindo García

Máster Universitario en Inteligencia Artificial

Trabajo Fin de Máster