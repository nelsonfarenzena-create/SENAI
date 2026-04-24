dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

anos = dias_trabalhados // 365
resto = dias_trabalhados % 365

meses = resto // 30
dias = resto % 30

print(f"{dias_trabalhados} dias equivalem a {anos} anos, {meses} meses e {dias} dias.")