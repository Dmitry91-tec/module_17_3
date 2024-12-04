from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/all_tasks")
async def get_all_tasks():
    pass

@router.get("/tasks_id")
async def task_by_id():
    pass

@router.post("/create")
async def creaty_task():
    pass

@router.put("/update")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass


