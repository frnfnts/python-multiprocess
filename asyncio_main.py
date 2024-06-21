import asyncio


async def f(i):
    return i * i


async def main():
    result = await asyncio.gather(*[f(i) for i in range(5)])
    print(result)


asyncio.run(main())
