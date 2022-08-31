from threading import Thread, Lock
from random import uniform
from time import sleep

class Philosophers(Thread):
    execute = True

    def __init__(self, id, hashi_left, hashi_right):
        Thread.__init__(self)
        self.id = id
        self.hashi_left = hashi_left
        self.hashi_right = hashi_right

    def run(self):
        while self.execute:
            print(f"\n {self.id} is thinking")
            sleep(uniform(5, 15))
            self.eat()

    def eat(self):
        hashi1, hashi2 = self.hashi_left, self.hashi_right

        while self.execute:
            hashi1.acquire(True)
            locked = hashi2.acquire(False)
            if locked:
                break
            hashi1.release()
        else:
            return

        print(f"\n {self.id} started to eat")
        sleep(uniform(5, 10))
        print(f"\n {self.id} stopped eating")
        hashi1.release()
        hashi2.release()


id = ['F1', 'F2', 'F3', 'F4', 'F5']
hashis = [Lock() for _ in range(5)]
table = [Philosophers(id[i], hashis[i % 5], hashis[(i + 1) % 5]) for i in range(5)]
for _ in range(50):

    Philosophers.execute = True
    for philosophers in table:
        try:
            philosophers.start()
            sleep(2)
        except RuntimeError:
            pass
    sleep(uniform(5, 15))
    execute = False