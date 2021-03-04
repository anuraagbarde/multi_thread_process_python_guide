# Use the below for running in powershell

# Measure-Command { python performance.py |Out-Default} | Select-Object -Property TotalSeconds

import threading
from threading import Thread


def bigForLoop(x):
    for i in range(30000000):
        i*i
    print("done", x)
    return "exiting big function..."

def smallForLoop(x):
    for i in range(100000):
        i*i
    print("done", x)
    return "exiting small function..."


class MyThread(Thread):   # extending the threading.Thread class
    def __init__(self, x, name = None): # You can specify the custom-name for understanding or it will get named automatically 
        super().__init__(name = name)
        self.x = x
    
    def run(self):     # this is an inbuilt function for running Thread
        identity = threading.get_ident() # need to dynamically/at runtime  fetch the thread id
        print("start thread name =", self.name, "id =", identity)

        # do whatever you want
        smallForLoop(self.x)
        bigForLoop(self.x+10)
        # end

        print("ending thread name =", self.name)


if __name__ == '__main__':

    # most basic way to make threads
        # ONLY ONE THREAD CAN USE THE CPU AT ANY GIVEN TIME IN A SINGLE PROCESS, USE THREADING FOR I/O LIKE OPERATIONS

    t1 = Thread(target=bigForLoop, args=(1001,)) # or can use >> t1 = MyThread(1001) << and then do >> t1.start() <<
    t2 = Thread(target=bigForLoop, args=(1002,))
    t3 = Thread(target=bigForLoop, args=(1003,))
    t4 = Thread(target=bigForLoop, args=(1004,))
    t5 = Thread(target=bigForLoop, args=(1005,))
    
    t11 = Thread(target=bigForLoop, args=(1011,))
    t12 = Thread(target=bigForLoop, args=(1012,))
    t13 = Thread(target=bigForLoop, args=(1013,))
    t14 = Thread(target=bigForLoop, args=(1014,))
    t15 = Thread(target=bigForLoop, args=(1015,))


    # # Threading 0
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()

    # # Threading 1
    # t11.start()
    # t12.start()
    # t13.start()
    # t14.start()
    # t15.start()


    # # Basic 0
    # bigForLoop(1)
    # bigForLoop(2)
    # bigForLoop(3)
    # bigForLoop(4)
    # bigForLoop(5)

    # # Basic 1
    # bigForLoop(11)
    # bigForLoop(12)
    # bigForLoop(13)
    # bigForLoop(14)
    # bigForLoop(15)


from multiprocessing import Pool

    # To actually apply multiprocessing and not multi-threading

    # with Pool(processes=4) as localpool1: # The number of Processes will depend on your machine and try to keep it below the number of core your system has. Process are costly, threads aren't.

        # data = [2001,2002,2003,2004,2005]
        # data += [2011, 2012, 2013, 2014, 2015]
        # results = localpool1.map(bigForLoop, data)

        
        # You can also use localpool1.apply_async(func, arguments) if you want to excecute func only once, input argumets will go as tuples
        
        # result_single_1 = localpool1.apply_async(bigForLoop, (3001,))
        # result_single_2 = localpool1.apply_async(bigForLoop, (3002,))
        # result_single_3 = localpool1.apply_async(bigForLoop, (3003,))
        # result_single_4 = localpool1.apply_async(bigForLoop, (3004,))
        
        # print(result_single_1.get())
        # print(result_single_2.get())
        # print(result_single_3.get())
        # print(result_single_4.get())