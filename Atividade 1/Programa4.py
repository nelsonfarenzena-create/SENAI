contador = 1
soma_notas = 0

while contador <= 4:
    nota= float(input(f"Digite A Nota Do { contador } bimestre: "))
    if nota < 0 or nota > 10: 
        print("nota inválida. A nota deve estar entre 0 e 10.")
        continue
    contador += 1
    soma_notas += nota

media= soma_notas / contador 
print ("a média de notas é: ", media)
if media >= 7:
    print ("Aluno Aprovado")
if media >= 5:
        print ("Aluno Reprovado")
else:
    print("o aluno está reprovado")