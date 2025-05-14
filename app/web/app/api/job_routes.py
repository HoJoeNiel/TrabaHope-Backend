from fastapi import APIRouter, Depends, HTTPException, Path
from schema.job import JobCreate, JobResponse, JobUpdate
from services.job_service import create_job, update_job, delete_job
from db.database import Database
from typing import Optional

router = APIRouter(prefix="/jobs", tags=["Jobs"])

async def get_db():
    db = Database()
    await db.initialize_connection()
    try:
        yield db
    finally:
        await db.close_all()

@router.post("/", response_model=JobResponse)
async def post_job(job: JobCreate, db: Database = Depends(get_db)):
    return await create_job(job, db)

@router.put("/{job_id}", response_model=JobResponse)
async def put_job(
    job_id: int, 
    job_update: JobUpdate, 
    db: Database = Depends(get_db)
):
    updated_job = await update_job(job_id, job_update, db)
    if not updated_job:
        raise HTTPException(status_code=404, detail="Job not found or no fields provided")
    return updated_job

@router.delete("/{job_id}", status_code=204)
async def delete_job_endpoint(
    job_id: int = Path(..., description="ID of the Job to delete"),
    db: Database = Depends(get_db)
):
    deleted = await delete_job(job_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Job not found")