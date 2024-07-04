from package.maths.terms import Circulo


def criarCirculo():
    
    circulo1 = Circulo(4,2,5)
    #circulo1.setCor('vermelho')
    circulo1.printarInit()
    circulo1.printaDiametro()
    circulo1.printarArea()
    circulo1.printarComprimento()
    circulo1.printarCor()

criarCirculo()
