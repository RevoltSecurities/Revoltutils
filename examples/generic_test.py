from revoltutils import GenericUtils


def test_string_to_string_list():
    assert GenericUtils.string_to_string_list("a,b,c") == ["a", "b", "c"]
    assert GenericUtils.string_to_string_list(["x", " y "]) == ["x", "y"]
    assert GenericUtils.string_to_string_list("a|b|c", delimiter="|") == ["a", "b", "c"]
    print("[+] string_to_string_list passed")


def test_string_to_int_list():
    assert GenericUtils.string_to_int_list("1,2,5-7") == [1, 2, 5, 6, 7]
    assert GenericUtils.string_to_int_list(["3", 4, "5"]) == [3, 4, 5]
    assert GenericUtils.string_to_int_list("10-12,15") == [10, 11, 12, 15]
    print("[+] string_to_int_list passed")


def test_expand_range():
    assert GenericUtils.expand_range("100-102") == [100, 101, 102]
    assert GenericUtils.expand_range("1,3-5") == [1, 3, 4, 5]
    print("[+] expand_range passed")


def test_is_numeric():
    assert GenericUtils.is_numeric("123")
    assert GenericUtils.is_numeric("-10")
    assert GenericUtils.is_numeric("3.14")
    assert not GenericUtils.is_numeric("abc")
    print("[+] is_numeric passed")


def test_flatten():
    assert GenericUtils.flatten([1, [2, 3], (4, [5, 6])]) == [1, 2, 3, 4, 5, 6]
    print("[+] flatten passed")


def test_unique():
    assert GenericUtils.unique([1, 2, 2, 3, 1]) == [1, 2, 3]
    print("[+] unique passed")


def test_chunk_list():
    assert GenericUtils.chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    print("[+] chunk_list passed")


def test_safe_cast():
    assert GenericUtils.safe_cast("123", int) == 123
    assert GenericUtils.safe_cast("abc", int, default=0) == 0
    print("[+] safe_cast passed")


def test_normalize_list_str():
    assert GenericUtils.normalize_list_str([1, " two ", 3.5]) == ["1", "two", "3.5"]
    print("[+] normalize_list_str passed")


def test_validate_range():
    assert GenericUtils.validate_range("100-200,80,443")
    assert not GenericUtils.validate_range("abc,123")
    print("[+] validate_range passed")


if __name__ == "__main__":
    test_string_to_string_list()
    test_string_to_int_list()
    test_expand_range()
    test_is_numeric()
    test_flatten()
    test_unique()
    test_chunk_list()
    test_safe_cast()
    test_normalize_list_str()
    test_validate_range()
    print("[*] All GenericUtils tests passed.")
