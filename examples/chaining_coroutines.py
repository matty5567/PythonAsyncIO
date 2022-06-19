import asyncio
import random
import time

async def part1() -> int:
    i = random.randint(0, 5)
    print(f"part1 sleeping for {i} seconds.")
    await asyncio.sleep(i)
    return i

async def part2(n: int) -> int:
    i = random.randint(0, 5)
    print(f"part2 sleeping for {i} seconds.")
    await asyncio.sleep(i)
    print(f"")
    return i

async def chain() -> None:
    start = time.perf_counter()
    p1 = await part1()
    p2 = await part2(p1)
    end = time.perf_counter() - start
    print(f"{p1} (from part1) + {p2} (from part2) = {p1 + p2} (took {(end-start):0.2f} secs to complete)")

async def main():
    await asyncio.gather(*(chain() for _ in range(3)))

if __name__=="__main__":
    asyncio.run(main())
    