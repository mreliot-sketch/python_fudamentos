# Criando o status dos sensores

grade_fechada = True
emergencia_desativada = True 

#Amabas precisam ser True para liberar o sistema
sistema_pronto = grade_fechada and emergencia_desativada
print(f"Sistema liberado: {sistema_pronto}")