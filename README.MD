# CRUD Python FastAPI

Este repositorio contiene un proyecto de ejemplo que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) utilizando **Python** y el framework **FastAPI**.

## ¿Qué es FastAPI?

FastAPI es un framework moderno y rápido para construir APIs con Python, basado en las anotaciones de tipo estándar de Python 3.6+.

## ¿Qué incluye este repositorio?

- **Endpoints CRUD**: Permiten crear, leer, actualizar y eliminar registros.
- **Estructura modular**: Código organizado en módulos para facilitar el mantenimiento.
- **Documentación automática**: Acceso a la documentación interactiva de la API usando Swagger UI.

## ¿Cómo ejecutar el proyecto?

1. Clona el repositorio.
2. Inicializa el servidor de Docker para acceder a la base de datos.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta el servidor con `uvicorn main:app --reload --port 5000`.
4. Accede a la documentación en `http://localhost:5000/docs`.

## Objetivo

El objetivo de este proyecto es servir como base para aprender y desarrollar APIs RESTful usando FastAPI.
