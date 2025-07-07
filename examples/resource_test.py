from revoltutils import ResourceUtils

def test_get_nofile_limit():
    soft, hard = ResourceUtils.get_nofile_limit()
    assert isinstance(soft, int) and isinstance(hard, int)
    print(f"[✓] get_nofile_limit passed: soft={soft}, hard={hard}")

def test_extend_nofile_limit():
    result = ResourceUtils.extend_nofile_limit(65536)
    assert isinstance(result, bool)
    print(f"[✓] extend_nofile_limit passed: result={result}")

def test_get_max_memory():
    soft, hard = ResourceUtils.get_max_memory()
    assert isinstance(soft, int) and isinstance(hard, int)
    print(f"[✓] get_max_memory passed: soft={soft}, hard={hard}")

def test_get_memory_usage_kb():
    usage = ResourceUtils.get_memory_usage_kb()
    assert isinstance(usage, int) and usage > 0
    print(f"[✓] get_memory_usage_kb passed: usage={usage} KB")

def test_get_cpu_time():
    cpu_time = ResourceUtils.get_cpu_time()
    assert isinstance(cpu_time, float) and cpu_time >= 0
    print(f"[✓] get_cpu_time passed: time={cpu_time:.2f} sec")

def test_cpu_cores():
    logical = ResourceUtils.cpu_cores(True)
    assert isinstance(logical, int) and logical >= 1
    print(f"[✓] cpu_cores (logical) passed: cores={logical}")

def test_get_stack_size():
    soft, hard = ResourceUtils.get_stack_size()
    assert isinstance(soft, int) and isinstance(hard, int)
    print(f"[✓] get_stack_size passed: soft={soft}, hard={hard}")

def test_is_high_perf_env():
    result = ResourceUtils.is_high_perf_env(1024)
    assert isinstance(result, bool)
    print(f"[✓] is_high_perf_env passed: high_perf={result}")

def run_all_tests():
    print("[*] Running ResourceUtils tests...\n")
    test_get_nofile_limit()
    test_extend_nofile_limit()
    test_get_max_memory()
    test_get_memory_usage_kb()
    test_get_cpu_time()
    test_cpu_cores()
    test_get_stack_size()
    test_is_high_perf_env()
    print("\n[*] All ResourceUtils tests completed successfully.")

if __name__ == "__main__":
    run_all_tests()
