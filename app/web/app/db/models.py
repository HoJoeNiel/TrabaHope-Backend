from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from datetime import date

@dataclass
class Job:
    job_id: Optional[int] = None
    job_name: str
    job_desc: str
    job_keywords: List[str]
    job_loc: str
    min_salary: int
    max_salary: int
    employment_type: str
    work_status: str
    posted_at: date
    due_date: Optional[date] = None
    company_id: int

    @classmethod
    def from_db_row(cls, row: Dict[str, Any]) -> "Job":
        return cls(
            job_id=row["job_id"],
            job_name=row["job_name"],
            job_desc=row["job_desc"],
            job_keywords=row["job_keywords"],
            job_loc=row["job_loc"],
            min_salary=row["min_salary"],
            max_salary=row["max_salary"],
            employment_type=row["employment_type"],
            work_status=row["work_status"],
            posted_at=row["posted_at"],
            due_date=row["due_date"],
            company_id=row["company_id"],
        )

    def to_db_dict(self) -> Dict[str, Any]:
        return {
            "job_name": self.job_name,
            "job_desc": self.job_desc,
            "job_keywords": self.job_keywords,
            "job_loc": self.job_loc,
            "min_salary": self.min_salary,
            "max_salary": self.max_salary,
            "employment_type": self.employment_type,
            "work_status": self.work_status,
            "posted_at": self.posted_at,
            "due_date": self.due_date,
            "company_id": self.company_id,
        }