from package.maths.terms import Reta


def workspace():

    segmento_1 = Reta(1, 3, 7, 4)
    segmento_1.model()
    segmento_1.printaInterpolar()
    segmento_1.printarCor()


if __name__ == "__main__":

    print("O arquivo 'testbench.py' foi envocado como programa")
    workspace()

else:

    print("o arquivo 'testbench.py' foi envocado como modulo")