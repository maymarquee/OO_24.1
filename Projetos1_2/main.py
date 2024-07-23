from package.maths.menu import Menu

def workspace():
     
    programa = Menu()
    programa.run()


if __name__ == "__main__":
    workspace()
else: 
    print('O arquivo foi envocado como módulo, por favor, envoque-o como programa')