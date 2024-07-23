from package.maths.terms import Circulo, Ponto


def criarCirculo():
    objeto = Ponto(2, 3)
    circulo1 = Circulo(objeto.centro(), 5)
    circulo1.printarInit()
    circulo1.printaDiametro()
    circulo1.printarArea()
    circulo1.printarComprimento()
    circulo1.printarCor()

if __name__ == "__main__":
    criarCirculo()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")
