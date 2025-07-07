from revoltutils import PermissionUtils
import os
import tempfile

def test_user_info():
    print(f"[✓] Current User: {PermissionUtils.current_user()}")
    print(f"[✓] UID: {PermissionUtils.user_id()}")
    print(f"[✓] GID: {PermissionUtils.group_id()}")
    assert isinstance(PermissionUtils.user_id(), int)
    assert isinstance(PermissionUtils.group_id(), int)

def test_root_check():
    print(f"[✓] Is Root: {PermissionUtils.is_root()}")
    assert isinstance(PermissionUtils.is_root(), bool)

def test_user_home():
    home = PermissionUtils.user_home()
    print(f"[✓] Home Dir (current): {home}")
    assert os.path.isdir(home)

    current_user = PermissionUtils.current_user()
    user_home = PermissionUtils.user_home(current_user)
    print(f"[✓] Home Dir ({current_user}): {user_home}")
    assert os.path.isdir(user_home)

def test_file_permissions_and_ownership():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_path = f.name

    try:
        print(f"[✓] Temp File: {temp_path}")
        assert PermissionUtils.is_readable(temp_path)
        assert PermissionUtils.is_writable(temp_path)
        print(f"[✓] File Owner: {PermissionUtils.file_owner(temp_path)}")
        print(f"[✓] File Group: {PermissionUtils.file_group(temp_path)}")

        # Test chmod
        assert PermissionUtils.chmod(temp_path, 0o600)
        assert PermissionUtils.is_readable(temp_path)
        assert not PermissionUtils.is_executable(temp_path)

        # Test has_all_permissions (won't pass unless chmod 700)
        PermissionUtils.chmod(temp_path, 0o700)
        assert PermissionUtils.has_all_permissions(temp_path)

    finally:
        os.remove(temp_path)

def test_chown_skip_if_not_root():
    if not PermissionUtils.is_root():
        print("[!] Skipping chown test (requires root)")
        return

    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_path = f.name

    try:
        # Change to nobody:nogroup (if exists)
        changed = PermissionUtils.chown(temp_path, "nobody", "nogroup")
        print(f"[✓] chown success: {changed}")
        assert changed
    finally:
        os.remove(temp_path)

if __name__ == "__main__":
    print("[*] Running PermissionUtils tests...\n")
    test_user_info()
    test_root_check()
    test_user_home()
    test_file_permissions_and_ownership()
    test_chown_skip_if_not_root()
    print("\n[*] All PermissionUtils tests completed.")
