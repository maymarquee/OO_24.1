from package.maths.terms import Retangulo

def criaRetangulo():
    quadrado1 = Retangulo(2, 4)
    quadrado1.printarInit()
    quadrado1.printaCor()
    quadrado1.printaPerimentro()
    quadrado1.printaArea()
    quadrado1.printaDiagonal()

if __name__ == "__main__":
    criaRetangulo()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")