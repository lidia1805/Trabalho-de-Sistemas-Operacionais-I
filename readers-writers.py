import threading
import time


class LeitoresEEscritores():
    def __init__(self):
        self.leitor = threading.Semaphore()  #inicializando semaforos de leitor e escritor                               
        self.escritor = threading.Semaphore() 
        self.contLeitor = 0   #numero de leitores

    def Leitor (self):
        while True:
            self.leitor.acquire()      #leitor espera no semaforo

            self.contLeitor+=1       #incrementando leitor

            if self.contLeitor == 1:   #se há um leitor, há espera na escrita
                self.escritor.acquire()  #escritor espera no semaforo

            self.leitor.release()     #sinal do leitor liberado

            print(f"Leitor número {self.contLeitor} está lendo")

            self.leitor.acquire()   #leitor espera no semaforo 

            self.contLeitor-=1   #se um leitor leu, decrementa o número de leitores

            if self.contLeitor == 0: #se não há leitor, o escritor pode escrever
                self.escritor.release()  #sinal do escritor liberado
                
            self.leitor.release()      #sinal on read semaphore

            time.sleep(3)          

    def Escritor (self):
        while True:
            self.escritor.acquire()     #espera no sinal de escrita
            print("Dados sendo escritos...")  #escreve os dados
            print("--------------------------")

            self.escritor.release()      #sinal do escritor liberado

            time.sleep(3)    
    
    def main(self):
        #funcao pra chamar leitores e escritores
        l1 = threading.Thread(target = self.Leitor) 
        l1.start()
        l2 = threading.Thread(target = self.Leitor) 
        l2.start()
        l3 = threading.Thread(target = self.Leitor) 
        l3.start()
        l4 = threading.Thread(target = self.Leitor) 
        l4.start()
        e1 = threading.Thread(target = self.Escritor) 
        e1.start()
        e2 = threading.Thread(target = self.Escritor) 
        e2.start()
       
        

if __name__=="__main__":
    run = LeitoresEEscritores()
    run.main()