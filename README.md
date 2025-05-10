# TrabaHope-Backend

## Repo Structure

Below is only a guide for the team. It's not meant to be a rigid rule.

```
job-matcher-app/
├── docker-compose.yml
├── .env
├── README.md

├── common/                      # Shared utilities (optional)
│   └── models/                  # Pydantic schemas used across services
│       └── job.py
│       └── resume.py

├── web/                         # Main app microservice
│   ├── Dockerfile
│   ├── .env
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── api/                 # Routes
│   │   ├── db/                  # DB connection, models, pooling
│   │   ├── services/            # Business logic
│   │   ├── schemas/             # Pydantic schemas
│   │   └── core/                # Settings, config
│   └── requirements.txt

├── ai/                          # AI microservice
│   ├── Dockerfile
│   ├── .env
│   ├── app/
│   │   ├── main.py              # FastAPI entry
│   │   ├── scorer/              # Vector scoring logic
│   │   ├── model/               # Embedding model loading (e.g. all-MiniLM)
│   │   ├── db/                  # Optional: if AI needs its own DB
│   │   └── schemas/             # API request/response schemas
│   └── requirements.txt

```
