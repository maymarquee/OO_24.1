from math import pi
import math
from abc import ABC, abstractmethod

class Ponto():

    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def setX(self,x):

        if x.isdigit():
            self.__x = x
        else:
            self.__x = 0

    def getX(self):
        return self.__x

    def setY(self,y):

        if y.isdigit():
            self.__y = y
        else: 
            self.__y = 0

    def getY(self):
        return self.__y 
    
    def getType(self):

        return 'Ponto_'

    def printarInit(self):
        
        print(f'\nO ponto está nas coordenadas x={self.__x} e y={self.__y}.\n')

    def centro(self):
        centro = [self.__x, self.__y]
        return centro
    
    def distancia(self):

        dis = self.__y - self.__x
        return dis

    def distanciaAOrigem(self):

        self.d = self.__x **2 + self.__y **2
        self.raizded = math.sqrt(self.d)
        return self.raizded
    
    def printaDistancia(self):
        
        self.distanciaAOrigem()
        print(f'\nA distância do ponto à origem é igual a {self.raizded:.2f} unidades de comprimento.\n')

    def distanciaEntrePontos(self, x_p, y_p):

        d = ((x_p - self.__x)**2 +(y_p - self.__y)) 
        raizd = math.sqrt(d)
        darredondada = round(raizd, 2)
        return darredondada

    def printaDistaPontos(self, x_p, y_p):

        distancia = self.distanciaEntrePontos(x_p, y_p)
        print(f'\nA distância entre o ponto informado e o ponto criado é de {distancia} unidades de comprimento.\n')

    def setCor(self, cor):

        self.cor = cor

    def printarCor(self):

        c = input("Escolha a cor do seu ponto:")
        self.cor = c

        print(f'A cor do ponto é: {self.cor}.')

    def verificaInterferencias(self, x_, y_):

        x_ = int(x_)
        y_ = int(y_)
        if self.__x == x_ and self.__y == y_:
            print('\nOs pontos possuem interferência.')
        else:
            print('\nOs pontos não possuem interferência.')

      

class Reta():

    def __init__(self,x, y, z, w):

        self.ponto1 = Ponto(x, y)
        self.ponto2 = Ponto(z, w)
        self._x1 = x 
        self._y1 = y
        self._x2 = z
        self._y2 = w

    def getType(self):

        return 'Reta_'

    def interpolar(self, a):

        i = self.ponto1.distancia() * a + self.ponto2.distancia()
        return i
    
    def printaInterpolar(self):

        while True:
            try:
                z = int(input("\nInsira o valor que deseja interpolar:"))
                break
            except ValueError:
                print('O valor inserido não é válido. Insira um número')

        print(f'\nInterpolando o valor {z}: i = {self.interpolar(z)}\n')

    def distanciaEntrePontos(self):
        
        d = ((self._x2 - self._x1)**2 +(self._y2 - self._y1)) 
        raizd = math.sqrt(d)
        darredondada = round(raizd, 2)
        return darredondada

    def printarInit(self):

        print(f'\nOs parâmetros do meu modelo de reta são: x1={self._x1}, y1={self._y1}, x2={self._x2} e y2={self._y2}.\n')

    def printarDistanciaPontos(self):
        
        tamanho = self.distanciaEntrePontos()
        print(f'\nA dimensão da reta é de {tamanho} unidades de comprimento.\n')

    def setCor(self, cor):

        self.cor = cor

    def printarCor(self):

        c = input("Escolha a cor da sua reta:")
        self.cor = c

        print(f'A cor da reta é: {self.cor}.')

    def verificaInterferencias(self, x_p, y_p):
        
        x_p = int(x_p)
        y_p = int(y_p)
        distancia1 = ((x_p - self._x1)**2 + (y_p - self._y1)**2)**0.5
        distancia2 = ((x_p - self._x2)**2 + (y_p - self._y2)**2)**0.5

        distancia12 = ((self._x1 - self._x2)**2 + (self._y1 - self._y2)**2)**0.5

        if (distancia1 + distancia2) <= 1.1*distancia12:
            print('\nO ponto inserido está compreendido nas proximidades do segmento de reta')
        else:
            print('\nO ponto inserido não está compreendido nas proximidades do segmento de reta')

class Circulo():

    def __init__(self, ponto, r):

        self.__ponto = ponto
        self.__r = r

    def setR(self,r):

        if isinstance(r, float, int):
            self.__r = r
        else:
            self.__r = 0

    def getR(self):

        return self.__r
    
    def getType(self):

        return 'Círculo_'

    def printarInit(self):

        print(f'\nO círculo tem centro em {self.__ponto} e raio igual a {self.__r}.\n')

    def diametro(self):

        self.d1 = 2 * self.__r
        return self.d1
    
    def printaDiametro(self):

        diametro = self.diametro()
        print(f'\nO diâmetro do círculo é igual a {diametro}.\n')
    
    def area(self):
        self.a = (self.__r **2) * pi
        return self.a
    
    def printarArea(self):
        area = self.area()
        print(f'\nA área do círculo é igual a {area:.2f}.\n')
    
    def comprimento(self):
        self.c = self.__r * pi *2
        return self.c
    
    def printarComprimento(self):
        comprimento = self.comprimento()
        print(f'\nO comprimento do círculo é igual a {comprimento:.2f}.\n')
    
    def setCor(self, cor):

        self.cor = cor

    def printarCor(self):

        c = input("Escolha a cor do seu círculo:")
        self.cor = c
        print(f'A cor do círculo é: {self.cor}.')

    def verificaInterferencias(self, x_, y_):
        
        x_ = int(x_)
        y_ = int(y_)

        x_centro = self.__ponto[0]
        y_centro = self.__ponto[1]

        def distanciaAoCentro():
            dis = ((x_ - x_centro)**2 + (y_ - y_centro)**2)**0.5
            disArredondada = round(dis, 2)
            return disArredondada
        
        d = distanciaAoCentro()
        raio = self.__r
        if d < raio:
            print('\nO ponto informado está contido no círculo')
        else:
            print('\nO ponto informado não está contido no círculo')

class Triangulo(ABC):
    
    def __init__(self, lado1, lado2, lado3, ponto):

        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
        self._ponto = ponto

    
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
    
    def printarInit(self):

        print(f'\nO triângulo tem como lados {self._lado1}, {self._lado2} e {self._lado3} e possui centro em {self._ponto}.\n')

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
        if self._lado1 != self._lado2 and self._lado1 != self._lado3 and self._lado2 != self._lado3:
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
    
    def __init__(self, lado1, lado2, lado3, ponto):
        super().__init__(lado1, lado2, lado3, ponto)

    def getType(self):

        return 'Triângulo_Equilátero_'

    def printaPerimetro(self):

        verificar = self._verificaEquilatero()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                perimetro = self.perimetro()
                print(f'\nO perímetro do triângulo equilátero é {perimetro}\n')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo equilátero, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')
    
    def printarCor(self):

        verificar = self._verificaEquilatero()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                c = input("Escolha a cor do seu triângulo equilátero:")
                self.cor = c
                print(f'A cor do triângulo equilátero é: {self.cor}.')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo equilátero, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

    def area(self):

        verificar = self._verificaEquilatero()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                self.a = ((self._lado1**2 * math.sqrt(3))/4)
                self.areaArredondada = round(self.a, 2)
                return self.areaArredondada
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo equilátero, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

    def printaArea(self):

        verificar = self._verificaEquilatero()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                area = self.areaArredondada
                print(f'\nA área do triângulo equilátero é igual a {area}\n')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo equilátero, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

    def altura(self):

        h = (math.sqrt(3)*self._lado1)/2
        hArredondada = round(h, 2)
        return hArredondada

    def areaAux(self, ponto1, ponto2, ponto3):

        areaAux = abs(0.5*(ponto1.getX()*(ponto2.getY()-ponto3.getY()) + ponto2.getX()*(ponto3.getY()-ponto1.getY()) + ponto3.getX()*(ponto1.getY() - ponto2.getY())))
        return areaAux

    def verificaInterferencias(self, x_p, y_p):

        h = self.altura()
        pontos = {'ponto1': [self._ponto[0], self._ponto[1]+h/2], 'ponto2': [self._ponto[0]-self._lado3/2, self._ponto[1]-h/2], 'ponto3': [self._ponto[0]+self._lado3/2, self._ponto[1]-h/2] }

        ponto1 = Ponto(pontos['ponto1'][0], pontos['ponto1'][1])
        ponto2 = Ponto(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Ponto(pontos['ponto3'][0], pontos['ponto3'][1])
        pontoN = Ponto(x_p, y_p)

        area1 = self.areaAux(ponto1, ponto2, pontoN)
        area2 = self.areaAux(ponto2, ponto3, pontoN)
        area3 = self.areaAux(ponto1, ponto3, pontoN)
        areatotal = self.areaAux(ponto1, ponto2, ponto3)

        if area1 + area2 + area3 == areatotal:
            print('\nO ponto informado está contido no triângulo')
        else:
            print('\nO ponto informado não está contido no triângulo')

class TrianguloIsosceles(Triangulo):
    
    def __init__(self, lado1, lado2, lado3, ponto):
        super().__init__(lado1, lado2, lado3, ponto)

    def getType(self):

        return 'Triângulo_Isósceles_'

    def printaPerimetro(self):

        verificar = self._verificaIsosceles()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                perimetro = self.perimetro()
                print(f'\nO perímetro do triângulo isósceles é {perimetro}.\n')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

    def printarCor(self):

        verificar = self._verificaIsosceles()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                c = input("Escolha a cor do seu triângulo isósceles:")
                self.cor = c
                print(f'A cor do triângulo isósceles é: {self.cor}.')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

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
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                a = (altura * base)/ 2
                areaArredondada = round( a, 2)
                return areaArredondada
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

    def printaArea(self):

        verificar = self._verificaIsosceles()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                area = self.area()
                print(f'\nA área do triângulo isósceles é igual a {area}.\n')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

    def areaAux(self, ponto1, ponto2, ponto3):

        areaAux = abs(0.5*(ponto1.getX()*(ponto2.getY()-ponto3.getY()) + ponto2.getX()*(ponto3.getY()-ponto1.getY()) + ponto3.getX()*(ponto1.getY() - ponto2.getY())))
        return areaAux

    def verificaInterferencias(self, x_p, y_p):

        h = self.altura()
        pontos = {'ponto1': [self._ponto[0], self._ponto[1]+h/2], 'ponto2': [self._ponto[0]-self._lado3/2, self._ponto[1]-h/2], 'ponto3': [self._ponto[0]+self._lado3/2, self._ponto[1]-h/2] }

        ponto1 = Ponto(pontos['ponto1'][0], pontos['ponto1'][1])
        ponto2 = Ponto(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Ponto(pontos['ponto3'][0], pontos['ponto3'][1])
        pontoN = Ponto(x_p, y_p)

        area1 = self.areaAux(ponto1, ponto2, pontoN)
        area2 = self.areaAux(ponto2, ponto3, pontoN)
        area3 = self.areaAux(ponto1, ponto3, pontoN)
        areatotal = self.areaAux(ponto1, ponto2, ponto3)

        if area1 + area2 + area3 == areatotal:
            print('\nO ponto informado está contido no triângulo')
        else:
            print('\nO ponto informado não está contido no triângulo')

class TrianguloEscaleno(Triangulo):
    
    def __init__(self, lado1, lado2, lado3, ponto):
        super().__init__(lado1, lado2, lado3, ponto)

    def getType(self):

        return 'Triângulo_Escaleno_'

    def printaCor(self):

        verificar = self._verificaEscaleno()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                c = input("Escolha a cor do seu triângulo escaleno:")
                self.cor = c
                print(f'A cor do triângulo escaleno é: {self.cor}.')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo escaleno, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

    def printaPerimetro(self):

        verificar = self._verificaEscaleno()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                perimetro = self.perimetro()
                print(f'\nO perímetro do triângulo escaleno é {perimetro}\n')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo escaleno, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')


    def area(self):
        
        s = self._semiperimetro()
        a = (s*((s-self._lado1)*(s-self._lado2)*(s-self._lado3)))**0.5
        return a
    
    def printaArea(self):

        verificar = self._verificaEscaleno()
        desigual = self._desigualdadetriangular()
        if desigual is True:
            if verificar is True:
                area = self.area()
                areaArredondada = round(area, 2)
                print(f'\nA área do triângulo escaleno é {areaArredondada}\n')
            else:
                print('Os valores de lado escolhidos não correspondem a um triângulo escaleno, por favor, informe outros valores')
        else:
            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')

    def altura(self):
        
        s = self._semiperimetro()
        h = (2/self._lado1)*((s*(s-self._lado1)*(s - self._lado2)*(s - self._lado3))**0.5)
        hArre = round(h, 2)
        return hArre

    def areaAux(self, ponto1, ponto2, ponto3):

        areaAux = abs(0.5*(ponto1.getX()*(ponto2.getY()-ponto3.getY()) + ponto2.getX()*(ponto3.getY()-ponto1.getY()) + ponto3.getX()*(ponto1.getY() - ponto2.getY())))
        return areaAux

    def verificaInterferencias(self, x_p, y_p):

        h = self.altura()
        pontos = {'ponto1': [self._ponto[0], self._ponto[1]+h/2], 'ponto2': [self._ponto[0]-self._lado3/2, self._ponto[1]-h/2], 'ponto3': [self._ponto[0]+self._lado3/2, self._ponto[1]-h/2] }

        ponto1 = Ponto(pontos['ponto1'][0], pontos['ponto1'][1])
        ponto2 = Ponto(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Ponto(pontos['ponto3'][0], pontos['ponto3'][1])
        pontoN = Ponto(x_p, y_p)

        area1 = self.areaAux(ponto1, ponto2, pontoN)
        area2 = self.areaAux(ponto2, ponto3, pontoN)
        area3 = self.areaAux(ponto1, ponto3, pontoN)
        areatotal = self.areaAux(ponto1, ponto2, ponto3)

        if area1 + area2 + area3 == areatotal:
            print('\nO ponto informado está contido no triângulo')
        else:
            print('\nO ponto informado não está contido no triângulo')
       

class Quadrado():

    def __init__(self, lado1, lado2, lado3, lado4, ponto):

        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
        self.__lado4 = lado4
        self.__ponto = ponto

    def setLado1(self, lado1):

        if isinstance(lado1, float, int):
            self.__lado1 = lado1
        else:
            self.__lado1 = 0

    def getLado1(self):

        return self.__lado1
    
    def setLado2(self, lado2):

        if isinstance( lado2, float, int):
            self.__lado2 = lado2
        else:
            self.__lado2 = 0

    def getLado2(self):

        return self.__lado2
    
    def setLado3(self, lado3):

        if isinstance(lado3, float, int):
            self.__lado3 = lado3
        else:
            self.__lado3 = 0

    def getLado3(self):

        return self.__lado3
    
    def setLado4(self,lado4):

        if isinstance(lado4, float, int):
            self.__lado4 = lado4
        else:
            self.__lado4 = 0

    def getLado4(self):

        return self.__lado4
    
    def getType(self):

        return 'Quadrado_'
    
    def _verificaQuadrado(self):

        auxiliar = False
        if self.__lado1 == self.__lado2 == self.__lado3 == self.__lado4:
            auxiliar = True
            return auxiliar
        else:
            return auxiliar    
          
    def printarInit(self):

        verificador = self._verificaQuadrado()
        if verificador is True:
            print(f'\nO quadrado tem como lados {self.__lado1}, {self.__lado2}, {self.__lado3} e {self.__lado4} e possui centro em {self.__ponto}.\n')
        else:
            print('Os valores de lado escolhidos não correspondem a um quadrado, por favor, informe outros valores')

    def perimetro(self):

        p = self.__lado1*4
        return p

    def printaPerimentro(self):

        verificador = self._verificaQuadrado()
        if verificador is True:
            perimetro = self.perimetro()
            print(f'\nO perímetro do quadrado é igual a {perimetro}\n')
        else:
            print('Os valores de lado escolhidos não correspondem a um quadrado, por favor, informe outros valores')

    def area(self):

        a = self.__lado1**2
        return a 
    
    def printaArea(self):

        verificador = self._verificaQuadrado()
        if verificador is True:
            area = self.area()
            print(f'\nA área do quadrado é igual a {area}\n')
        else:
            print(f'Os valores de lado escolhidos não correspondem a um quadrado, por favor, informe outros valores')

    def diagonal(self):

        d = self.__lado1 * math.sqrt(2)
        dArredondada = round(d, 2)
        return dArredondada
    
    def printaDiagonal(self):

        verificador = self._verificaQuadrado()
        if verificador is True:
            diagonal = self.diagonal()
            print(f'\nA diagonal do quadrado é igual a {diagonal}\n')
        else:
            print('Os valores de lado escolhidos não correspondem a um quadrado, por favor, informe outros valores')

    def printaCor(self):

        cor = input('Escolha a cor do quadrado:')
        print(f'A cor do quadrado é {cor}.')

    def verificaInterferencias(self, x_p, y_p):
        
        pontos = {'ponto1': [self.__ponto[0]-self.__lado1/2, self.__ponto[1]+self.__lado1/2], 'ponto2': [self.__ponto[0]+self.__lado1/2, self.__ponto[1]+self.__lado1/2], 'ponto3': [self.__ponto[0]-self.__lado1/2, self.__ponto[1]-self.__lado1/2], 'ponto4': [self.__ponto[0] + self.__lado1/2, self.__ponto[1]- self.__lado1/2]}

        if pontos['ponto1'][0] < x_p <= pontos['ponto4'][0] and pontos['ponto4'][1] <= y_p <= pontos['ponto1'][1]:
            print('\nO ponto informado está contido no quadrado.')
        else:
            print('\nO ponto inforado não está contido nesse quadrado.')

class Poligono(ABC):
    
    def __init__(self, lado, ponto): 

        self._lado = lado
        self._ponto = ponto

    def setLado(self, lado):

        if isinstance(lado, float, int):
            self._lado = self._lado
        else:
            self._lado = 0

    def getLado(self):

        return self._lado

    def perimetro(self):

        p = self.i * self._lado
        return p
    
    @abstractmethod
    def area(self):
        pass

    def setCor(self, cor):

        self._cor = cor

    def areaAux(self, ponto1, ponto2, ponto3):

        area1 = abs(0.5*(ponto1.getX()*(ponto2.getY()-ponto3.getY()) + ponto2.getX()*(ponto3.getY()-ponto1.getY()) + ponto3.getX()*(ponto1.getY()- ponto2.getY())))
        area1Arre = round(area1, 2)
        return area1Arre

class Pentagono(Poligono):

    def __init__(self, lado, ponto):
        super().__init__(lado, ponto)
        self.i = 5

    def getType(self):

        return 'Pentágono_'

    def printarInit(self):

        print(f'\nOs lados do pentágono regular são {self._lado}, {self._lado}, {self._lado}, {self._lado} e {self._lado} e possui centro em {self._ponto}. \n')

    def printaPerimetro(self):

        perimetro = self.perimetro()
        print(f'\nO perímetro do pentágono é igual a {perimetro}.\n')

    def area(self): #polimorfismo na classe filha
        
        auxiliador = math.tan(36)
        a = (5*self._lado**2)/(4*auxiliador)
        aArredondada = round(a, 2)
        return aArredondada
    
    def printaArea(self):

        area = self.area()
        print(f'\nA área do pentágono regular é igual a {area}\n')

    def printaCor(self):

        cor = input('Escolha a cor do pentágono regular:')
        print(f'A cor do pentágono regular é {cor}.')

    def raio(self):

        seno = math.sin(pi/5)
        raio = self._lado/(2*seno)
        return raio 

    def verificaInterferencias(self, x_p, y_p):
         
        raio = self.raio()
        pontos = {
            'ponto1': [self._ponto[0] + raio*math.cos(0), self._ponto[1] + raio*math.sin(0)],
            'ponto2': [self._ponto[0] + raio*math.cos(2*pi/5), self._ponto[1] + raio*math.sin(2*pi/5)],
            'ponto3': [self._ponto[0] + raio*math.cos(4*pi/5), self._ponto[1] + raio*math.sin(4*pi/5)],
            'ponto4': [self._ponto[0] + raio*math.cos(6*pi/5), self._ponto[1] + raio*math.sin(6*pi/5)],
            'ponto5': [self._ponto[0] + raio*math.cos(8*pi/5), self._ponto[1] + raio*math.sin(8*pi/5)]
        }

        ponto1 = Ponto(pontos['ponto1'][0], pontos['ponto1'][1])
        ponto2 = Ponto(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Ponto(pontos['ponto3'][0], pontos['ponto3'][1])
        ponto4 = Ponto(pontos['ponto4'][0], pontos['ponto4'][1])
        ponto5 = Ponto(pontos['ponto5'][0], pontos['ponto5'][1])
        pontoN = Ponto(x_p, y_p)
        centro = Ponto(self._ponto[0],self._ponto[1])

        areaN1 = self.areaAux(ponto1, ponto2, pontoN)
        areaN2 = self.areaAux(ponto2, ponto3, pontoN)
        areaN3 = self.areaAux(ponto3, ponto4, pontoN)
        areaN4 = self.areaAux(ponto4, ponto5, pontoN)
        areaN5 = self.areaAux(ponto5, ponto1, pontoN)

        areaC1 = self.areaAux(ponto1, ponto2, centro)
        areaC2 = self.areaAux(ponto2, ponto3, centro)
        areaC3 = self.areaAux(ponto3, ponto4, centro)
        areaC4 = self.areaAux(ponto4, ponto5, centro)
        areaC5 = self.areaAux(ponto5, ponto1, centro)

        somaAreaC = areaC1 + areaC2 + areaC3 + areaC4 + areaC5
        somaAreaN = areaN1 + areaN2 + areaN3 + areaN4 + areaN5
        if somaAreaC == somaAreaN:
            print('\nO ponto informado está contido no pentágono.')
        else:
            print('\nO ponto informado não está contido no pentágono.')

class Hexagono(Poligono):

    def __init__(self, lado, ponto):
        super().__init__(lado, ponto)
        self.i = 6

    def getType(self):

        return 'Hexágono_'

    def printarInit(self):

        print(f'\nOs lados do hexágono regular são {self._lado}, {self._lado}, {self._lado}, {self._lado}, {self._lado} e {self._lado} e possui centro em {self._ponto}. \n')

    def printaPerimetro(self):

        perimetro = self.perimetro()
        print(f'\nO perímetro do hexágono é igual a {perimetro}.\n')

    def area(self): #polimorfismo na classe filha
        a = (3*self._lado**2*math.sqrt(3))/2
        aArredondada = round(a, 2)
        return aArredondada
    
    def printaArea(self):

        area = self.area()
        print(f'\nA área do hexágono regular é igual a {area}\n')

    def printaCor(self):

        cor = input('Escolha a cor do hexágono regular:')
        print(f'A cor do hexágono regular é {cor}.')

    def verificaInterferencias(self, x_p, y_p):
        
        c = self._ponto[0] + self._ponto[1]
        pontos = {
            'ponto1': [self._ponto[0]+ c*math.cos(0), self._ponto[1]+ c*math.sin(0)],
            'ponto2': [self._ponto[0]+ c *math.cos(pi/3), self._ponto[1]+ c * math.sin(pi/3)],
            'ponto3': [self._ponto[0]+ c *math.cos(2*pi/3), self._ponto[1]+ c * math.sin(2*pi/3)],
            'ponto4': [self._ponto[0]+ c *math.cos(pi), self._ponto[1]+ c * math.sin(pi)],
            'ponto5': [self._ponto[0]+ c *math.cos(4*pi/3), self._ponto[1]+ c * math.sin(4*pi/3)],
            'ponto6': [self._ponto[0]+ c *math.cos(5*pi/3), self._ponto[1]+ c * math.sin(5*pi/3)],
        }

        ponto1 = Ponto(pontos['ponto1'][0], pontos['ponto1'][1])
        ponto2 = Ponto(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Ponto(pontos['ponto3'][0], pontos['ponto3'][1])
        ponto4 = Ponto(pontos['ponto4'][0], pontos['ponto4'][1])
        ponto5 = Ponto(pontos['ponto5'][0], pontos['ponto5'][1])
        ponto6 = Ponto(pontos['ponto6'][0], pontos['ponto6'][1])
        pontoN = Ponto(x_p, y_p)
        centro = Ponto(self._ponto[0],self._ponto[1])

        areaN1 = self.areaAux(ponto1, ponto2, pontoN)
        areaN2 = self.areaAux(ponto2, ponto3, pontoN)
        areaN3 = self.areaAux(ponto3, ponto4, pontoN)
        areaN4 = self.areaAux(ponto4, ponto5, pontoN)
        areaN5 = self.areaAux(ponto5, ponto6, pontoN)
        areaN6 = self.areaAux(ponto6, ponto1, pontoN)

        areaC1 = self.areaAux(ponto1, ponto2, centro)
        areaC2 = self.areaAux(ponto2, ponto3, centro)
        areaC3 = self.areaAux(ponto3, ponto4, centro)
        areaC4 = self.areaAux(ponto4, ponto5, centro)
        areaC5 = self.areaAux(ponto5, ponto6, centro)
        areaC6 = self.areaAux(ponto6, ponto1, centro)

        somaAreaC = areaC1 + areaC2 + areaC3 + areaC4 + areaC5 + areaC6
        somaArea = areaN1 + areaN2 + areaN3 + areaN4 + areaN5 + areaN6
        if somaAreaC == somaArea:
            print('\nO ponto informado está contido no hexágono.')
        else:
            print('\nO ponto informado não está contido no hexágono.')       

class Heptagono(Poligono):

    def __init__(self, lado, ponto):
        super().__init__(lado, ponto)
        self.i = 7

    def getType(self):

        return 'Heptágono_'

    def printarInit(self):

        print(f'\nOs lados do heptágono regular são {self._lado}, {self._lado}, {self._lado}, {self._lado}, {self._lado}, {self._lado} e {self._lado} e possui centro em {self._ponto}. \n')

    def printaPerimetro(self):

        perimetro = self.perimetro()
        print(f'\nO perímetro do heptágono é igual a {perimetro}.\n')

    def area(self): #polimorfismo na classe filha

        a = (3.634*self._lado**2)
        aArredondada = round(a, 2)
        return aArredondada
    
    def printaArea(self):

        area = self.area()
        print(f'\nA área do heptágono regular é igual a {area}.\n')

    def printaCor(self):

        cor = input('Escolha a cor do heptágono regular:')
        print(f'A cor do heptágono regular é {cor}.')

    def raio(self):
        
        r = (self._lado)/2*math.sin(pi/7)
        rArre = round(r, 2)
        return rArre

    def verificaInterferencias(self, x_p, y_p):

        raio = self.raio()
        pontos = {
            'ponto1': [self._ponto[0]+ raio*math.cos(0), self._ponto[1]+ raio*math.sin(0)],
            'ponto2': [self._ponto[0]+ raio *math.cos(((2*pi)/7)), self._ponto[1]+ raio * math.sin(((2*pi)/7))],
            'ponto3': [self._ponto[0]+ raio *math.cos(((2*pi)/7)*2), self._ponto[1]+ raio * math.sin(((2*pi)/7)*2)],
            'ponto4': [self._ponto[0]+ raio *math.cos(((2*pi)/7)*3), self._ponto[1]+ raio * math.sin(((2*pi)/7)*3)],
            'ponto5': [self._ponto[0]+ raio *math.cos(((2*pi)/7)*4), self._ponto[1]+ raio * math.sin(((2*pi)/7)*4)],
            'ponto6': [self._ponto[0]+ raio *math.cos(((2*pi)/7)*5), self._ponto[1]+ raio * math.sin(((2*pi)/7)*5)],
            'ponto7': [self._ponto[0]+ raio *math.cos(((2*pi)/7)*6), self._ponto[1]+ raio * math.sin(((2*pi)/7)*6)],
        }

        ponto1 = Ponto(pontos['ponto1'][0], pontos['ponto1'][1])
        ponto2 = Ponto(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Ponto(pontos['ponto3'][0], pontos['ponto3'][1])
        ponto4 = Ponto(pontos['ponto4'][0], pontos['ponto4'][1])
        ponto5 = Ponto(pontos['ponto5'][0], pontos['ponto5'][1])
        ponto6 = Ponto(pontos['ponto6'][0], pontos['ponto6'][1])
        ponto7 = Ponto(pontos['ponto7'][0], pontos['ponto7'][1])
        pontoN = Ponto(x_p, y_p)
        centro = Ponto(self._ponto[0],self._ponto[1])

        areaN1 = self.areaAux(ponto1, ponto2, pontoN)
        areaN2 = self.areaAux(ponto2, ponto3, pontoN)
        areaN3 = self.areaAux(ponto3, ponto4, pontoN)
        areaN4 = self.areaAux(ponto4, ponto5, pontoN)
        areaN5 = self.areaAux(ponto5, ponto6, pontoN)
        areaN6 = self.areaAux(ponto6, ponto7, pontoN)
        areaN7 = self.areaAux(ponto7, ponto1, pontoN)

        areaC1 = self.areaAux(ponto1, ponto2, centro)
        areaC2 = self.areaAux(ponto2, ponto3, centro)
        areaC3 = self.areaAux(ponto3, ponto4, centro)
        areaC4 = self.areaAux(ponto4, ponto5, centro)
        areaC5 = self.areaAux(ponto5, ponto6, centro)
        areaC6 = self.areaAux(ponto6, ponto7, centro)
        areaC7 = self.areaAux(ponto7, ponto1, centro)

        somaAreaC = areaC1 + areaC2 + areaC3 + areaC4 + areaC5 + areaC6 + areaC7
        somaArea = areaN1 + areaN2 + areaN3 + areaN4 + areaN5 + areaN6 + areaN7
        if somaAreaC == somaArea:
            print('\nO ponto informado está contido no heptágono.')
        else:
            print('\nO ponto informado não está contido no heptágono.')              

class Octogono(Poligono):

    def __init__(self, lado, ponto):
        super().__init__(lado, ponto)
        self.i = 8

    def getType(self):

        return 'Octógono_'

    def printarInit(self):

        print(f'\nOs lados do octógono regular são {self._lado}, {self._lado}, {self._lado}, {self._lado}, {self._lado}, {self._lado}, {self._lado} e {self._lado} e possui centro em {self._ponto}. \n')

    def printaPerimetro(self):

        perimetro = self.perimetro()
        print(f'\nO perímetro do octógono é igual a {perimetro}.\n')

    def area(self): #polimorfismo na classe filha

        a = (2*(1 + math.sqrt(2)*self._lado**2))
        aArredondada = round(a, 2)
        return aArredondada
    
    def printaArea(self):

        area = self.area()
        print(f'\nA área do octógono regular é igual a {area}.\n')

    def printaCor(self):

        cor = input('Escolha a cor do octógono regular:')
        print(f'A cor do octógono regular é {cor}.')

    def raio(self):
        
        r = (self._lado)/2*math.sin(pi/8)
        rArre = round(r, 2)
        return rArre

    def verificaInterferencias(self, x_p, y_p):

        raio = self.raio()
        pontos = {
            'ponto1': [self._ponto[0]+ raio*math.cos(0), self._ponto[1]+ raio*math.sin(0)],
            'ponto2': [self._ponto[0]+ raio *math.cos((pi/4)), self._ponto[1]+ raio * math.sin((pi/4))],
            'ponto3': [self._ponto[0]+ raio *math.cos((pi/4)*2), self._ponto[1]+ raio * math.sin((pi/4)*2)],
            'ponto4': [self._ponto[0]+ raio *math.cos((pi/4)*3), self._ponto[1]+ raio * math.sin((pi/4)*3)],
            'ponto5': [self._ponto[0]+ raio *math.cos((pi/4)*4), self._ponto[1]+ raio * math.sin((pi/4)*4)],
            'ponto6': [self._ponto[0]+ raio *math.cos((pi/4)*5), self._ponto[1]+ raio * math.sin((pi/4)*5)],
            'ponto7': [self._ponto[0]+ raio *math.cos((pi/4)*6), self._ponto[1]+ raio * math.sin((pi/4)*6)],
            'ponto8': [self._ponto[0]+ raio *math.cos((pi/4)*7), self._ponto[1]+ raio * math.sin((pi/4)*7)],
        }

        ponto1 = Ponto(pontos['ponto1'][0], pontos['ponto1'][1])
        ponto2 = Ponto(pontos['ponto2'][0], pontos['ponto2'][1])
        ponto3 = Ponto(pontos['ponto3'][0], pontos['ponto3'][1])
        ponto4 = Ponto(pontos['ponto4'][0], pontos['ponto4'][1])
        ponto5 = Ponto(pontos['ponto5'][0], pontos['ponto5'][1])
        ponto6 = Ponto(pontos['ponto6'][0], pontos['ponto6'][1])
        ponto7 = Ponto(pontos['ponto7'][0], pontos['ponto7'][1])
        ponto8 = Ponto(pontos['ponto8'][0], pontos['ponto8'][1])
        pontoN = Ponto(x_p, y_p)
        centro = Ponto(self._ponto[0],self._ponto[1])

        areaN1 = self.areaAux(ponto1, ponto2, pontoN)
        areaN2 = self.areaAux(ponto2, ponto3, pontoN)
        areaN3 = self.areaAux(ponto3, ponto4, pontoN)
        areaN4 = self.areaAux(ponto4, ponto5, pontoN)
        areaN5 = self.areaAux(ponto5, ponto6, pontoN)
        areaN6 = self.areaAux(ponto6, ponto7, pontoN)
        areaN7 = self.areaAux(ponto7, ponto8, pontoN)
        areaN8 = self.areaAux(ponto8, ponto1, pontoN)

        areaC1 = self.areaAux(ponto1, ponto2, centro)
        areaC2 = self.areaAux(ponto2, ponto3, centro)
        areaC3 = self.areaAux(ponto3, ponto4, centro)
        areaC4 = self.areaAux(ponto4, ponto5, centro)
        areaC5 = self.areaAux(ponto5, ponto6, centro)
        areaC6 = self.areaAux(ponto6, ponto7, centro)
        areaC7 = self.areaAux(ponto7, ponto8, centro)
        areaC8 = self.areaAux(ponto8, ponto1, centro)

        somaAreaC = areaC1 + areaC2 + areaC3 + areaC4 + areaC5 + areaC6 + areaC7 + areaC8
        somaArea = areaN1 + areaN2 + areaN3 + areaN4 + areaN5 + areaN6 + areaN7 + areaN8
        if somaAreaC == somaArea:
            print('\nO ponto informado está contido no octógono.')
        else:
            print('\nO ponto informado não está contido no octógono.')     

class Retangulo():
    
    def __init__(self, lado1, lado2, ponto):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__ponto = ponto

    def setLado1(self, lado1):

        if isinstance(lado1, int):
            self.__lado1 = lado1
        else:
            self.__lado1 = 0

    def getLado1(self):

        return self.__lado1
    
    def setLado2(self, lado2):

        if isinstance( lado2, int):
            self.__lado2 = lado2
        else:
            self.__lado2 = 0

    def getLado2(self):

        return self.__lado2
    
    def getType(self):

        return 'Retângulo_'
    
    def printarInit(self):

        print(f'\nO retângulo tem como lados {self.__lado1}, {self.__lado2}, {self.__lado1} e {self.__lado2} e possui centro em {self.__ponto}.\n')

    def perimetro(self):

        p = self.__lado1*2 + self.__lado2*2
        return p

    def printaPerimentro(self):

        perimetro = self.perimetro()
        print(f'\nO perímetro do retângulo é igual a {perimetro}.\n')

    def area(self):

        a = self.__lado1*self.__lado2
        return a 
    
    def printaArea(self):

            area = self.area()
            print(f'\nA área do retângulo é igual a {area}.\n')

    def diagonal(self):

        d = self.__lado1**2 + self.__lado2**2
        aux = math.sqrt(d)
        dArrendondada = round(aux, 2)
        return dArrendondada
    
    def printaDiagonal(self):

            diagonal = self.diagonal()
            print(f'\nA diagonal do retângulo é igual a {diagonal}.\n')

    def printaCor(self):

        cor = input('Escolha a cor do retângulo:')
        print(f'A cor do retângulo é {cor}.')

    def verificaInterferencias(self, x_p, y_p):

        pontos = {
            'ponto1': [self.__ponto[0]-self.__lado1/2, self.__ponto[1]+self.__lado2/2], 'ponto2': [self.__ponto[0]+self.__lado1/2, self.__ponto[1]+self.__lado2/2], 'ponto3': [self.__ponto[0]-self.__lado1/2, self.__ponto[1]-self.__lado2/2], 'ponto4': [self.__ponto[0]+self.__lado1/2, self.__ponto[1]-self.__lado2/2]
        }

        if pontos['ponto1'][0] <= x_p <= pontos['ponto4'][0] and pontos['ponto3'][1] <= y_p <= pontos['ponto2'][1]:
            print('\nO ponto informado está contido no retângulo.')
        else:
            print('\nO ponto informado não está contido no retângulo.')
