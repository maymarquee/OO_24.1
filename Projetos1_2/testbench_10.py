from package.maths.terms import Heptagono

def criarHeptagono():
    n = int(input('Informe um lado do seu heptágono regular:'))
    heptagono1 = Heptagono(n)
    heptagono1.printaCor()
    heptagono1.printarInit()
    heptagono1.printaPerimetro()
    heptagono1.printaArea()

if __name__ == "__main__":
    criarHeptagono()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")