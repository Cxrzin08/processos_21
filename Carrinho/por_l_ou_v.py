class PorLitroOuValor:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.litros = 0
        self.capacidade_maxima = 100 

    def por_litro(self):
        try:
            por_litro = float(input("Digite a quantidade de litros que deseja abastecer: "))
            
            if por_litro + self.litros > self.capacidade_maxima:
                print(f"Não é possível abastecer {por_litro} litros. Seu tanque só pode comportar {self.capacidade_maxima - self.litros:.2f} litros.")
                return
            
            resultado = por_litro * self.valor
            self.litros += por_litro 
            quantidade_disponivel = f"A capacidade do seu tanque é de 100 litros no total. Quantia atual do seu tanque: {self.litros:.2f} litros"
            print(quantidade_disponivel)
            print(f"O valor total é de R${resultado:.2f}")
            
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")

    def por_valor(self):
        try:
            por_valor = float(input("Digite o valor em reais que deseja abastecer: "))
            resultado = por_valor / self.valor
            if resultado + self.litros > self.capacidade_maxima:
                print(f"Não é possível abastecer R${por_valor} de combustível. Seu tanque só pode comportar {self.capacidade_maxima - self.litros:.2f} litros.")
                return
            self.litros += resultado 
            quantidade_disponivel = f"A capacidade do seu tanque é de 100 litros no total. Quantia atual do seu tanque: {self.litros:.2f} litros"
            print(quantidade_disponivel)
            print(f"A quantidade de combustível abastecida foi de {resultado:.2f} litros")
            
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")
