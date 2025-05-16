import asyncpg
from typing import AsyncGenerator, Optional, Dict, Any

class Database:
    def __init__(self):
        self.pool: Optional[asyncpg.Pool] = None

    async def initialize_connection(self):
        self.pool = await asyncpg.create_pool(
            "postgresql://user:password@localhost/dbname" #tentative ilalagay pa yung totoong pg
        )

    async def fetch_row(self, query: str, *args) -> Dict[str, Any]:
        if not self.pool:
            raise RuntimeError("Database connection not initialized")
        async with self.pool.acquire() as conn:
            return await conn.fetchrow(query, *args)

    async def close_all(self):
        if self.pool:
            await self.pool.close()