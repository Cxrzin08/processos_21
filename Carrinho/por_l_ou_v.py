class PorLitroOuValor:
    def __init__(self, valor) -> None:
        self.valor = valor

    def por_litro(self):
        try:
            por_litro = float(input("Digite a quantia de litros: "))
            resultado = por_litro * self.valor
            print(f"O valor em reais foi de {resultado:.2f} reais")
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")

    def por_valor(self):
        try:
            por_valor = float(input("Digite a quantia em litros que deseja abastecer: "))
            resultado = por_valor / self.valor
            print(f"O valor em reais abastecido foi de {resultado:.2f} litros")
        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico.")

