# ⚙️ TaskFlow API — Serverless Task Manager (AWS + S3 Deployment)

<p align="center">

[![Live API](https://img.shields.io/badge/API-Live-success?style=for-the-badge)](https://89djj7pnai.execute-api.ap-south-1.amazonaws.com/default/)
![AWS](https://img.shields.io/badge/AWS-Serverless-orange?style=for-the-badge\&logo=amazonaws)
![Lambda](https://img.shields.io/badge/AWS-Lambda-yellow?style=for-the-badge\&logo=awslambda)
![DynamoDB](https://img.shields.io/badge/Database-DynamoDB-blue?style=for-the-badge\&logo=amazondynamodb)
![API Gateway](https://img.shields.io/badge/API-Gateway-green?style=for-the-badge)
![S3](https://img.shields.io/badge/Deployment-S3-blue?style=for-the-badge\&logo=amazons3)

</p>

---

## 🚀 Overview

**TaskFlow API** is a fully **serverless backend** built using **FastAPI deployed on AWS Lambda**, integrated with **API Gateway and DynamoDB**.

The application is packaged and deployed via **Amazon S3**, enabling scalable and production-ready deployment.

---

## 🌐 Live API

👉 https://89djj7pnai.execute-api.ap-south-1.amazonaws.com/default/

---

## ✨ Features

* 📋 Get all tasks
* 🔎 Get task by ID
* ➕ Create tasks
* ✏️ Update tasks
* ❌ Delete tasks
* ⚡ Fast execution using AWS Lambda
* ☁️ Fully scalable serverless architecture
* 📦 Deployment via Amazon S3

---

## 🛠 Tech Stack

### Backend

* FastAPI
* Mangum (ASGI → Lambda adapter)
* Boto3

### Cloud Infrastructure

* AWS Lambda
* API Gateway
* DynamoDB
* Amazon S3 (deployment package storage)

---

## 📂 Project Structure

```bash id="tfaws1"
taskflow-api
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Deployment Architecture

```bash id="tfaws2"
Client → API Gateway → Lambda (FastAPI via Mangum) → DynamoDB
                           ↑
                     Code stored in S3
```

---

## 📦 Deployment (S3 + Lambda)

1. Package your application:

```bash id="tfaws3"
zip -r function.zip .
```

2. Upload to **Amazon S3**

3. Create / update Lambda function using:

* S3 bucket
* Uploaded ZIP file

4. Configure:

* Runtime: Python
* Handler: `main.handler`

5. Connect Lambda to **API Gateway**

---

## 📡 API Endpoints

| Method | Endpoint                       | Description    |
| ------ | ------------------------------ | -------------- |
| GET    | `/tasks`                       | Get all tasks  |
| GET    | `/tasks/{task_id}`             | Get task by ID |
| POST   | `/tasks/create_task`           | Create task    |
| PUT    | `/tasks/update_task/{task_id}` | Update task    |
| DELETE | `/tasks/delete_task/{task_id}` | Delete task    |

---

## 🎯 Example Request

```json id="tfaws4"
{
  "id": 1,
  "title": "Build TaskFlow",
  "description": "Deploy serverless backend",
  "priority": "high",
  "completed": false
}
```

---

## ☁️ AWS Configuration

* **Region:** ap-south-1
* **DynamoDB Table:** tasks
* **Partition Key:** id (Number)
* **API Gateway Stage:** `/default`

---

## 🔧 Key Implementation Details

* Middleware handles `/default` stage prefix
* CORS enabled for frontend integration
* Mangum adapts FastAPI for Lambda execution
* DynamoDB used for persistent storage

---

## 🌐 Frontend Application

👉 https://staging.d3b7v2fqtuw73g.amplifyapp.com/

---

## 🔮 Future Improvements

* 🔐 Authentication (AWS Cognito / JWT)
* 📊 Task analytics dashboard
* 📅 Due dates & scheduling
* 🔍 Search & filtering
* 📁 File attachments

---

## 👨‍💻 Author

**Chinmay V Chatradamath**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
