from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

TASKS = [
 {"id":1,"title":"Learn FastAPI","description":"Build APIs","completed":False,"priority":"high"},
 {"id":2,"title":"Study Python","description":"Practice coding","completed":False,"priority":"medium"},
 {"id":3,"title":"Workout","description":"Gym session","completed":True,"priority":"low"}
]

@app.get("/")
async def root():
    return {"message": "API is running!"}

@app.get("/tasks")
async def show_tasks():
    return TASKS

@app.get("/tasks/{task_id}")
async def task_by_id(task_id: int):
    for task in TASKS:
        if int(task.get("id")) == task_id:
            return task
    return {"error": "Task Not Found"}

@app.post("/tasks/create_task")
async def create_tasks(create_task = Body()):
    TASKS.append(create_task)
    return "Task Created Successfully.."

@app.put("/tasks/update_task/{task_id}")
async def update_task(task_id: int, updated_task = Body()):
    for i in range(len(TASKS)):
        if TASKS[i].get("id") == task_id:
            TASKS[i] = updated_task
            return "Task Updated Successfully"
    return "Could not Update Task"

@app.delete("/tasks/delete_task/{task_id}")
async def delete_task(task_id: int):
    for i in range(len(TASKS)):
        if TASKS[i].get("id") == task_id:
            TASKS.pop(i)
            return "Task Successfully Deleted"
    return "Task Not Deleted"
