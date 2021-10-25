import time
import psutil
import os
def memory_usage_psutil():
    # return the memory usage in MB

    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

def singleton(cls):
    
    instances =dict()
    
    def wrap(*arg,**kwarg):
        if cls not in instances:
            instances[cls]=cls(*arg,**kwarg)
        return instances[cls]

    return wrap


@singleton
class  prueba:
    mehijo="dato"
    def __init__(self,features):
        self.features = features
    
    def __repr__(self):
        return f'Car ({self.features})'
    @classmethod
    def hola(cls):
        m=cls.mehijo
        return m

if __name__ =='__main__':
    inicio=time.time()
    for i in range(50000):
        user1=prueba('calato')
        user2=prueba('test')
        user2=prueba('dato')
        print(user1 is user2)
        #print(user2)
        print(user2.__repr__())
        print(user1.hola())
        print(prueba('morongo del morongo').hola())
    
    fin=time.time()
print(fin-inicio)
print(memory_usage_psutil())