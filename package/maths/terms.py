from math import pi
import math

class Reta():

    def __init__(self,x,y):

        self.__x = x
        self.__y = y

    def setX(self, x):

        if isinstance(x, float, int):
            self.__x = x
        else:
            self.__x = 0

    def getX(self):

        return self.__x

    def setY(self, y):

        if isinstance(y, float, int):
            self.__y = y
        else:
            self.__y = 0

    def getY(self):

        return self.__y

    def interpolar(self, a):

        i = self.__x * a + self.__y
        return i
    
    def printaInterpolar(self):

        z = int(input("Insira o valor que deseja interpolar:"))

        print(f'Interpolando o valor {z}: i = {self.interpolar(z)}')

    
    def model(self):

        print(f'Os parâmetros do meu modelo de reta são: x={self.__x}, y={self.__y}')

    def setCor(self, cor):

        self.cor = cor

    def printarCor(self):

        c = input("Escolha a cor da sua reta:")
        self.cor = c

        print(f'A cor da reta é: {self.cor}.')


class Circulo():

    def __init__(self,x,y,r):

        self.__x = x
        self.__y = y
        self.__r = r

    def setX(self,x):

        if isinstance(x, float, int):
            self.__x = x
        else:
            self.__x = 0

    def getX(self):

        return self.__x

    def setY(self,y):

        if isinstance(y, float, int):
            self.__y = y
        else: 
            self.__y = 0

    def getY(self):

        return self.__y

    def setR(self,r):

        if isinstance(r, float, int):
            self.__r = r
        else:
            self.__r = 0

    def getR(self):

        return self.__r

    def printarInit(self):

        print(f'O círculo tem origem em {self.__x} e {self.__y} e raio igual a {self.__r}.')

    def diametro(self):

        self.d1 = 2 * self.__r
        return self.d1
    
    def printaDiametro(self):

        diametro = self.diametro()
        print(f'O diâmetro do círculo é igual a {diametro}.')
    
    def area(self):
        self.a = (self.__r **2) * pi
        return self.a
    
    def printarArea(self):
        area = self.area()
        print(f'A área do círculo é igual a {area:.4f}.')
    
    def comprimento(self):
        self.c = self.__r * pi *2
        return self.c
    
    def printarComprimento(self):
        comprimento = self.comprimento()
        print(f'O comprimento do círculo é igual a {comprimento:.4f}.')

    
    def setCor(self, cor):

        self.cor = cor

    def printarCor(self):

        c = input("Escolha a cor do seu círculo:")
        self.cor = c
        print(f'A cor do círculo é: {self.cor}.')


class Ponto():

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def setX(self,x):

        if isinstance(x, float, int):
            self.__x = x
        else:
            self.__x = 0

    def getX(self):
        return self.__x

    def setY(self,y):

        if isinstance(y, float, int):
            self.__y = y
        else: 
            self.__y = 0

    def getY(self):
        return self.__y 

    def printarInit(self):
        
        print(f'O ponto está nas coordenadas {self.__x} e {self.__y}.')

    def distanciaAOrigem(self):

        self.d = self.__x **2 + self.__y **2
        self.raizded = math.sqrt(self.d)
        return self.raizded
    
    def printaDistancia(self):
        
        self.distanciaAOrigem()
        print(f'A distância do ponto à origem é igual a {self.raizded:.4f} unidades de comprimento.')

    def setCor(self, cor):

        self.cor = cor

    def printarCor(self):

        c = input("Escolha a cor do seu ponto:")
        self.cor = c

        print(f'A cor do ponto é: {self.cor}.')


class Triangulo():
    pass

class Quadrado():
    pass

class Retangulo():
    pass
