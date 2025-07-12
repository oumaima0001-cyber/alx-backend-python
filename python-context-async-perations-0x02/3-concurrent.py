#!/usr/bin/env python3
import asyncio
import aiosqlite

DB_NAME = 'users.db'

async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()
        await cursor.close()
        print("All Users:", users)
        return users

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        older_users = await cursor.fetchall()
        await cursor.close()
        print("Users over 40:", older_users)
        return older_users

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

# ✅ Run the concurrent fetch
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
