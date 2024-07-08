from package.maths.terms import Quadrado

def criaQuadrado():
    quadrado1 = Quadrado(2, 2, 2, 2)
    quadrado1.printaInfosBasicas()
    quadrado1.printaCor()
    quadrado1.printaPerimentro()
    quadrado1.printaArea()
    quadrado1.printaDiagonal()

criaQuadrado()