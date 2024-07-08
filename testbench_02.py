from package.maths.terms import Circulo, Ponto


def criarCirculo():
    objeto = Ponto(2, 3)
    circulo1 = Circulo(objeto.centro(), 5)
    circulo1.printarInit()
    circulo1.printaDiametro()
    circulo1.printarArea()
    circulo1.printarComprimento()
    circulo1.printarCor()

criarCirculo()
