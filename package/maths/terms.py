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
    
    def __init__(self, lado1, lado2, lado3):

        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
    
    def setLado1(self, lado1):

        if isinstance(lado1, float, int):
            self._lado1 = lado1
        else:
            self._lado1 = 0

    def getLado1(self):

        return self._lado1
    
    def setLado2(self, lado2):

        if isinstance( lado2, float, int):
            self._lado2 = lado2
        else:
            self._lado2 = 0

    def getLado2(self):

        return self._lado2
    
    def setLado3(self, lado3):

        if isinstance(lado3, float, int):
            self._lado3 = lado3
        else:
            self._lado3 = 0

    def getLado3(self):

        return self._lado3
    
    def printaInfosBasicas(self):

        print(f'O triângulo tem como lados {self._lado1}, {self._lado2} e {self._lado3}')

    def perimetro(self):

        self.p = self._lado1 + self._lado2 + self._lado3
        return self.p

    def setCor(self, cor):

        self.cor = cor

    def _verificaEquilatero(self):

        auxiliar = False
        if self._lado1 == self._lado2 == self._lado3:
            self._lado1 = self._lado1
            self._lado2 = self._lado2
            self._lado3 = self._lado3
            auxiliar = True
            return auxiliar
        else:
            return auxiliar
        
    def _verificaIsosceles(self):

        auxiliar = False
        if self._lado1 == self._lado2 or self._lado1 == self._lado3 or self._lado2 == self._lado3:
            self._lado1 = self._lado1
            self._lado2 = self._lado2
            self._lado3 = self._lado3
            auxiliar = True
            return auxiliar
        else:
            return auxiliar
        
    def _verificaEscaleno(self):

        auxiliar = False
        if self._lado1 != self._lado2 != self._lado3:
            self._lado1 = self._lado1
            self._lado2 = self._lado2
            self._lado3 = self._lado3
            auxiliar = True
            return auxiliar
        else:
            return auxiliar
        
    def _verificaMaiorLado(self):

        maiorlado = max(self._lado1, self._lado2, self._lado3)
        return maiorlado
    
    def _verificaMenorLado(self):

        menorlado = min(self._lado1, self._lado2, self._lado3)
        return menorlado
    
    def _desigualdadetriangular(self):

        auxiliar = False
        if (self._lado1 + self._lado2) > self._lado3 and (self._lado2 + self._lado3) > self._lado1 and (self._lado1 + self._lado3) > self._lado2:
            auxiliar = True
            return auxiliar
        else:
            return auxiliar
        
    def _semiperimetro(self):

        semi = (self._lado1 + self._lado2 + self._lado3)/2
        return semi


class TrianguloEquilatero(Triangulo):
    
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)

    def printaPerimetro(self):

        verificar = self._verificaEquilatero()
        if verificar is True:
            perimetro = self.perimetro()
            print(f'O perímetro do triângulo equilátero é {perimetro}')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo equilátero, por favor, informe outros valores')
    
    def printarCor(self):

        verificar = self._verificaEquilatero()
        if verificar is True:
            c = input("Escolha a cor do seu triângulo equilátero:")
            self.cor = c
            print(f'A cor do triângulo equilátero é: {self.cor}.')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo equilátero, por favor, informe outros valores')

    def area(self):

        verficar = self._verificaEquilatero()
        if verficar is True:
            self.a = ((self._lado1**2 * math.sqrt(3))/4)
            self.areaArredondada = round(self.a, 2)
            return self.areaArredondada
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo equilátero, por favor, informe outros valores')

    def printaArea(self):

        verficar = self._verificaEquilatero()
        if verficar is True:
            area = self.areaArredondada
            print(f'A área do triângulo equilátero é igual a {area}')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo equilátero, por favor, informe outros valores')

class TrianguloIsosceles(Triangulo):
    
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)

    def printaPerimetro(self):

        verificar = self._verificaIsosceles()
        if verificar is True:
            perimetro = self.perimetro()
            print(f'O perímetro do triângulo isósceles é {perimetro}')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')

    def printarCor(self):

        verificar = self._verificaIsosceles()
        if verificar is True:
            c = input("Escolha a cor do seu triângulo isósceles:")
            self.cor = c
            print(f'A cor do triângulo isósceles é: {self.cor}.')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')

    def altura(self):
        
        if self._lado1 == self._lado2:
            h = (self._lado1**2 - ((self._lado3**2)/4))**0.5
            return h
        elif self._lado1 == self._lado3:
            h = (self._lado1**2 -((self._lado2**2)/4))**0.5
            return h
        elif self._lado2 == self._lado3:
            h = (self._lado2**2-((self._lado1**2)/4))**0.5
            return h
        
    def base(self):

        if self._lado1 == self._lado2:
            b = self._lado3
            return b
        elif self._lado1 == self._lado3:
            b = self._lado2
            return b
        elif self._lado2 == self._lado3:
            b = self._lado1
            return b

    def area(self):
        verificar = self._verificaIsosceles()
        altura = self.altura()
        base = self.base()
        if verificar is True:
            a = (altura * base)/ 2
            areaArredondada = round( a, 2)
            return areaArredondada
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')

    def printaArea(self):

        verficar = self._verificaIsosceles()
        if verficar is True:
            area = self.area()
            print(f'A área do triângulo isósceles é igual a {area}')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')

class TrianguloEscaleno(Triangulo):
    
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2, lado3)

    def printaCor(self):

        verificar = self._verificaEscaleno()
        if verificar is True:
            c = input("Escolha a cor do seu triângulo escaleno:")
            self.cor = c
            print(f'A cor do triângulo escaleno é: {self.cor}.')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo escaleno, por favor, informe outros valores')

    def printaPerimetro(self):

        verificar = self._verificaEscaleno()
        if verificar is True:
            perimetro = self.perimetro()
            print(f'O perímetro do triângulo escaleno é {perimetro}')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo escaleno, por favor, informe outros valores')



    def area(self):
        
        s = self._semiperimetro()
        a = (s*((s-self._lado1)*(s-self._lado2)*(s-self._lado3)))**0.5
        return a
    
    def pintaArea(self):

        verificar = self._verificaEscaleno()
        desigual = self._desigualdadetriangular()
        if verificar is True:
            if desigual is True:
                area = self.area()
                areaArredondada = round(area, 2)
                print(f'A área do triângulo escaleno é {areaArredondada}')
            else:
                print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')
        else:
            print('Os valores de lado escolhidos não correspondem a um triângulo escaleno, por favor, informe outros valores')


class Quadrado():
    pass

class Retangulo():
    pass

class Trapezio():
    pass

class Poligono():
    pass

class Octal():
    pass