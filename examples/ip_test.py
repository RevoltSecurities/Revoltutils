import asyncio
from revoltutils import IPUtils

async def main():
    ipu = IPUtils()
    print("Is IP:", ipu.is_ip("8.8.8.8"))
    print("Is internal:", ipu.is_internal("192.168.1.1"))
    print("Public IP:", await ipu.whats_my_ip())
    print("To FQDN of 8.8.8.8:", await ipu.to_fqdn("8.8.8.8"))

asyncio.run(main())
