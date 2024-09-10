from subpastasbombas.BombaEtanol import Etanol
from subpastasbombas.BombaGasolina import Gasolina
from Carrinho.por_l_ou_v import PorLitroOuValor

print("Olá, somos o Samunipe")

valor = input('''O que você deseja?
[1]. Abastecer Etanol - 3 R$
[2]. Abastecer Gasolina - 5 R$
[3]. Abastecer Gasolina com Aditivo
Digite sua resposta: ''')

test = input('''Você deseja abastecer por?
[1]. Litro
[2]. Valor
Digite sua resposta: ''')

if test == '1':
    valor_combustivel = 3
elif test == '2':
    valor_combustivel = 5
elif test == '3':
    valor_combustivel = 5 
else:
    print("Opção inválida")



if valor == '1':
    Etanol.bomba_etanol()
elif valor == '2':
    Gasolina.gasolina_comum()
elif valor == '3':
    Gasolina.gasolina_com_aditivo()

abastecimento = PorLitroOuValor(valor_combustivel)

if test == "1":
    abastecimento.por_litro()
elif test == "2":
    abastecimento.por_valor()
else:
    print("Opção inválida")
    exit()


