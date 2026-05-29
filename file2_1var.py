import multiprocessing     #импорты
import random
import time

def generator(p_conn, count):           #генератор чисел
    numb = [random.randint(-1_000_000, 1_000_000) for _ in range(count)]
    p_conn.send(numb)
    p_conn.close()

def square(p_conn):         #вычисление квадрата
    numb = p_conn.recv()
    square = [i**2 for i in numb]   
    print(f'Получено чисел : {len(numb)} . Квадраты чисел : {square}')
    p_conn.close()  
def main():                     #мультипроцесс с функциями генератора и вычисления квадрата
    n_count = 1_000
    par_conn, ch_conn = multiprocessing.Pipe()
    proc_generator = multiprocessing.Process(target = generator, args=(ch_conn, n_count, ) )
    proc_calculator = multiprocessing.Process(target=square ,args = (par_conn, ))
    print('Запуск процессов')
    start_time = time.time()
    proc_generator.start()
    proc_calculator.start()
    proc_generator.join()
    proc_calculator.join()
    print(f'Обмен данными и вычисления завершены за {time.time() - start_time} сек.')

if __name__ == "__main__":
    main()