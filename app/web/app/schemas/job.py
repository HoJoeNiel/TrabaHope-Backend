from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import date

class JobBase(BaseModel):
    job_name: str = Field(..., min_length=1)
    job_desc: str = Field(..., min_length=1)
    job_keywords: List[str] = Field(..., min_items=1)
    job_loc: str = Field(...)
    min_salary: int = Field(..., gt=0)
    max_salary: int = Field(..., gt=0)
    employment_type: str = Field(..., max_length=50)
    work_status: str = Field(...)
    posted_at: date = Field(...)
    due_date: Optional[date] = None
    company_id: int = Field(..., gt=0)

    @field_validator("max_salary")
    @classmethod
    def validate_salary(cls, v, values):
        if "min_salary" in values and v < values["min_salary"]:
            raise ValueError("Max salary must be >= min salary")
        return v

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    job_id: int

class JobUpdate(BaseModel):
    job_name: Optional[str] = Field(None, min_length=1)
    job_desc: Optional[str] = Field(None, min_length=1)
    job_keywords: Optional[List[str]] = Field(None, min_items=1)
    job_loc: Optional[str] = None
    min_salary: Optional[int] = Field(None, gt=0)
    max_salary: Optional[int] = Field(None, gt=0)
    employment_type: Optional[str] = Field(None, max_length=50)
    work_status: Optional[str] = None
    due_date: Optional[date] = None

    @field_validator("max_salary")
    @classmethod
    def validate_salary(cls, v, values):
        if v and "min_salary" in values and values["min_salary"] and v < values["min_salary"]:
            raise ValueError("Max salary must be >= min salary")
        return v