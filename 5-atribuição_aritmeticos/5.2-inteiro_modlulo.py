#definindo o valor das variaveis

total_sensores = int(input("Quantidade total de sensores: "))

CAPACIDADE_CAIXA = 12

# Quantas Caixas completas podemos encher

caixas_fechadas = total_sensores // CAPACIDADE_CAIXA

#Quantos sensores vão sobrar na caixa

sobra_sensores = total_sensores % CAPACIDADE_CAIXA

#############################################

print(f"quantas caixas completas: {caixas_fechadas}, e as sobras dessas peças avulsas: {sobra_sensores}")