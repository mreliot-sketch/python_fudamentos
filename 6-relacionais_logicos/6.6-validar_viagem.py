#Solicitando dados do veículo

combustivel = float(input("Quantidade de combustivel: "))
pneus_ok = input("os pneus estão kalibrados? sim/não: ").lower().strip()
documento_ok = input("A documentação está em dia? (sim/não):  ").lower().strip()

# Checagem individual (Retorna True ou False)
combustivel_suficiente = combustivel >= 10.0
pneus_kalibrados = pneus_ok == "sim"
documento_regular = documento_ok == "sim"

#comnbinação logica para a liberação da viagem

viagem_liberada = combustivel_suficiente and pneus_ok and documento_ok 

#apresentando o status e liberação da viagem

print("\n------PROCEDIMENTOS DE SEGURANÇA PARA A VIAGEM------")
print(f"1. Combustivel Suficiente (>=10L): {combustivel_suficiente}\n 2.Pneus Kalibrados: {pneus_ok}\n 3. Documentação Regular?: {documento_ok}\n VIAGEM LIBERADA: {viagem_liberada}")




