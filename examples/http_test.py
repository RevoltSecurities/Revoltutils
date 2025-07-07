import asyncio
import httpx
from revoltutils import HttpUtils
from requests.cookies import RequestsCookieJar


def test_get_random_user_agent():
    ua = HttpUtils.get_random_user_agent()
    print("[✓] get_random_user_agent passed")
    assert isinstance(ua, str) and len(ua) > 0


def test_normalize_header():
    raw = ["User-Agent: test-agent", "Accept: */*"]
    normalized = HttpUtils.normalize_header(raw)
    print("[✓] normalize_header passed")
    assert normalized == {"User-Agent": "test-agent", "Accept": "*/*"}


def test_all_http_methods():
    methods = HttpUtils.all_http_methods()
    print("[✓] all_http_methods passed")
    assert "GET" in methods and "POST" in methods


def test_raw_request_builder():
    req = HttpUtils.raw_request_builder("GET", "https://example.com/path?query=1", {"Host": "example.com"}, "")
    print("[✓] raw_request_builder passed")
    assert "GET /path?query=1 HTTP/1.1" in req


def test_raw_response_builder():
    resp = HttpUtils.raw_response_builder(200, "OK", {"Content-Type": "text/plain"}, "Hello")
    print("[✓] raw_response_builder passed")
    assert "HTTP/1.1 200 OK" in resp


def test_extract_cookies():
    jar = RequestsCookieJar()
    jar.set("session", "abc123", domain="example.com", path="/")
    cookies = HttpUtils.extract_cookies(jar)
    print("[✓] extract_cookies passed")
    assert cookies[0]["name"] == "session"


async def test_dump_request_and_response():
    async with httpx.AsyncClient() as client:
        req = client.build_request("GET", "https://httpbin.org/get")
        raw_req = await HttpUtils.dump_request(req)

        resp = await client.send(req)
        raw_resp = await HttpUtils.dump_response(resp)

        print("[✓] dump_request / dump_response passed")
        assert "GET /get HTTP/1.1" in raw_req
        assert f"{resp.status_code}" in raw_resp


async def test_dump_response_headers_and_raw():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        headers, full = await HttpUtils.dump_response_headers_and_raw(response)

        print("[✓] dump_response_headers_and_raw passed")
        assert "Content-Type" in headers or "content-type" in headers.lower()

async def test_raw_http_reader():
    # --- Test with no body ---
    raw1 = "GET / HTTP/1.1\r\nHost: example.com\r\nUser-Agent: test\r\n\r\n"
    method, url, headers, body = await HttpUtils.raw_http_reader(raw1)
    assert method == "GET"
    assert url == "/"
    assert headers["Host"] == "example.com"
    assert headers["User-Agent"] == "test"
    assert body == ""
    print("[✓] raw_http_reader (no body) passed")

    # --- Test with body ---
    raw2 = "POST /submit HTTP/1.1\r\nHost: example.com\r\nContent-Type: application/json\r\n\r\n{\"key\":\"value\"}"
    method, url, headers, body = await HttpUtils.raw_http_reader(raw2)
    assert method == "POST"
    assert url == "/submit"
    assert headers["Host"] == "example.com"
    assert headers["Content-Type"] == "application/json"
    assert body == '{"key":"value"}'
    print("[✓] raw_http_reader (with body) passed")


async def main():
    print("[*] Running HttpUtils tests...\n")
    test_get_random_user_agent()
    test_normalize_header()
    test_all_http_methods()
    test_raw_request_builder()
    test_raw_response_builder()
    test_extract_cookies()
    await test_dump_request_and_response()
    await test_dump_response_headers_and_raw()
    await test_raw_http_reader()
    print("\n[*] All HttpUtils tests passed!")


if __name__ == "__main__":
    asyncio.run(main())
