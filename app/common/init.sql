CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    loc TEXT NOT NULL,
    contact TEXT NOT NULL,
    profile_img_url TEXT,
    resume_file_url TEXT,
    title TEXT,
    user_desc TEXT,
    created_at DATE NOT NULL,
    url TEXT,
    preferred_employment_type TEXT
);


CREATE TABLE IF NOT EXISTS companies (
    company_id SERIAL PRIMARY KEY,
    company_name TEXT NOT NULL UNIQUE,
    company_desc TEXT NOT NULL,
    company_email TEXT NOT NULL UNIQUE,
    company_contact TEXT NOT NULL,
    company_keywords TEXT[] NOT NULL,
    company_loc TEXT NOT NULl,
    company_url TEXT,
    img_url TEXT,
    specialties TEXT[] NOT NULL,
    mission TEXT NOT NULL,
    num_of_employees INT NOT NULL DEFAULT 0,
    date_founded DATE,
    reviews TEXT[] 
);


CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    review_desc TEXT NOT NULL,
    review_stars INT NOT NULL DEFAULT 0,
    review_keywords TEXT[] NOT NULL,
    employee_role TEXT NOT NULL,
    employe_experience TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS jobs (
    job_id SERIAL PRIMARY KEY,
    job_name TEXT NOT NULL,
    job_desc TEXT NOT NULL,
    job_keywords TEXT[] NOT NULL,
    job_loc TEXT NOT NULL,
    max_salary INT NOT NULL,
    min_salary INT NOT NULL,
    employment_type TEXT NOT NULL,
    work_status TEXT NOT NULL,
    posted_at DATE NOT NULL,
    due_date DATE,
    company_id INT NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS applied_jobs (
    job_id INT NOT NULL REFERENCES jobs(job_id) ON DELETE CASCADE,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT applied_job_id PRIMARY KEY (job_id, user_id),
    applied_on DATE NOT NULL,
    updated_on DATE NOT NULL,
    status TEXT NOT NULL,
    feedback TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS company_reviews (
    company_id INT REFERENCES companies(company_id) ON DELETE CASCADE,
    review_id INT REFERENCES reviews(review_id) ON DELETE CASCADE,
    CONSTRAINT company_review_id PRIMARY KEY (company_id, review_id)
);

CREATE TABLE IF NOT EXISTS save_jobs (
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    job_id INT REFERENCES jobs(job_id) ON DELETE CASCADE,
    CONSTRAINT saved_job_id PRIMARY KEY (user_id, job_id)
);