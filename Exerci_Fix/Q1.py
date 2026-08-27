class Carro():
    marca = 'Toyota'
    modelo = 'Corolla'
    ano = 2020
    motor = '1.8L'

    def andar(self):
        print(f'O carro {self.marca} {self.modelo} está andando.')

    def parar(self):
        print(f'O carro {self.marca} {self.modelo} parou.')

    def buzinar(self):
        print(f'O carro {self.marca} {self.modelo} está buzinando.')


carro1 = Carro()
carro1.andar()
carro1.buzinar()
carro1.parar()
