from math import pi
import math

class Reta():


    def __init__(self,a,b):

        self.a = a
        self.b = b


    def interpolar(self,x):

        y = self.a * x + self.b
        return y

    
    def model(self):

        print(f'Os parâmertros do meu modelo de reta são: a={self.a}, b={self.b}')


class Circulo():

    def __init__(self,x,y,r):

        self.setX(x)
        self.setY(y)
        self.setR(r)

    def setX(self,x):

        if x > 0:
            self.x = x
        else:
            self.x = 0

    def setY(self,y):

        if y > 0:
            self.y = y
        else: 
            self.y = 0

    def setR(self,r):

        if r > 0:
            self.r = r
        else:
            self.r = 0

    def printarInit(self):

        print(f'O círculo tem origem em {self.x} e {self.y} e raio igual a {self.r}.')

    def diametro(self):

        self.d1 = 2 * self.r
        return self.d1
    
    def printaDiametro(self):

        diametro = self.diametro()
        print(f'O diâmetro do círculo é igual a {diametro}.')
    
    def area(self):
        self.a = (self.r **2) * pi
        return self.a
    
    def printarArea(self):
        area = self.area()
        print(f'A área do círculo é igual a {area:.4f}.')
    
    def comprimento(self):
        self.c = self.r * pi *2
        return self.c
    
    def printarComprimento(self):
        comprimento = self.comprimento()
        print(f'O comprimento do círculo é igual a {comprimento:.4f}.')

    
    def setCor(self, cor):

        self.cor = cor

    def printarCor(self):

        print(f'A cor do círculo é: {self.cor}.')


class Ponto():

    def __init__(self,x,y):
        self.setX(x)
        self.setY(y)

    def setX(self,x):

        if x > 0:
            self.x = x
        else:
            self.x = 0

    def setY(self,y):

        if y > 0:
            self.y = y
        else: 
            self.y = 0
 

    def printarInit(self):
        
        print(f'O ponto está nas coordenadas {self.x} e {self.y}.')

    def distanciaAOrigem(self):

        self.d = self.x **2 + self.y **2
        self.raizded = math.sqrt(self.d)
        return self.raizded
    
    def printaDistancia(self):
        
        self.distanciaAOrigem()
        print(f'A distância do ponto à origem é igual a {self.raizded:.4f} unidades de comprimento.')
