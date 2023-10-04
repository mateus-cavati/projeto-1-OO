class Circulo():
    def __init__(self, raio):
        self.raio = raio
    
    def Area(self):
        Area = (self.raio**2)*3.14
        print(Area)
    
    def Circunferencia(self):
        circunferencia = 2*3.14*self.raio
        print(circunferencia)

class Ponto():
    def __init__(self, x, y):
        self.coordenadax = x
        self.coordenaday = y

    def Coordenada(self):
        print('(',self.coordenadax,',',self.coordenaday,')')

class Reta():
    def __init__(self, x1, y1, x2, y2):
        self.coordenadax1 = x1
        self.coordenaday1 = y1
        self.coordenadax2 = x2
        self.coordenaday2 = y2

    def Tamanho(self):
        diferenca_x = self.coordenadax2 - self.coordenadax1
        diferenca_y = self.coordenaday2 - self.coordenaday1
        tamanho = (diferenca_x ** 2 + diferenca_y ** 2)**(1/2)
        tamanho = float(tamanho)
        print(tamanho)

if __name__ == "__main__":
    a = input('escolha uma forma(ponto, circulo ou reta): ')
    if a == 'circulo':
        R1 = float(input('informe o Raio do circulo: '))
        circulo1 = Circulo(R1)
        Op1 = input('escolha uma das opções:(area do circulo ou circunferencia do circulo) ')
        if Op1 == 'area do circulo':
            circulo1.Area()
        elif Op1 == 'circunferencia do circulo':
            circulo1.Circunferencia()
        else:
            print('não há essa opção')
    
    elif a == 'ponto':
        x = float(input('informe a coordenada x do ponto: '))
        y = float(input('informe a coordenada y do ponto: '))
        ponto1 = Ponto(x, y)
        Op2 = input('você gostaria de saber a coordenada do seu ponto?(s/n) ')
        if Op2 == 's':
            ponto1.Coordenada()
        elif Op2 == 'n':
            StopIteration
        else:
            print('não há essa opção')
    
    elif a == 'reta':
        w = float(input('informe a coordenada x1 da reta: '))
        x = float(input('informe a coordenada y1 da reta: '))
        y = float(input('informe a coordenada x2 da reta: '))
        z = float(input('informe a coordenada y2 da reta: '))
        reta1 = Reta(w, x, y, z)
        Op3 = input('você gostaria de saber o tamanho da reta?(s/n) ')
        if Op3 == 's':
            reta1.Tamanho()
        elif Op3 == 'n':
            StopIteration
        else:
            print('não há essa opção')
    
    else:
        print('não há essa opção')