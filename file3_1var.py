import asyncio
import time

async def task(name, delay):            #Процессы
    await asyncio.sleep(delay)
    print(f'Задача {name} готова')

async def asyn():               #выполняем задачи параллельно и последовательно, сравнивая их по времени, а также добавим задержки каждому процессу
    delays = [2, 1, 0.5, 4, 3]
    
    print('\nПараллельно : ')
    first_start = time.time()
    t = [task(i, d) for i, d in enumerate(delays)]
    await asyncio.gather(*t)
    first_time = time.time() - first_start
    print(f'Время {first_time} сек')

    print('\nПоследовательно : ')
    second_start = time.time()
    for i,d in enumerate(delays):
        await task(i,d)

    second_time = time.time() - second_start
    print(f'Время {second_time} сек')

    print(f'\nПараллельное быстрее последовательного на {second_time - first_time} сек.')

def main():
    asyncio.run(asyn()) 

if __name__=='__main__':
    main()