import asyncio
from revoltutils import FolderUtils

TEST_FOLDER = "test_dir"
RENAMED_FOLDER = "renamed_dir"
FILE_INSIDE = "test_dir/file1.txt"

async def test_folderutils():
    print("[+] Cleanup if old test folders exist...")
    await FolderUtils.delete_folder(TEST_FOLDER)
    await FolderUtils.delete_folder(RENAMED_FOLDER)

    # 1. Create folder
    await FolderUtils.create_folder(TEST_FOLDER)
    print("[+] Folder created:", TEST_FOLDER)

    # 2. Check if folder exists
    exists = await FolderUtils.folder_exists(TEST_FOLDER)
    print("[+] Folder exists:", exists)

    # 3. Folder readable/writable/permissions
    print("[+] Folder readable:", await FolderUtils.folder_readable(TEST_FOLDER))
    print("[+] Folder writable:", await FolderUtils.folder_writable(TEST_FOLDER))
    print("[+] Folder has full permission:", await FolderUtils.has_permission(TEST_FOLDER))

    # 4. Create file inside it
    with open(FILE_INSIDE, "w") as f:
        f.write("Hello World")

    # 5. List files
    files = await FolderUtils.list_files(TEST_FOLDER)
    print("[+] Files in folder:", files)

    # 6. List directories (should be empty since only a file exists)
    dirs = await FolderUtils.list_dirs(TEST_FOLDER)
    print("[+] Sub-directories:", dirs)

    # 7. Check if folder is empty
    print("[+] Is empty:", await FolderUtils.is_empty(TEST_FOLDER))

    # 8. List all (files and folders)
    all_items = await FolderUtils.list_all(TEST_FOLDER)
    print("[+] All contents:", all_items)

    # 9. Rename folder
    renamed = await FolderUtils.rename_folder(TEST_FOLDER, RENAMED_FOLDER)
    print("[+] Renamed folder:", renamed)

    # 10. Copy folder
    copied = await FolderUtils.copy_folder(RENAMED_FOLDER, TEST_FOLDER)
    print("[+] Folder copied back:", copied)

    # 11. Delete folders
    deleted1 = await FolderUtils.delete_folder(TEST_FOLDER)
    deleted2 = await FolderUtils.delete_folder(RENAMED_FOLDER)
    print("[+] Deleted test_dir:", deleted1)
    print("[+] Deleted renamed_dir:", deleted2)

if __name__ == "__main__":
    asyncio.run(test_folderutils())
