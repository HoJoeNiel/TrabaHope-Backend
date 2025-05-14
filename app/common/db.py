from ..common.logging import logger

import asyncio
import asyncpg

class Database:


	# we use a pool so that we dont have to establish connection
	# whenever we do something with our db.

	# should we use a single persistent connection, we risk the connection
	# from being overwhelmed by requests.

	def __init__(self, database="task_scheduler", host="localhost", user="yisa", password="aye", port="5432"):
		self.pool = None # the connection pool
		self.datbase = database
		self.host = host
		self.user = user
		self.password = password
		self.port = port
		
	async def initialize_connection(self, max_retries=5, base_delay=0.5): 
		# initializes the connection pool

		for attempt in range(1, max_retries + 1): # backoff strategy
			try:
				self.pool = await asyncpg.create_pool(
					database=self.datbase,
					host=self.host,
					user=self.user,
					password=self.password,
					port=self.port
					)
		
				logger.info("Database initialized successfully.")
				return
			
			except Exception as e:
				logger.warning(f"Database initialization failed (attempt {attempt}): {e}")

				if attempt < max_retries:
					base_delay = min(6.0, base_delay * (2 ** (attempt - 1)))  # Exponential backoff
					logger.warning(f"Retrying in {base_delay} seconds.")
					await asyncio.sleep(base_delay)

				else: # no more retries
					logger.error("Max retries reached. Could not connect to database.")
					raise


	async def get_connection(self): # get a connection from the pool
		if self.pool is None:
			raise Exception("Database not initialized. Call Database.initialize() first.")
		
		return await self.pool.acquire()
	

	async def release_connection(self, conn): # release the 'conn' connection
		await self.pool.release(conn)


	async def close_all(self): # closes all connection
		if self.pool is None:
			await self.pool.close()
