from package.maths.terms import Hexagono

def criarHexagono():
    n = int(input('Informe um lado do seu hexágono regular:'))
    hexagono1 = Hexagono(n)
    hexagono1.printaCor()
    hexagono1.printaInfosBasicas()
    hexagono1.printaPerimetro()
    hexagono1.printaArea()

criarHexagono()