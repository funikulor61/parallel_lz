import requests
import threading
import time
        #ссылки
urls = [            
    "https://google.com", "https://wikipedia.org", "https://python.org",
    "https://github.com", "https://habr.com", "https://yandex.ru",
    "https://microsoft.com", "https://apple.com", "https://samsung.com",
    "https://cloudflare.com"
]

def download(url):          #функция скачивания сайта
    req = requests.get(url)
    print(f'Скачено : {url} (Размер: {len(req.content)} байт)')

def main():
    print('Скачивание без потоков: ')               #Скачиваник без потоками
    first_start = time.time()

    for i in urls:
        download(i)

    first_time = time.time() - first_start
    print(f'Время без поток: {first_time} сек.\n')

    print('Cкачивание с потоками: ')            #Скачивание с потоками
    second_start = time.time()      #начало выполнения
    threads = []

    for i in urls:
        thr = threading.Thread(target=download, args=(i,))
        threads.append(thr)
        thr.start()
    for thr in threads:
        thr.join()

    second_time = time.time() - second_start        #время выполнения 
    print(f'Время без поток: {second_time} сек.\n')

    print(f'Разница по времени: {first_time - second_time} сек.')

if __name__ == '__main__':
    main()