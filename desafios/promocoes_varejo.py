
valor = int(input())


if valor < 50:
    print("Obrigado por comprar conosco!")
elif valor >= 50 and valor < 100:
    print("Parabens! Voce ganhou um brinde!")
elif valor >= 100 and valor < 200:
    print("Desconto de 10 reais aplicado!")
else:
    print("Desconto de 25 reais aplicado!")
