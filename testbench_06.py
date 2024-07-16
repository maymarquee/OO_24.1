from package.maths.terms import TrianguloEscaleno

def criaTrianguloEscaleno():
    triangulo3 = TrianguloEscaleno(10, 5, 13)
    triangulo3.printaInfosBasicas()
    triangulo3.printaCor()
    triangulo3.printaPerimetro()
    triangulo3.printaArea()

if __name__ == "__main__":
    criaTrianguloEscaleno()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")