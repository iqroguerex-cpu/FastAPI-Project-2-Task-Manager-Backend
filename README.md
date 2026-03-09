# ⚡ TaskFlow API — FastAPI Backend

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge\&logo=render\&logoColor=white)](https://render.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()

A **high-performance REST API** built with **FastAPI** that powers the **TaskFlow productivity application**.

The API manages tasks, priorities, and completion states while providing a **clean, scalable backend architecture**.

---

# 🌐 Live API

**Base URL**

https://fastapi-project-2-task-manager-backend.onrender.com

**Interactive API Documentation**

Swagger UI
https://fastapi-project-2-task-manager-backend.onrender.com/docs

ReDoc
https://fastapi-project-2-task-manager-backend.onrender.com/redoc

---

# 🚀 Features

* ⚡ **FastAPI Performance** — built on Starlette and Pydantic
* 📚 **Auto-Generated Documentation** — Swagger & ReDoc
* 🔄 **Full CRUD Operations**
* 🌐 **CORS Enabled** for frontend communication
* 🧠 **Priority Management** (Low / Medium / High)
* 🟢 **Task Status Tracking**
* 🧩 **Lightweight In-Memory Storage**

> Note: Data resets on server restart in the current version.

---

# 🏗 Architecture

```
Client (Streamlit Frontend)
        │
        ▼
   FastAPI Backend
        │
        ▼
   In-Memory Task Store
```

The API is designed to be easily extendable with:

* PostgreSQL
* MongoDB
* Redis caching
* Authentication systems

---

# 📡 API Endpoints

| Method   | Endpoint                  | Description            |
| -------- | ------------------------- | ---------------------- |
| `GET`    | `/tasks`                  | Retrieve all tasks     |
| `GET`    | `/tasks/{id}`             | Retrieve a single task |
| `POST`   | `/tasks/create_task`      | Create a new task      |
| `PUT`    | `/tasks/update_task/{id}` | Update task details    |
| `DELETE` | `/tasks/delete_task/{id}` | Delete a task          |

---

# 📥 Example Request

### Create Task

```
POST /tasks/create_task
```

Request Body

```json
{
  "id": 1,
  "title": "Finish FastAPI project",
  "description": "Build task manager API",
  "completed": false,
  "priority": "high"
}
```

Response

```json
"Task Created Successfully"
```

---

# 📂 Project Structure

```
taskflow-api
│
├── task_api.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Development

Clone the repository

```
git clone https://github.com/iqroguerex-cpu/fastapi-project-2-task-manager-backend
```

Navigate into the project

```
cd fastapi-project-2-task-manager-backend
```

Install dependencies

```
pip install -r requirements.txt
```

Run the API server

```
uvicorn task_api:app --reload --port 8002
```

Access documentation

```
http://127.0.0.1:8002/docs
```

---

# ☁️ Deployment

The API is deployed using **Render**.

Render automatically:

* pulls from GitHub
* installs dependencies
* runs the FastAPI server

Start command used in deployment:

```
uvicorn task_api:app --host 0.0.0.0 --port $PORT
```

---

# 🖥 Frontend

The **TaskFlow frontend dashboard** is built using **Streamlit**.

Frontend Repository
https://github.com/iqroguerex-cpu/fastapi-project-2-task-manager-frontend

---

# 📄 License

This project is released under the **MIT License**.

---

# 👨‍💻 Author

**Chinmay V Chatradamath**

GitHub
https://github.com/iqroguerex-cpu

---

⭐ If you found this project useful, consider **starring the repository**.
