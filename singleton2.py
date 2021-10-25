def singleton(cls):
    
    instances =dict()
    
    def wrap(*arg,**kwarg):
        if cls not in instances:
            instances[cls]=cls(*arg,**kwarg)
        return instances[cls]
    return wrap


@singleton
class Humano:
    def __init__(self,edad):
        self.edad=edad
    def hablar(self,mensaje): 
        self.logo=mensaje
       

if __name__ =='__main__':
    pedro=Humano(26)
    raul=Humano(36)
    pedro.hablar('hola pedro edad')
    raul.hablar('hola raul edad')
    print(pedro.edad)
    print(raul.edad)
    print(pedro.logo)
    print(raul.logo)
    print(pedro is raul)