from revoltutils import UrlUtils


def test_ensure_scheme():
    assert UrlUtils.ensure_scheme("example.com") == "https://example.com"
    assert UrlUtils.ensure_scheme("http://example.com") == "http://example.com"
    print("[✓] ensure_scheme passed")


def test_add_ports():
    urls = UrlUtils.add_ports("https://example.com", [80, 8080])
    assert "https://example.com:80" in urls
    assert "https://example.com:8080" in urls
    print("[✓] add_ports passed")


def test_add_paths():
    urls = UrlUtils.add_paths("https://example.com", ["admin", "/login"])
    assert "https://example.com/admin" in urls
    assert "https://example.com/login" in urls
    print("[✓] add_paths passed")


def test_expand_url():
    urls = UrlUtils.expand_url("example.com", ports=[80], paths=["admin", "dashboard"])
    assert "https://example.com:80/admin" in urls
    assert "https://example.com:80/dashboard" in urls
    print("[✓] expand_url passed")


def test_parse_url_parts():
    parsed = UrlUtils.parse_url_parts("https://user:pass@example.com:443/path?query=1#frag")
    assert parsed["scheme"] == "https"
    assert parsed["hostname"] == "example.com"
    assert parsed["port"] == 443
    assert parsed["username"] == "user"
    print("[✓] parse_url_parts passed")


def test_replace_path():
    result = UrlUtils.replace_path("https://example.com/old", "/new")
    assert result == "https://example.com/new"
    print("[✓] replace_path passed")


def test_strip_url():
    stripped = UrlUtils.strip_url("https://example.com/test?x=1#frag", keep=["scheme", "netloc"])
    assert stripped == "https://example.com"
    print("[✓] strip_url passed")


def test_normalize_url():
    result = UrlUtils.normalize_url("HTTPS://EXAMPLE.COM/test/")
    assert result == "https://example.com/test"
    print("[✓] normalize_url passed")


def test_extract_root_domain():
    assert UrlUtils.extract_root_domain("https://sub.example.co.uk") == "example.co.uk"
    print("[✓] extract_root_domain passed")


def test_is_valid_url():
    assert UrlUtils.is_valid_url("https://example.com")
    assert not UrlUtils.is_valid_url("example.com")
    print("[✓] is_valid_url passed")


def test_get_auth_from_url():
    auth = UrlUtils.get_auth_from_url("https://user:pass@example.com")
    assert auth == ("user", "pass")
    print("[✓] get_auth_from_url passed")


def test_append_query_params():
    url = "https://example.com/path"
    new_url = UrlUtils.append_query_params(url, {"x": "1", "y": "2"})
    assert "x=1" in new_url and "y=2" in new_url
    print("[✓] append_query_params passed")


def run_all():
    print("[*] Running UrlUtils tests...\n")
    test_ensure_scheme()
    test_add_ports()
    test_add_paths()
    test_expand_url()
    test_parse_url_parts()
    test_replace_path()
    test_strip_url()
    test_normalize_url()
    test_extract_root_domain()
    test_is_valid_url()
    test_get_auth_from_url()
    test_append_query_params()
    print("\n[*] All UrlUtils tests completed successfully.")

if __name__ == "__main__":
    run_all()
