# Situação do botão não pressionado
emergencia_pressionada = False


#Liberação do funcionamento da máquina
maquina_liberada = not emergencia_pressionada
print(f"Emergencia pressionada?: {emergencia_pressionada}")
print(f"a máquina pode rodar?: {maquina_liberada}")