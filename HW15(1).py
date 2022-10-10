def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper


@benchmark
def func1():
  A = [i for i in range(101)]
  B = [x for x in A if x%2 == 0]
  print(B)

func1()

@benchmark
def func2():
    lst = []
    for x in range(100):
        if x%2==0:lst.append(x)
    print(lst)

func2()







