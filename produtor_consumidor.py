import threading
import time, random
import threading

class BufferLimitado:
   TAM_BUFFER = 5
   mutex  = threading.Semaphore(1)
   empty  = threading.Semaphore(TAM_BUFFER)
   full   = threading.Semaphore(0)
   buffer = list(range(TAM_BUFFER))
   cheio  = 0
   livre  = 0

   def insert(self, item):
      self.empty.acquire()
      self.mutex.acquire()
      self.buffer[self.livre] = item
      self.livre = (self.livre + 1) % self.TAM_BUFFER
      self.mutex.release()
      self.full.release()

   def remove(self):
      self.full.acquire()
      self.mutex.acquire()
      item = self.buffer[self.cheio]
      self.cheio = (self.cheio + 1) % self.TAM_BUFFER
      self.mutex.release()
      self.empty.release()
      return item

b = BufferLimitado()

def produtor():
   while True:
      time.sleep(2)
      item = time.ctime()
      b.insert(item)
      print ("Produtor produziu:", b.livre, b.cheio)
      print("--------------------------------------------------------------------")

def consumidor():
   while True:
      time.sleep(2)
      item = b.remove()
      print ("Consumidor consumiu:",  b.livre, b.cheio)
      print("--------------------------------------------------------------------")
threading._start_new_thread(produtor, ())
threading._start_new_thread(consumidor, ())

while 1: pass
