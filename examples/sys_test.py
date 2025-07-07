from revoltutils import SystemUtils

def test_os_info():
    assert isinstance(SystemUtils.os_name(), str)
    assert isinstance(SystemUtils.os_version(), str)
    assert isinstance(SystemUtils.os_release(), str)
    print("[✓] OS info methods passed")

def test_arch_and_python_version():
    assert isinstance(SystemUtils.architecture(), str)
    assert isinstance(SystemUtils.python_version(), str)
    print("[✓] Architecture & Python version methods passed")

def test_cpu_and_memory():
    assert isinstance(SystemUtils.cpu_count(), int)
    memory = SystemUtils.memory_info()
    assert isinstance(memory, dict) and "total" in memory
    print("[✓] CPU & memory info passed")

def test_disk_usage():
    usage = SystemUtils.disk_usage("/")
    assert isinstance(usage, dict) and "total" in usage
    print("[✓] Disk usage passed")

def test_hostname_user():
    assert isinstance(SystemUtils.hostname(), str)
    assert isinstance(SystemUtils.current_user(), str)
    print("[✓] Hostname and current user passed")

def test_uptime():
    assert SystemUtils.uptime_seconds() > 0
    assert isinstance(SystemUtils.uptime_human(), str)
    print("[✓] Uptime info passed")

def test_platform_checks():
    assert isinstance(SystemUtils.is_linux(), bool)
    assert isinstance(SystemUtils.is_windows(), bool)
    assert isinstance(SystemUtils.is_macos(), bool)
    print("[✓] Platform checks passed")

def test_time():
    assert isinstance(SystemUtils.timezone_name(), str)
    assert isinstance(SystemUtils.local_datetime(), object)
    assert isinstance(SystemUtils.utc_datetime(), object)
    print("[✓] Time methods passed")

def test_load_and_reboot():
    load = SystemUtils.load_average()
    assert load is None or isinstance(load, tuple)
    assert isinstance(SystemUtils.is_reboot_required(), bool)
    print("[✓] Load average and reboot check passed")

def test_processes():
    processes = SystemUtils.running_processes()
    assert isinstance(processes, list)
    assert isinstance(SystemUtils.is_process_running("python"), bool)
    print("[✓] Process listing and check passed")

def test_terminal_and_arch():
    assert isinstance(SystemUtils.supports_color(), bool)
    assert isinstance(SystemUtils.is_64bit(), bool)
    print("[✓] Terminal support and 64-bit check passed")

def run_all_tests():
    print("[*] Running SystemUtils tests...\n")
    test_os_info()
    test_arch_and_python_version()
    test_cpu_and_memory()
    test_disk_usage()
    test_hostname_user()
    test_uptime()
    test_platform_checks()
    test_time()
    test_load_and_reboot()
    test_processes()
    test_terminal_and_arch()
    print("\n[*] All SystemUtils tests completed successfully.")

if __name__ == "__main__":
    run_all_tests()
