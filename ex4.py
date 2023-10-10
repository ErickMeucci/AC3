# Função para verificar se um ano é bissexto
def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Entrada dos anos INÍCIO e FIM
ano_inicio = int(input())
ano_fim = int(input())

# Loop para encontrar e exibir os anos bissextos no intervalo
contador_bissextos = 0
for ano in range(ano_inicio, ano_fim + 1):
    if eh_bissexto(ano):
        print(ano)
        contador_bissextos += 1

# Exibição da quantidade de anos bissextos no intervalo
print(f"bissexto: {contador_bissextos}")
