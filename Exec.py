# Considere o problema de ordenar um conjunto V de n números inteiros todos com exatamente d dígitos.


# Considere um algoritmo de ordenação que se baseia em ordenar os valores com relação aos seus dígitos, ou seja, dígito a dígito partindo do dígito menos significativo até o mais significativo. Sabemos que um dígito específico pode assumir 10 possíveis valores (0,1,2,3,4,5,6,7,8,9). Sendo assim, para cada dígito deve-se separar os elementos em 10 caixas numeradas de 0 a 9. A ordem dos elementos  em cada caixa (de mesmo dígito) deve preservar a ordem parcial entre os elementos. Com relação a um dígito específico, uma vez que todos os elementos foram adicionas nas suas respectivas caixas, uma nova disposição dos elementos deve ser apresentada extraindo sucessivamente os elementos de cada caixa (respeitando a ordem interna), partindo da caixa 0 até a caixa 9. O algoritmo termina, quando o passo a passo anterior é efetuado para o dígito mais significativo. A disposição final será ordenada de forma crescente.


# 1) Descreva as estruturas de dados necessárias para o desenvolvimento desse algoritmo.


# 2) Qual é a estrutura de dados vista em aula adequada para implementar as caixas? Justifique sua resposta.


# 3) Esboce tal algoritmo utilizando inserções e remoções na estrutura escolhida para modelar as caixas como sub-rotinas predefinas.


# Exemplo de execução do algoritmo:  


# V = [ 19, 13, 05, 27, 01, 26, 31, 16, 02, 09, 11, 21, 60, 07]


# considerando d como o dígito menos significativo:


# caixa 0 = 60 
# caixa 1 = 01, 31, 11, 21
# caixa 2 = 02
# caixa 3 = 13
# caixa 4 = 
# caixa 5 = 05
# caixa 6 = 26, 16
# caixa 7 = 27, 07
# caixa 8 = 
# caixa 9 =  19, 09


# Disposição com relação ao dígito menos significativo: 


# 60, 01, 31, 11, 21, 02, 13, 05, 26, 16, 07, 27, 19, 09


# Considerando d como o próximo dígito:


# caixa 0 = 01, 02, 05, 07, 09 
# caixa 1 = 11, 13, 16, 19
# caixa 2 = 21, 26, 27
# caixa 3 = 31
# caixa 4 = 
# caixa 5 = 
# caixa 6 = 60
# caixa 7 = 
# caixa 8 = 
# caixa 9 =  


# disposição final:


# 01, 02, 05, 07, 09, 11, 13, 16, 19, 21, 26, 27, 31, 60


vetorOriginal = [ 19, 13, 5, 27, 1, 26, 31, 16, 2, 9, 11, 21, 60, 7]

vetorNovo = []



tamVetorOriginal =  len(vetorOriginal)

for pos in range(tamVetorOriginal):
    if vetorOriginal[pos] < 10:
        vetorNovo.append('0' + str(vetorOriginal[pos]))
    else:
        vetorNovo.append(str(vetorOriginal[pos]))


# print(vetorNovo)




numAlgarismos = 2


caixas = [
    [], #0
    [], #1
    [], #2
    [], #3
    [], #4
    [], #5
    [], #6
    [], #7
    [], #8
    [], #9
]




tamVetorNovo = len(vetorNovo)

for pos in range(tamVetorNovo):
    numCaixa = int(vetorNovo[pos][1])
    valor = vetorNovo[pos]

    caixas[numCaixa].append(valor)
    


print(caixas)






