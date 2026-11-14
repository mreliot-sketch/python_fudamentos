# carregado os logs sistema
log_sistema = "ERRO: Falha de comunicação no sensor 04"

#Verificar se a palavra "ERRO" está presente no log

tem_erro = "ERRO" in log_sistema
print(f"Falha detectada no log? {tem_erro}")

sem_critico = "CRITICO" not in log_sistema
print(f"sem nivel critico?: {sem_critico}")


