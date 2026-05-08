qtd_blusas = int(input("Digite A Quantidade De Blusas Necessárias: "))

metro_totais = qtd_blusas * 120
novelos = metro_totais // 125  # Divisão inteira

if metro_totais % 125 > 0:
    novelos += 1

print(f"Total De Novelos Necessários: {novelos}")