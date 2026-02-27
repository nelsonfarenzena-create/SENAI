nome = input("insira seu nome: ")
nota1 = float(input("Insira A Primeira Nota: "))
nota2 = float(input("Insira A Segunda Nota: "))
media = (nota1 + nota2) /2
print ("O Usuário" ,nome," Obteve a Média das Notas de :",media)
if media >= 7:
    print("O Aluno Está Aprovado")
else:
    print("O Aluno Está Reprovado")