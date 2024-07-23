from package.maths.terms import Hexagono

def criarHexagono():
    n = int(input('Informe um lado do seu hexágono regular:'))
    hexagono1 = Hexagono(n)
    hexagono1.printaCor()
    hexagono1.printarInit()
    hexagono1.printaPerimetro()
    hexagono1.printaArea()

if __name__ == "__main__":
    criarHexagono()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")