from package.maths.terms import Octogono

def criarOctogono():
    n = int(input('Informe um lado do seu octógono regular:'))
    Octogono1 = Octogono(n)
    Octogono1.printaCor()
    Octogono1.printaInfosBasicas()
    Octogono1.printaPerimetro()
    Octogono1.printaArea()

if __name__ == "__main__":
    criarOctogono()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")