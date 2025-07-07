import asyncio
from revoltutils import HealthCheck, ConnectionInfo


async def test_tcp_success():
    info: ConnectionInfo = await HealthCheck.check_connection("google.com", 80)
    print(f"[TCP Success] {info.message}")
    assert info.successful


async def test_tcp_fail():
    info: ConnectionInfo = await HealthCheck.check_connection("127.0.0.1", 9999)
    print(f"[TCP Fail] {info.message}")
    assert not info.successful


async def main():
    print("[*] Running HealthCheck TCP-only tests...\n")
    await test_tcp_success()
    await test_tcp_fail()
    print("\n[*] All TCP tests completed.")


if __name__ == "__main__":
    asyncio.run(main())