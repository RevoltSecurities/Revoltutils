from revoltutils import RandomUtils
import string

def test_uuid4():
    uuid_val = RandomUtils.uuid4()
    assert isinstance(uuid_val, str) and len(uuid_val) == 36
    print("[✓] uuid4 passed")

def test_random_int():
    val = RandomUtils.random_int(10, 20)
    assert 10 <= val <= 20
    print("[✓] random_int passed")

def test_random_float():
    val = RandomUtils.random_float(1.5, 3.5)
    assert 1.5 <= val <= 3.5
    print("[✓] random_float passed")

def test_random_choice():
    val = RandomUtils.random_choice(["a", "b", "c"])
    assert val in ["a", "b", "c"]
    print("[✓] random_choice passed")

def test_random_string():
    s = RandomUtils.random_string(16)
    assert len(s) == 16
    assert all(c in string.ascii_letters + string.digits for c in s)
    print("[✓] random_string passed")

def test_random_lowercase():
    s = RandomUtils.random_lowercase(10)
    assert len(s) == 10 and s.islower()
    print("[✓] random_lowercase passed")

def test_random_uppercase():
    s = RandomUtils.random_uppercase(10)
    assert len(s) == 10 and s.isupper()
    print("[✓] random_uppercase passed")

def test_random_hex():
    h = RandomUtils.random_hex(16)
    assert len(h) == 16 and all(c in string.hexdigits for c in h)
    print("[✓] random_hex passed")

def test_random_bytes():
    b = RandomUtils.random_bytes(8)
    assert isinstance(b, bytes) and len(b) == 8
    print("[✓] random_bytes passed")

def test_secure_token():
    t = RandomUtils.secure_token(16)
    assert isinstance(t, str)
    print("[✓] secure_token passed")

def test_random_bool():
    assert RandomUtils.random_bool() in [True, False]
    print("[✓] random_bool passed")

def test_random_password():
    pwd = RandomUtils.random_password(14, use_symbols=True)
    assert len(pwd) == 14
    print("[✓] random_password passed")


def main():
    print("[*] Running RandomUtils tests...\n")
    test_uuid4()
    test_random_int()
    test_random_float()
    test_random_choice()
    test_random_string()
    test_random_lowercase()
    test_random_uppercase()
    test_random_hex()
    test_random_bytes()
    test_secure_token()
    test_random_bool()
    test_random_password()
    print("\n[*] All RandomUtils tests completed successfully.")

if __name__ == "__main__":
    main()
