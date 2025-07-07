import asyncio
from revoltutils import FileUtils

TEST_FILE = "test_file.txt"
COPY_FILE = "copy_test_file.txt"
JSON_FILE = "test_file.json"
TEST_DIR = "."

async def test_fileutils():
    # Cleanup old test files if exist
    await FileUtils.delete_file(TEST_FILE)
    await FileUtils.delete_file(COPY_FILE)
    await FileUtils.delete_file(JSON_FILE)

    # 1. Create file
    print("[+] Creating test file...")
    await FileUtils.create_file(TEST_FILE)

    # 2. Write content
    await FileUtils.write(TEST_FILE, "This is a test\nSecond line\nThird line\n")
    print("[+] Written to file.")

    # 3. File exists
    exists = await FileUtils.file_exist(TEST_FILE)
    print("[+] File exists:", exists)

    # 4. File exists in directory
    exists_in = await FileUtils.file_exist_in(TEST_FILE, TEST_DIR)
    print("[+] File exists in directory:", exists_in)

    # 5. Read whole file
    content = await FileUtils.read(TEST_FILE)
    print("[+] File content:\n", content.strip())

    # 6. Read lines
    lines = await FileUtils.readlines(TEST_FILE)
    print("[+] Lines:", [line.strip() for line in lines])

    # 7. Stream file
    print("[+] Streaming file:")
    async for line in FileUtils.stream(TEST_FILE):
        print(" >>", line)

    # 8. Read with buffer
    print("[+] Read file with buffer:")
    async for chunk in FileUtils.read_with_buffer(TEST_FILE, 10):
        print(" >>", chunk.strip())

    # 9. Check permissions
    print("[+] Readable:", await FileUtils.readable(TEST_FILE))
    print("[+] Writable:", await FileUtils.writeable(TEST_FILE))
    print("[+] Has permission:", await FileUtils.has_permission(TEST_FILE))

    # 10. Check if file is empty
    print("[+] Is file empty:", await FileUtils.is_empty(TEST_FILE))

    # 11. Is stdin
    print("[+] Is stdin?", FileUtils.is_stdin())

    # 12. Copy file
    await FileUtils.copy_file(TEST_FILE, COPY_FILE)
    print("[+] Copied file to:", COPY_FILE)

    # 13. Write JSON file
    await FileUtils.json_write(JSON_FILE, {"name": "Revolt", "version": 1.0})
    print("[+] Wrote JSON file.")

    # 14. Delete files
    print("[+] Deleted test_file:", await FileUtils.delete_file(TEST_FILE))
    print("[+] Deleted copy_test_file:", await FileUtils.delete_file(COPY_FILE))
    print("[+] Deleted json file:", await FileUtils.delete_file(JSON_FILE))

if __name__ == "__main__":
    asyncio.run(test_fileutils())
