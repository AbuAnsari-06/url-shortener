import asyncio
import os

from dotenv import load_dotenv
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()

async def main():
    engine = create_async_engine(
        os.environ["DATABASE_URL"],
        pool_pre_ping=True,
        connect_args={"statement_cache_size": 0},
    )

    async with engine.connect() as conn:
        version = (await conn.execute(text("select version()"))).scalar()
        print("CONNECTED:" , version)
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())