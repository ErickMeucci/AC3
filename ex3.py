# Inicializa as variáveis para armazenar o total de doações em VC$ e em R$
total_vc = 0.0
total_reais = 0.0

# Loop para receber as doações em VC$
while True:
    valor_vc = float(input())
    
    if valor_vc == -1.0:
        break
    
    total_vc += valor_vc

# Calcula o total em reais
total_reais = total_vc * 2.5

# Exibe o total de doações em VC$ e em reais com duas casas decimais
print(f"VC$ {total_vc:.2f}")
print(f"R$ {total_reais:.2f}")
