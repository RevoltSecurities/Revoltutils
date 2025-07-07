import asyncio
from revoltutils import AsyncQueue
from revoltlogger import Logger


async def test_async_queue():
    logger = Logger()
    logger.debug("hello")
    print("[*] Creating AsyncQueue with debug mode ON")

    queue = AsyncQueue(maxsize=3, debug=True)

    await queue.put("task-1")
    await queue.put("task-2")
    await queue.put("task-3")

    print(f"Queue full? {queue.full()}")
    print(f"Queue size: {queue.qsize()}")

    while not queue.empty():
        item = await queue.get()
        print(f"[+] Processed item: {item}")
        queue.task_done()

    await queue.join()
    print("[✓] All tasks completed")


if __name__ == "__main__":
    asyncio.run(test_async_queue())
