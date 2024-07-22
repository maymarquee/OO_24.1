from package.maths.terms import Reta


def criaReta():

    segmento_1 = Reta(1, 3, 7, 4)
    segmento_1.printarInit()
    segmento_1.printaInterpolar()
    segmento_1.printarCor()


if __name__ == "__main__":
    criaReta()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")