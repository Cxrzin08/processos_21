from subpastasbombas.BombaEtanol import Etanol
from subpastasbombas.BombaGasolina import Gasolina
from Carrinho.por_l_ou_v import PorLitroOuValor

while True:
    print("Olá, somos o Samunipe")

    valor = input('''O que você deseja?
[1]. Abastecer Etanol - 3 R$
[2]. Abastecer Gasolina - 5 R$
[3]. Abastecer Gasolina com Aditivo
Digite sua resposta: ''')

    metodo_abastecimento = input('''Você deseja abastecer por?
[1]. Litro
[2]. Valor
Digite sua resposta: ''')

    if valor == '1':
        abastecimento_combustivel = Etanol()
    elif valor == '2':
        abastecimento_combustivel = Gasolina(tipo='comum')
    elif valor == '3':
        abastecimento_combustivel = Gasolina(tipo='aditivo')
    else:
        print("Opção inválida. Tente novamente.")
        continue

    abastecimento = PorLitroOuValor(abastecimento_combustivel.preco)

    if metodo_abastecimento == "1":
        abastecimento.por_litro()
    elif metodo_abastecimento == "2":
        abastecimento.por_valor()
    else:
        print("Opção inválida. Tente novamente.")
        continue
