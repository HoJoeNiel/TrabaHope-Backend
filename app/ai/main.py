from ..common.db import Database
from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Server startup 


  db = Database()
  logger = logging.getLogger("uvicorn")

  await db.initialize_connection()

  yield
  # Server shutdown

  await db.close_all()

app = FastAPI(lifespan=lifespan) 

@app.get("/api/ai/dummy")
async def dummy_server():
  return "Hello, AI World!"