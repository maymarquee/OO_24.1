from package.maths.terms import Ponto

def criarPonto():

    ponto1 = Ponto(7,3)
    ponto1.printarInit()
    ponto1.printaDistancia()
    ponto1.printarCor()

if __name__ == "__main__":
    criarPonto()
else:
    print("o arquivo 'testbench.py' foi envocado como modulo, envoque-o como programa")
