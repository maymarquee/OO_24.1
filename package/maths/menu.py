from package.maths.terms import *

class PlanoCartesiano(): #classe controladora de criação e exclusão de formas geométricas
    
    def __init__(self):

        self.formas = {}
        self.contagem = 0

    def inserirForma(self, formas):

        self.contagem += 1
        self.formas[formas.getType() + str(self.contagem)] = formas

    def removerForma(self, formas): #remove, a partir da entrada do usuário, a forma geométrica escolhida
        
        del self.formas[formas.getType() + str(self.contagem)]

    def listarFormas(self): #printa as formas geométricas criadas

        print('\nAs formas geométricas criadas neste plano cartesiano são:\n')
        for lista in self.formas.keys():
            print(lista)
    
    def printaInfos(self):

        for chave in self.formas.keys():
            self.formas[chave].printarInit()

    def retornarFormas(self, identificacao):

        return self.formas[identificacao]
    
    def printaContagem(self):

        print(f'\nO número de formas geómetricas criadas é igual a: {self.contagem}\n')
    

class Menu():
    
    def __init__(self):

        self.dashboard = PlanoCartesiano()
        self.acoes = {
            'Criar_forma' : self.criar,
            'Interferencia_entre_formas' : self.crash,
            'Listagem' : self.listar,
            'Quantidade' : self.contar,
            'Sair' : exit
        }

    def criar(self):

        print('Você pode criar as seguintes formas geométricas: ')
        print('1. Ponto')
        print('2. Reta')
        print('3. Círculo')
        print('4. Triângulo Equilátero')
        print('5. Triângulo Isósceles')
        print('6. Triângulo Escaleno')
        print('7. Quadrado')
        print('8. Pentágono')
        print('9. Hexágono')
        print('10. Heptágono')
        print('11. Octógono')
        print('12. Retângulo')

        escolha = input('Digite o número da opção escolhida: ')

        if escolha.isdigit():

            escolha = int(escolha)

            if escolha == 1: 
                while True:
                    try:
                        x = int(input('Escolha a coordenada de x do ponto: '))
                        y = int(input('Escolha a coordenada de y do ponto: '))
                        break
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                        
                objponto = Ponto(x, y)
                self.dashboard.inserirForma(objponto)

                print('Escolha o que deseja fazer com o ponto criado:')
                print('1. Printar as coordenadas')
                print('2. Calcular a distância do ponto ao centro')
                print('3. Calcular distância entre pontos')

                escolha2 = input('Digite a opção escolhida:')

                if escolha2.isdigit():

                    escolha2 = int(escolha2)
                    if escolha2 == 1:
                        objponto.printarInit()
                    elif escolha2 == 2:
                        objponto.printaDistancia()
                    elif escolha2 == 3:
                        while True:
                            try:
                                x_p = int(input('Escolha a coordenada de x do novo ponto: '))
                                y_p = int(input('Escolha a coordenada de y do novo ponto: '))
                                break
                            except ValueError:
                                print('O valor inserido não é válido. Insira um número')

                        objponto.printaDistaPontos(x_p, y_p)
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                        print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')
            
            elif escolha == 2:
                while True:
                    try:
                        x1 = int(input('Escolha a coordenada do x1 da reta: '))
                        y1 = int(input('Escolha a coordenada de y1 da reta: '))
                        x2 = int(input('Escolha a coordenada do x2 da reta: '))
                        y2 = int(input('Escolha a coordenada do y2 da reta: '))
                        break
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                objreta = Reta(x1, y1, x2, y2)
                self.dashboard.inserirForma(objreta) 

                print('Escolha o que deseja fazer com a reta criado:')
                print('1. Printar as coordenadas')
                print('2. Calcular a dimensão da reta')
                print('3. Interpolar um valor à reta')

                escolha3 = input('Digite a opção escolhida:')

                if escolha3.isdigit():

                    escolha3 = int(escolha3)
                    if escolha3 == 1:
                        objreta.printarInit()
                    elif escolha3 == 2:
                        objreta.printarDistanciaPontos()
                    elif escolha3 == 3:
                        objreta.printaInterpolar()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                        print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 3:
                while True:
                    try:
                        x_centro = int(input('Escolha a coordenada x do centro do círculo: '))
                        y_centro = int(input('Escolha a coordenada y do centro do círculo: '))
                        raio = int(input('Escolha o raio do círculo: '))
                        break
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                objpontoc = Ponto(x_centro, y_centro)
                centro = objpontoc.centro()
                objcirculo = Circulo(centro, raio)
                self.dashboard.inserirForma(objcirculo)

                print('Escolha o que deseja fazer com o círculo criado:')
                print('1. Printar as informações do círculo')
                print('2. Calcular o diâmetro do círculo')
                print('3. Calcular a área do círculo')
                print('4. Calcular o comprimento do círculo')

                escolha4 = input('Digite a opção escolhida:')

                if escolha4.isdigit():

                    escolha4 = int(escolha4)
                    if escolha4 == 1:
                        objcirculo.printarInit()
                    elif escolha4 == 2:
                        objcirculo.printaDiametro()
                    elif escolha4 == 3:
                        objcirculo.printarArea()
                    elif escolha4 == 4:
                        objcirculo.printarComprimento()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else: 
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 4:
                while True:
                    try:
                        lado1_teq = int(input('Escolha o lado 1 do triângulo: '))
                        lado2_teq = int(input('Escolha o lado 2 do triângulo: '))
                        lado3_teq = int(input('Escolha o lado 3 do triângulo: '))
                        x_teq = int(input('Escolha a coordenada x do centro do triângulo: '))
                        y_teq = int(input('Escolha a coordenada y do centro do triângulo: '))

                        verificador1 = Triangulo(lado1_teq, lado2_teq, lado3_teq, None)
                        verificador6 = Triangulo(lado1_teq, lado2_teq, lado3_teq, None)
                        z1 = verificador1._verificaEquilatero() 
                        z6 = verificador6._desigualdadetriangular()
                        
                        if z6 == True:
                            if z1 == True:

                                objpontoteq = Ponto(x_teq, y_teq)
                                centroteq = objpontoteq.centro()
                                objtrianguloeq = TrianguloEquilatero(lado1_teq, lado2_teq, lado3_teq, centroteq)
                                self.dashboard.inserirForma(objtrianguloeq)
                                break
                            else:
                                print('Os valores de lado escolhidos não correspondem a um triângulo equiláero, por favor, informe outros valores')
                        else:
                            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                print('Escolha o que deseja fazer com o triângulo criado: ')
                print('1. Printar informações do triângulo')
                print('2. Calcular o perímetro do triângulo')
                print('3. Calcular a área do triângulo')

                escolha5 = input('Digite a opção escolhida:')

                if escolha5.isdigit():

                    escolha5 = int(escolha5)
                    if escolha5 == 1:
                        objtrianguloeq.printarInit()
                    elif escolha5 == 2:
                        objtrianguloeq.printaPerimetro()
                    elif escolha5 == 3:
                        objtrianguloeq.area()
                        objtrianguloeq.printaArea()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 5:
                while True:
                    try:
                        lado1_ti = int(input('Escolha o lado 1 do triângulo: '))
                        lado2_ti = int(input('Escolha o lado 2 do triângulo: '))
                        lado3_ti = int(input('Escolha o lado 3 do triângulo: '))
                        x_tis = int(input('Escolha a coordenada x do centro do triângulo: '))
                        y_tis = int(input('Escolha a coordenada y do centro do triângulo: '))
                        
                        verificador5 = Triangulo(lado1_ti, lado2_ti, lado3_ti, None)
                        verificador = Triangulo(lado1_ti, lado2_ti, lado3_ti, None)
                        z = verificador._verificaIsosceles() 
                        z5 = verificador5._desigualdadetriangular()

                        if z5 == True:
                            if z == True:
                                objpontotis = Ponto(x_tis, y_tis)
                                centrotis = objpontotis.centro()
                                objtriangulois = TrianguloIsosceles(lado1_ti, lado2_ti, lado3_ti, centrotis)
                                self.dashboard.inserirForma(objtriangulois)
                                break
                            else:
                                print('Os valores de lado escolhidos não correspondem a um triângulo isósceles, por favor, informe outros valores')
                        else:
                            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')


                print('Escolha o que deseja fazer com o triângulo criado: ')
                print('1. Printar informações do triângulo')
                print('2. Calcular o perímetro do triângulo')
                print('3. Calcular a área do triângulo')

                escolha6 = input('Digite a opção escolhida: ')

                if escolha6.isdigit():

                    escolha6 = int(escolha6)
                    if escolha6 == 1:
                        objtriangulois.printarInit()
                    elif escolha6 == 2:
                        objtriangulois.printaPerimetro()
                    elif escolha6 == 3:
                        objtriangulois.printaArea()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 6:
                while True:
                    try:
                        lado1_tes = int(input('Escolha o lado 1 do triângulo: '))
                        lado2_tes = int(input('Escolha o lado 2 do triângulo: '))
                        lado3_tes = int(input('Escolha o lado 3 do triângulo: '))
                        x_tes = int(input('Escolha a coordenada x do centro do triângulo: '))
                        y_tes = int(input('Escolha a coordenada y do centro do triângulo: '))

                        verificador2 = Triangulo(lado1_tes, lado2_tes, lado3_tes, None)
                        verificador4 = Triangulo(lado1_tes, lado2_tes, lado3_tes, None)
                        z4 = verificador4._desigualdadetriangular()
                        z2 = verificador2._verificaEscaleno() 
                        if z4 == True:
                            if z2 == True:
                                objpontotes = Ponto(x_tes, y_tes)
                                centrotes = objpontotes.centro()
                                objtrianguloes = TrianguloEscaleno(lado1_tes, lado2_tes, lado3_tes, centrotes)
                                self.dashboard.inserirForma(objtrianguloes)
                                break
                            else:
                                print('Os valores de lado escolhidos não correspondem a um triângulo escaleno, por favor, informe outros valores')
                        else:
                            print('Os valores escolhidos não formam um triângulo, por favor, informe outros valores.')
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                print('Escolha o que deseja fazer com o triângulo criado: ')
                print('1. Printar informações do triângulo')
                print('2. Calcular o perímetro do triângulo')
                print('3. Calcular a área do triângulo')

                escolha7 = input('Digite a opção escolhida: ')

                if escolha7.isdigit():

                    escolha7 = int(escolha7)
                    if escolha7 == 1:
                        objtrianguloes.printarInit()
                    elif escolha7 == 2:
                        objtrianguloes.printaPerimetro()
                    elif escolha7 == 3:
                        objtrianguloes.printaArea()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.') 
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 7:
                while True:
                    try:
                        lado1_qua = int(input('Escolha o lado 1 do quadrado: '))
                        lado2_qua = int(input('Escolha o lado 2 do quadrado: '))
                        lado3_qua = int(input('Escolha o lado 3 do quadrado: '))
                        lado4_qua = int(input('Escolha o lado 4 do quadrado: '))
                        x_qua = int(input('Escolha a coordenada x do centro do quadrado: '))
                        y_qua = int(input('Escolha a coordenada y do centro do quadrado: '))

                        verificador3 = Quadrado(lado1_qua, lado2_qua, lado3_qua, lado4_qua, None)
                        z3 = verificador3._verificaQuadrado()

                        if z3 == True:
                            objpontoqua = Ponto(x_qua, y_qua)
                            centroqua = objpontoqua.centro()
                            objquadrado = Quadrado(lado1_qua, lado2_qua, lado3_qua, lado4_qua, centroqua)
                            self.dashboard.inserirForma(objquadrado)
                            break
                        else: 
                            print('Os valores de lado escolhidos não correspondem a um quadrado, por favor, informe outros valores')
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')


                print('Escolha o que deseja fazer com o quadrado criado: ')
                print('1. Printar informações do quadrado')
                print('2. Calcular o perímetro do quadrado')
                print('3. Calcular a área do quadrado')
                print('4. Calcular a diagonal do quadrado')

                escolha8 = input('Digite a opção escolhida: ')

                if escolha8.isdigit():
                    
                    escolha8 = int(escolha8)
                    if escolha8 == 1:
                        objquadrado.printarInit()
                    elif escolha8 == 2:
                        objquadrado.printaPerimentro()
                    elif escolha8 == 3:
                        objquadrado.printaArea()
                    elif escolha8 == 4:
                        objquadrado.printaDiagonal()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 8:
                while True:
                    try:
                        ladopen = int(input('Informe um lado do seu pentágono regular: '))
                        x_pen = int(input('Escolha a coordenada x do centro do pentágono: '))
                        y_pen = int(input('Escolha a coordenada y do centro do pentágono: '))
                        break
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                objpontopen = Ponto(x_pen, y_pen)
                centropen = objpontopen.centro()
                objpentagono = Pentagono(ladopen, centropen)
                self.dashboard.inserirForma(objpentagono)

                print('Escolha o que deseja fazer com o pentágono criado: ')
                print('1. Printar informações do pentágono')
                print('2. Calcular o perímetro do pentágono')
                print('3. Calcular a área do pentágono')

                escolha9 = input('Digite a opção escolhida: ')

                if escolha9.isdigit():
                    
                    escolha9 = int(escolha9)
                    if escolha9 == 1:
                        objpentagono.printarInit()
                    elif escolha9 == 2:
                        objpentagono.printaPerimetro()
                    elif escolha9 == 3:
                        objpentagono.printaArea()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 9:
                while True:
                    try:
                        ladohex = int(input('Informe um lado do seu hexágono regular: '))
                        x_hex = int(input('Escolha a coordenada x do centro do hexágono: '))
                        y_hex = int(input('Escolha a coordenada y do centro do hexágono: '))
                        break
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')
                
                objpontohex = Ponto(x_hex, y_hex)
                centrohex = objpontohex.centro()
                objhexagono = Hexagono(ladohex, centrohex)
                self.dashboard.inserirForma(objhexagono)


                print('Escolha o que deseja fazer com o hexágono criado: ')
                print('1. Printar informações do hexágono')
                print('2. Calcular o perímetro do hexágono')
                print('3. Calcular a área do hexágono')

                escolha10 = input('Digite a opção escolhida: ')

                if escolha10.isdigit():

                    escolha10 = int(escolha10)
                    if escolha10 == 1:
                        objhexagono.printarInit()
                    elif escolha10 == 2:
                        objhexagono.printaPerimetro()
                    elif escolha10 == 3:
                        objhexagono.printaArea()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 10:
                while True:
                    try:
                        ladohep = int(input('Informe um lado do seu heptágono regular: '))
                        x_hep = int(input('Escolha a coordenada x do centro do heptágono: '))
                        y_hep = int(input('Escolha a coordenada y do centro do heptágono: '))
                        break
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                objpontohep = Ponto(x_hep, y_hep)
                centrohep = objpontohep.centro()
                objheptagono = Heptagono(ladohep, centrohep)
                self.dashboard.inserirForma(objheptagono)

                print('Escolha o que deseja fazer com o heptágono criado: ')
                print('1. Printar informações do heptágono')
                print('2. Calcular o perímetro do heptágono')
                print('3. Calcular a área do heptágono')

                escolha11 = input('Digite a opção escolhida: ')

                if escolha11.isdigit():

                    escolha11 = int(escolha11)
                    if escolha11 == 1:
                        objheptagono.printarInit()
                    elif escolha11 == 2:
                        objheptagono.printaPerimetro()
                    elif escolha11 == 3:
                        objheptagono.printaArea()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 11:
                while True:
                    try:
                        ladooct = int(input('Informe um lado do seu octógono regular: '))
                        x_oct = int(input('Escolha a coordenada x do centro do octógono: '))
                        y_oct = int(input('Escolha a coordenada y do centro do octógono: '))
                        break
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                objpontooct = Ponto(x_oct, y_oct)
                centrooct = objpontooct.centro()
                objoctogono = Octogono(ladooct, centrooct)
                self.dashboard.inserirForma(objoctogono)

                print('Escolha o que deseja fazer com o octógono criado: ')
                print('1. Printar informações do octógono')
                print('2. Calcular o perímetro do octógono')
                print('3. Calcular a área do octógono')

                escolha12 = input('Digite a opção escolhida: ')

                if escolha12.isdigit():
                    
                    escolha12 = int(escolha12)
                    if escolha12 == 1:
                        objoctogono.printarInit()
                    elif escolha12 == 2:
                        objoctogono.printaPerimetro()
                    elif escolha12 == 3:
                        objoctogono.printaArea()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

            elif escolha == 12:
                while True:
                    try:
                        lado1_ret = int(input('Informe um lado do seu retângulo: '))
                        lado2_ret = int(input('Informe o outro lado do seu retângulo: '))
                        x_ret = int(input('Escolha a coordenada x do centro do retângulo: '))
                        y_ret = int(input('Escolha a coordenada y do centro do retângulo: '))
                        break
                    except ValueError:
                        print('O valor inserido não é válido. Insira um número')

                objpontoret = Ponto(x_ret, y_ret)
                centroret = objpontoret.centro()
                objretangulo = Retangulo(lado1_ret, lado2_ret, centroret)
                self.dashboard.inserirForma(objretangulo)

                print('Escolha o que deseja fazer com o retângulo criado: ')
                print('1. Printar informações do retângulo')
                print('2. Calcular o perímetro do retângulo')
                print('3. Calcular a área do retângulo')
                print('4. Calcular a diagonal do retângulo')

                escolha13 = input('Digite a opção escolhida: ')

                if escolha13.isdigit():

                    escolha13 = int(escolha13)
                    if escolha13 == 1:
                        objretangulo.printarInit()
                    elif escolha13 == 2:
                        objretangulo.printaPerimentro()
                    elif escolha13 == 3:
                        objretangulo.printaArea()
                    elif escolha13 == 4:
                        objretangulo.printaDiagonal()
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')     

            else:
                print('O número escolhido não é uma opção, por favor, escolha um número válido.')

        else:
            print('\nO valor inserido não corresponde a um número, por favor, escolha uma opção válida.\n')


    def crash(self):

        if not self.dashboard.formas: 

            print('\nNão há formas geométricas criadas, por favor, crie uma forma geométrica.\n')

        else:

            self.dashboard.listarFormas()

            while True:
                print('\nEscolha uma opção para consulta:')
                print('1. Verificar interferências')
                print('2. Sair')

                escolha_ = input('\nDigite a opção escolhida: ')

                if escolha_.isdigit():
                    escolha_ = int(escolha_)
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')

                if type(escolha_) == int:

                    if escolha_ == 1:
                        while True:
                            try:
                                print('Digite as coordenadas do novo ponto que deseja verificar a interferência: ')
                                x_p = int(input('Coordenada x: '))
                                y_p = int(input('Coordenada y: '))
                                break
                            except ValueError:
                                print('O valor inserido não é válido. Insira um número')

                        while True:
                            try:
                                formag = input('\nEscolha a forma geométrica que deseja verificar interferência: ').strip()
                                formag_escolhida = self.dashboard.retornarFormas(formag)
                                formag_escolhida.verificaInterferencias(x_p, y_p)
                                break
                            except KeyError:
                                print('Digite corretamente o nome da forma geométrica que deseja verificar interferências.')

                    elif escolha_ == 2:
                        break
                        
                    else:
                        print('O número escolhido não é uma opção, por favor, escolha um número válido.')
                else:
                    print('O valor inserido não corresponde a um número, por favor, escolha uma opção válida.')


    def listar(self):

        if not self.dashboard.formas: 

            print('\nNão há formas geométricas criadas, por favor, crie uma forma geométrica.\n')

        else:

            self.dashboard.listarFormas()

    def contar(self):

        self.dashboard.printaContagem()

    def run(self):
        
        while True:
            print('Escolha uma opção:')
            print('1. Criar uma forma geométrica')
            print('2. Verificar interferências entre formas geométricas')
            print('3. Listar formas criadas')
            print('4. Contagem de formas geométricas criadas')
            print('5. Sair')
            escolha = input('Digite o número da opção escolhida: ')

            if escolha.isdigit():
                escolha = int(escolha)
                if escolha in range(1,6):
                    selecao = list(self.acoes.keys())[int(escolha)-1]
                    self.acoes[selecao]()
                else:
                    print('O número informado não correspode a uma opção válida, por favor, insira outro número')
            else:
                print('O valor inserido não corresponde a um número, por favor, insira um número')