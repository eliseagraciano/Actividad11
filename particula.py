from algoritmos import distancia_euclidiana
class Particula:
    def __init__(self,id=0,origen_x=0,origen_y=0,destino_x=0,destino_y=0,velocidad=0,red=0,green=0,blue=0,distancia=0.0):
        self.__id=id
        self.__origen_x=origen_x
        self.__origen_y=origen_y
        self.__destino_x=destino_x
        self.__destino_y=destino_y
        self.__velocidad=velocidad
        self.___red=red
        self.___green=green
        self.__blue=blue
        self.__distancia=distancia_euclidiana(origen_x, destino_x, origen_y, destino_y)
    
    #def __lt__(self,other):
     #   return self.__id < other.__id



    def __str__(self):
        return(
            'Id: '+ str(self.__id) + '\n' +
            'Origen x: '+ str(self.__origen_x) + '\n' +
            'Origen y: '+ str(self.__origen_y) + '\n' +
            'Destino x: '+ str(self.__destino_x) + '\n' +
            'Destino y: '+ str(self.__destino_y) + '\n' +
            'Velocidad: '+ str(self.__velocidad) + '\n' +
            'Red: '+ str(self.___red) + '\n' +
            'Green: '+ str(self.___green) + '\n' +
            'Blue: '+ str(self.__blue) + '\n' +
            'Distancia: '+ str(self.__distancia) + '\n' 
        )
    @property
    def id(self):
        return self.__id
    @property
    def origen_x(self):
        return self.__origen_x
    @property
    def origen_y(self):
        return self.__origen_y
    @property
    def destino_x(self):
        return self.__destino_x
    @property
    def destino_y(self):
        return self.__destino_y
    @property
    def velocidad(self):
        return self.__velocidad
    @property
    def red(self):
        return self.___red
    @property
    def green(self):
        return self.___green
    @property
    def blue(self):
        return self.__blue
    @property
    def distancia(self):
        return self.__distancia

    def to_dic(self):
        return{
            'id':self.__id,
            'origen_x':self.__origen_x,
            'origen_y':self.__origen_y,
            'destino_x':self.__destino_x,
            'destino_y':self.__destino_y,
            'velocidad':self.__velocidad,
            'red':self.___red,
            'green':self.___green,
            'blue':self.__blue,
            #'distancia':self.__distancia

        }
            
        
    
