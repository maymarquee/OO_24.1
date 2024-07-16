from package.maths.terms import Pentagono

def criaPentagono():
    n = int(input('Informe um lado do seu pentágono regular:'))
    petagono1 = Pentagono(n)
    petagono1.printaCor()
    petagono1.printaInfosBasicas()
    petagono1.printaPerimetro()
    petagono1.printaArea()

if __name__ == "__main__":
    criaPentagono()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")
