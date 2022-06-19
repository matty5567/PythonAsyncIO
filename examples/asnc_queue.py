import asyncio
import random
import os

async def make_item() -> str:
    return os.urandom(5).hex()


async def randsleep() -> None:
    wait_time: int = random.randint(0, 5)
    await asyncio.sleep(wait_time)


async def produce(id: int, q: asyncio.Queue) -> None:
    for _ in range(5):
        await randsleep()
        payload =  await make_item()
        await q.put(payload)
        print(f"producer {id} added <{payload}> to queue")



async def consume(id: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep()
        item = await q.get()
        print(f"consumer {id} recieved <{item}> from queue")
        q.task_done()


async def main():
    queue = asyncio.Queue()
   
    producers = [asyncio.create_task(produce(id, queue)) for id in range(10)]
    consumers = [asyncio.create_task(consume(id, queue)) for id in range(10)]

    await asyncio.gather(*producers)
    await queue.join()

    for c in consumers:
        c.cancel()

if __name__=="__main__":
    asyncio.run(main())