# Função para verificar se um ano é bissexto
def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Entrada dos anos INÍCIO e FIM
ano_inicio = int(input())
ano_fim = int(input())

# Inicializa o ano atual com o ano de início
ano_atual = ano_inicio

# Inicializa o contador de anos bissextos
contador_bissextos = 0

# Loop while para encontrar e exibir os anos bissextos no intervalo
while ano_atual <= ano_fim:
    if eh_bissexto(ano_atual):
        print(ano_atual)
        contador_bissextos += 1
    ano_atual += 1

# Exibição da quantidade de anos bissextos no intervalo
print(f"bissextos: {contador_bissextos}")
