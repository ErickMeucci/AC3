def desenhar_triangulo_alfabetico(N):
    for linha in range(1, N + 1):
        # Calcula o caractere inicial para cada linha
        caractere_inicial = chr(ord('A') + linha - 1)

        # Cria a linha atual
        linha_atual = ""
        for i in range(linha):
            linha_atual += caractere_inicial
            caractere_inicial = chr(ord(caractere_inicial))

        # Imprime a linha atual
        print(linha_atual)

# Solicita ao usuário o valor de N
N = int(input())
desenhar_triangulo_alfabetico(N)
