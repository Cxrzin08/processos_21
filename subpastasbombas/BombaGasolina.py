class Gasolina:
    def __init__(self, tipo) -> None:
        self.tipo = tipo
        self.preco = self.definir_preco()

    def definir_preco(self):
        if self.tipo == 'comum':
            return 5
        elif self.tipo == 'aditivo':
            return 5 
        else:
            raise ValueError("Tipo de gasolina inválido")

    def gasolina_comum(self):
        print(f"Abastecendo com gasolina comum a R${self.preco:.2f} por litro.")

    def gasolina_com_aditivo(self):
        print(f"Abastecendo com gasolina aditivada a R${self.preco:.2f} por litro.")
