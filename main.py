from fastapi import FastAPI, Body, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import boto3
from botocore.exceptions import ClientError

app = FastAPI()

# 1. Middleware to handle AWS Stage Name (/default)
@app.middleware("http")
async def strip_stage_prefix(request: Request, call_next):
    path = request.scope.get("path", "")
    if path.startswith("/default"):
        request.scope["path"] = path.replace("/default", "", 1)
    response = await call_next(request)
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. DynamoDB Setup
# Key assumption: Partition Key is "id" (Number)
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("tasks")

@app.get("/")
async def root():
    return {"message": "Task Manager API with DynamoDB is running! 🚀"}

@app.get("/tasks")
async def show_tasks():
    response = table.scan()
    return response.get("Items", [])

@app.get("/tasks/{task_id}")
async def task_by_id(task_id: int):
    response = table.get_item(Key={"id": task_id})
    if "Item" in response:
        return response["Item"]
    raise HTTPException(status_code=404, detail="Task Not Found")

@app.post("/tasks/create_task")
async def create_tasks(task = Body()):
    # Ensure ID is an integer for DynamoDB Number type
    if "id" in task:
        task["id"] = int(task["id"])
    table.put_item(Item=task)
    return {"message": "Task Created Successfully.."}

@app.put("/tasks/update_task/{task_id}")
async def update_task(task_id: int, updated_task = Body()):
    # Ensure the ID in the body matches the URL and is a Number
    updated_task["id"] = task_id
    table.put_item(Item=updated_task)
    return {"message": "Task Updated Successfully"}

@app.delete("/tasks/delete_task/{task_id}")
async def delete_task(task_id: int):
    try:
        table.delete_item(Key={"id": task_id})
        return {"message": "Task Successfully Deleted"}
    except ClientError as e:
        return {"error": e.response['Error']['Message']}

handler = Mangum(app)
