from db.models import Job
from db.database import Database
from schema.job import JobCreate, JobResponse, JobUpdate
from typing import Optional

async def create_job(job_data: JobCreate, db: Database) -> Job:
    query = """
    INSERT INTO jobs (
        job_name, job_desc, job_keywords, job_loc,
        min_salary, max_salary, employment_type,
        work_status, posted_at, due_date, company_id
    ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
    RETURNING job_id, *
    """
    db_row = await db.fetch_row(
        query,
        job_data.job_name,
        job_data.job_desc,
        job_data.job_keywords,
        job_data.job_loc,
        job_data.min_salary,
        job_data.max_salary,
        job_data.employment_type,
        job_data.work_status,
        job_data.posted_at,
        job_data.due_date,
        job_data.company_id,
    )
    return Job.from_db_row(db_row)

async def update_job(job_id: int, job_update: JobUpdate, db: Database) -> Optional[Job]:
    updates = job_update.model_dump(exclude_unset=True)
    if not updates:
        return None

    set_clause = ", ".join([f"{field} = ${i+1}" for i, field in enumerate(updates.keys())])
    query = f"""
    UPDATE jobs
    SET {set_clause}
    WHERE job_id = ${len(updates) + 1}
    RETURNING job_id, *
    """
    
    db_row = await db.fetch_row(
        query,
        *updates.values(),
        job_id,
    )
    return Job.from_db_row(db_row) if db_row else None

async def delete_job(job_id: int, db: Database) -> bool:
    result = await db.execute(
        "DELETE FROM jobs WHERE job_id = $1",
        job_id
    )
    return "DELETE 1" in result  # Returns True if deleted, False if not found