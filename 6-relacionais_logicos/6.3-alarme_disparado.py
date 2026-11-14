#Definindo os valores das variaveis
temperatura_critica = True
processao_critica = False


# Realização a checagem  dos sensores 
alarme_disparado = temperatura_critica or pressao_critica
#Apresentando disparo do alarme
print(f"Alarme Atividade: {alarme_disparado}")
