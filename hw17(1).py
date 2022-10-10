
 
from _thread import start_new_thread
 
threadId = 1
 
def factorial(n):
   global threadId
   if n < 1:
       print("%s: %d" % ("Нить", threadId ))
       threadId += 1
       return 1
   else:
       returnNumber = n * factorial( n - 1 )
       print(str(n) + '! = ' + str(returnNumber))
       return returnNumber
 
start_new_thread(factorial,(5, ))
start_new_thread(factorial,(4, ))
 
c = input("Ждем поток для возврата...\n")







def fact(n): 
    f = 1
    for i in range(1,n + 1):
        f *= i
    return f

print(fact(5))






