from particula import Particula

import json
class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_inicio(self,particula:Particula):
        self.__particulas.insert(0,particula)

    def agregar_final(self,particula:Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont=0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula =self.__particulas[self.cont]
            self.cont+=1
            return particula
        else:
            raise StopIteration
    
    def eliminaruno(self):
        self.__particulas.pop()
        return self.__particulas

    def recorrer(self,cont):
       
        if cont < len(self.__particulas):
            particula =self.__particulas[cont]
            return particula
        else:
            raise StopIteration

    def guardar(self,ubicacion):
        try:
            with open(ubicacion,"w") as archivo:
                lista=[particula.to_dic() for particula in self.__particulas]
                print(lista)
                json.dump(lista,archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self,ubicacion):
        try:
            with open(ubicacion,"r") as archivo:
                lista=json.load(archivo)
                self.__particulas=[Particula(**particula) for particula in lista]
            return 1
        except:
            return 0
    
    def sort_list(self,opc=1):
        if opc==1:
            #self.__particulas.sort()
            self.__particulas.sort(key= lambda particula: particula.id)
            print("\nid")
        elif opc==2:
            self.__particulas.sort(key= lambda particula: particula.distancia,reverse=True)
            print("\nd")
        if opc==3:
            self.__particulas.sort(key= lambda particula: particula.velocidad)
            print("\nv")
    def get_puntos(self):
        puntos=[]
        for particula in self.__particulas:
            punto01=Punto(particula.origen_x,particula.origen_y,particula.red,particula.green,particula.blue)
            punto02=Punto(particula.destino_x,particula.destino_y,particula.red,particula.green,particula.blue)
            puntos.append(punto01)
            puntos.append(punto02)
        return puntos
    
    def cantidad(self):
        return len(self.__particulas)
class Punto:
    def __init__(self, x:int=0,y:int=0,red:int=0,green:int=0,blue:int=0):
        self.x=x
        self.y=y
        self.red=red
        self.green=green
        self.blue=blue
        


    #def fuerza_bruta(self):
     #       fuerza_brutaalg(self.__particulas)


            #archivo.write(str(self))
#p= Particula(1,2,1,3,4,5,6,7,8,9)
#p1= Particula(20,69,59,41,55,66,99,80,52,63)
#p2= Particula(2,69,50,200,55,66,100,80,52,63)
#particulas=Particulas()
#particulas.agregar_inicio(p2)
#particulas.mostrar()
#particulas.agregar_final(p)
#particulas.mostrar()
##particulas.agregar_inicio(p1)
#particulas.mostrar()