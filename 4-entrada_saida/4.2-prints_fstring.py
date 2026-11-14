nome = "mariana"
curso = "fundamentos de python"
preco = 69.9
codigo_peca = 999999999999

print("Aluno: ", nome," | curso: ", curso.title())
print(f"Aluno: {nome} | curso: {curso.title()}")


print(f"Valor original (ponto): R$ {preco:.2f}".replace(".",","))


print(f"codigo da peça: #{codigo_peca:05d}")


