from package.maths.terms import Quadrado

def criaQuadrado():
    quadrado1 = Quadrado(2, 2, 2, 2)
    quadrado1.printarInit()
    quadrado1.printaCor()
    quadrado1.printaPerimentro()
    quadrado1.printaArea()
    quadrado1.printaDiagonal()

if __name__ == "__main__":
    criaQuadrado()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")