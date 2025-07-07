from revoltutils import OSUtils

def test_os_detection():
    print(f"[✓] OS Name: {OSUtils.os_name()}")
    print(f"[✓] Version: {OSUtils.os_version()}")
    print(f"[✓] Platform: {OSUtils.platform_info()}")
    print(f"[✓] Architecture: {OSUtils.architecture()}")

    assert OSUtils.is_linux() or OSUtils.is_windows() or OSUtils.is_macos()

def test_hostname_and_user():
    print(f"[✓] Hostname: {OSUtils.hostname()}")
    print(f"[✓] User: {OSUtils.current_user()}")
    assert OSUtils.hostname()
    assert OSUtils.current_user()

def test_process_ids():
    print(f"[✓] PID: {OSUtils.current_process_id()}")
    print(f"[✓] PPID: {OSUtils.parent_process_id()}")
    assert isinstance(OSUtils.current_process_id(), int)
    assert isinstance(OSUtils.parent_process_id(), int)

def test_env_vars():
    key = "TEST_ENV_VAR"
    value = "1234"
    OSUtils.set_env(key, value)
    result = OSUtils.env(key)
    print(f"[✓] Env Var Set/Get: {key}={result}")
    assert result == value

def test_directory_operations():
    original_dir = OSUtils.cwd()
    print(f"[✓] Current Directory: {original_dir}")
    OSUtils.change_dir("/")
    assert OSUtils.cwd() == "/"
    OSUtils.change_dir(original_dir)
    assert OSUtils.cwd() == original_dir
    print("[✓] Directory change test passed")

def test_uptime():
    uptime = OSUtils.uptime_seconds()
    if uptime is not None:
        print(f"[✓] System Uptime (seconds): {uptime:.2f}")
        assert uptime > 0
    else:
        print("[!] Uptime not implemented for this OS")

if __name__ == "__main__":
    print("[*] Running OSUtils tests...\n")
    test_os_detection()
    test_hostname_and_user()
    test_process_ids()
    test_env_vars()
    test_directory_operations()
    test_uptime()
    print("\n[*] All tests completed.")
