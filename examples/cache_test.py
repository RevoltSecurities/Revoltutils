import asyncio
from revoltutils import AsyncDiskCache

async def test_cache():
    print("[*] Starting cache tests...")
    async with AsyncDiskCache(directory=".cache-test") as cache:
        
        # Test set and get
        await cache.set("username", "revoltuser")
        value = await cache.get("username")
        print(f"[+] Retrieved value for 'username': {value}")

        # Test add (should fail if key already exists)
        added = await cache.add("username", "newuser")
        print(f"[+] Tried to add duplicate key 'username': {added}")

        # Test contains
        exists = await cache.contains("username")
        print(f"[+] 'username' in cache: {exists}")

        # Test size
        size = await cache.size()
        print(f"[+] Cache size: {size}")

        # Test delete
        await cache.delete("username")
        exists_after_delete = await cache.contains("username")
        print(f"[+] 'username' exists after delete: {exists_after_delete}")

        # Test iterkeys
        await cache.set("a", 1)
        await cache.set("b", 2)
        print("[+] Keys in cache:")
        async for key in cache.iterkeys():
            print(f"    - {key}")

        # Test clear
        await cache.clear()
        size_after_clear = await cache.size()
        print(f"[+] Cache size after clear: {size_after_clear}")

if __name__ == "__main__":
    asyncio.run(test_cache())
