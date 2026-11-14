#primeiro lote tem 255 componentes
componente = 255
componente_sobra = 0
#Operadores se tornam uma constante

OPERADORES = 4

#divida com os operadores

divisao = componente // OPERADORES

#faça uma divisão com o oporador e o componente

componente_sobra = componente % OPERADORES

print(f"divisão com os operadores: {divisao}\n sobra dos componentes: {componente_sobra}")


