import time

contador = 10

while contador >= 0:
    print(f"Tempo restante: {contador} segundos")
    time.sleep(1)  # pausa de 1 segundo
    contador -= 1

print("Resfriamento concluído. Pode abrir a prensa!")-