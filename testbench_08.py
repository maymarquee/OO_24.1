from package.maths.terms import Pentagono

def criaPentagono():
    n = int(input('Informe um lado do seu pentágono regular:'))
    petagono1 = Pentagono(n)
    petagono1.printaCor()
    petagono1.printaInfosBasicas()
    petagono1.printaPerimetro()
    petagono1.printaArea()


criaPentagono()
