nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))

if idade < 0:
    print("Não se pode inserir uma idade menor que 0.")
elif idade > 120:
    print("Não se pode inserir uma idade maior que 120.")
else:
    dias_de_vida = idade * 365
    print("Você já viveu:", dias_de_vida, "dias de sua vida")