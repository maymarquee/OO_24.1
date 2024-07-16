from package.maths.terms import TrianguloIsosceles

def criarTrianguloIsosceles():

    triangulo2 = TrianguloIsosceles(2, 2, 1)
    triangulo2.printaInfosBasicas()
    triangulo2.printarCor()
    triangulo2.printaPerimetro()
    triangulo2.printaArea()

if __name__ == "__main__":
    criarTrianguloIsosceles()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")