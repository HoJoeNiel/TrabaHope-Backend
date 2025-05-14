from typing import List, Optional
from datetime import date
from pydantic import BaseModel, conlist
from enum import Enum

class JobBase(BaseModel):
    job_name: str
    job_description: str
    job_keywords: List[str]
    job_salary_range: conlist(int, min_items=2, max_items=2) # type: ignore
    job_employment_type: str
    work_status: str
    job_location: str
    due_date: date
    company_id: int 

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    job_name: Optional[str] = None
    job_description: Optional[str] = None
    job_keywords: Optional[List[str]] = None
    job_salary_range: Optional[conlist(int, min_items=2, max_items=2)] = None # type: ignore
    job_employment_type: Optional[str] = None
    work_status: Optional[str] = None
    job_location: Optional[str] = None
    due_date: Optional[date] = None
    company_id: Optional[int] = None

class job(JobBase):
    job_id: int
    posted_at: date
    is_saved: Optional[bool] = None

    class Config:
        orm_mode = True

        