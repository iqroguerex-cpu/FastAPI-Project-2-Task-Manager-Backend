# ⚡ TaskFlow API (FastAPI Backend)

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

This is the high-performance RESTful API powering the TaskFlow ecosystem. Built with **FastAPI**, it handles task persistence, status updates, and priority management with minimal latency.

## 🔗 Live API Resources
- **Base URL:** [https://fastapi-project-2-task-manager-backend.onrender.com](https://fastapi-project-2-task-manager-backend.onrender.com)
- **Interactive Docs (Swagger):** [Click here to test endpoints](https://fastapi-project-2-task-manager-backend.onrender.com/docs)

---

## 🛠️ Features
- **RESTful Architecture:** Clean separation of concerns using GET, POST, PUT, and DELETE.
- **Auto-Documentation:** Interactive Swagger UI and ReDoc generated automatically.
- **CORS Enabled:** Configured to securely communicate with the Streamlit frontend.
- **In-Memory Data:** Lightweight and fast (Current version resets on server restart).



## 📡 API Endpoints
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/tasks` | List all tasks |
| `GET` | `/tasks/{id}` | Get specific task details |
| `POST` | `/tasks/create_task` | Add a new task object |
| `PUT` | `/tasks/update_task/{id}` | Modify task status or priority |
| `DELETE` | `/tasks/delete_task/{id}` | Remove a task by ID |

## 🚀 Local Setup
1. Clone the repo.
2. Install requirements: `pip install -r requirements.txt`.
3. Run the server: `uvicorn main:app --reload`.

---

**Author:** [Chinmay V Chatradamath](https://github.com/iqroguerex-cpu)
