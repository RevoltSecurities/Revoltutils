import asyncio
from revoltutils import DnsUtils

async def main():
    await DnsUtils.init()  # setup custom nameservers

    domain = "https://google.com"
    records = await DnsUtils.get_all_records(domain)
    print(records)
    domain = "https://api.google.com"
    records = await DnsUtils.get_all_records(domain)
    print(records)

if __name__ == "__main__":
    asyncio.run(main())
