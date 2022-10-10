import urllib.request
import time
import threading
import sys

url = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
for url in url:
    read_url(url)
print(time.time() - start)






def run_threads(count):
    threads = [
        threading.Thread(target=read_url, args=(url))
        for i in range(5, count)
    ]
    for thread in threads:
        thread.start() 
    for thread in threads:
        thread.join()



run_threads(4)
