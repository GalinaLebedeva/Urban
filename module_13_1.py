import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
        if i == power:
            break
        i -= 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    man1 = asyncio.create_task(start_strongman('Pasha', 3))
    man2 = asyncio.create_task(start_strongman('Denis', 4))
    man3 = asyncio.create_task(start_strongman('Apollon', 5))
    await man1
    await man2
    await man3

asyncio.run(start_tournament())