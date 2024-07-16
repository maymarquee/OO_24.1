from package.maths.terms import TrianguloEquilatero

def criarTrianguloEquilatero():
    
    triangulo1 = TrianguloEquilatero(5, 5, 5)
    triangulo1.printaInfosBasicas()
    triangulo1.printarCor()
    triangulo1.printaPerimetro()
    triangulo1.area()
    triangulo1.printaArea()

if __name__ == "__main__":
    criarTrianguloEquilatero()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")