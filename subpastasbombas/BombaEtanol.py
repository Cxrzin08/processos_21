class Etanol:
    def __init__(self) -> None:
        self.preco = 3 

    def bomba_etanol(self):
        print(f"Abastecendo com etanol a R${self.preco:.2f} por litro.")
