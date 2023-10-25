# math
import math

print(math.sqrt(9)) # raiz quadrada
print(math.sin(45)) # seno
print(math.cos(45)) # coseno
print(math.log(1000, 10)) # logaritmo
print(math.pi) # pi

print()

# datetime
import datetime

print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.date(2020, 7, 10))
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)

print()

# random
import random

print(random.random())
print(random.randint(1, 10))
print(random.randrange(0, 10, 2))

x = ['K', 'd', 13, '34-j', 'x']

print(random.choice(x))

print()

# time
import time as tm

print(tm.time())

antes = tm.time()

lista = []
for i in range(0, 100000):
    lista.append(i)

depois = tm.time()

print(antes, depois)

print('finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('até a proxima')
