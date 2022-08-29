from random import randint
from time import sleep
import sys
import os

list = []
sleep_c = False
sleep_p = False
list_length = int(input("Digite o tamanho da lista: "))

def producer():
    global list_length, sleep_c, sleep_p, list

    if not sleep_p:
        while len(list) < list_length:
            list.append(randint(0, 1000))
            print("Produtor: Produzindo valores á lista: " + str(list))

    else:
        print("Produtor: Todas as posições da lista foram preenchidas." + str(list))
        print("Produtor saiu para descansar.Ele voltará quando a lista estiver vazia.")
        sleep_p = True
        sleep_c = False
        consumer()

def consumer():
  global list_length, list, sleep_p, sleep_c

if not sleep_c:
    if list:
        del list[0]
        print("Consumidor: Consumindo os valores da lista: " + str(list))
else:
    print("Consumidor: Todas as posições da lista foram consumidas." +str(list))
    print("O consumidor saiu para descansar. Ele voltará quando a lista conter algum valor" )
    sleep_c = True
    sleep_p = False
    producer()

while True:
    producer()
    consumer()
    sleep(6)
    print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--")

