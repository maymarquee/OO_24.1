from package.maths.terms import Heptagono

def criarHeptagono():
    n = int(input('Informe um lado do seu heptágono regular:'))
    heptagono1 = Heptagono(n)
    heptagono1.printaCor()
    heptagono1.printaInfosBasicas()
    heptagono1.printaPerimetro()
    heptagono1.printaArea()

criarHeptagono()