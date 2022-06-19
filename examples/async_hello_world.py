'''
Talking to each of the calls to count() is a single event loop or coordinator.

When each task reaches await asyncio.sleep(1), the function yells up to the event loop and gives back control.

The execution of this function takes just 1.01 seconds, contrasted to the synchronous version which would take 3.

time.sleep represents a 'blocking function' whilst asyncio.sleep() would represent a non-blocking call.

'''

import asyncio

async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__=="__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")