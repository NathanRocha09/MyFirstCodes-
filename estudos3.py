def cria_matriz(num_linhas, num_colunas):
        matriz = []
        for i range (num_linhas):
                linha = []
                for j range (num_colunas):
                        valor = int(input("digite o elemento [" + str(i) + "][" + str(j) + "]"))
                        linha.append(valor)
                        matriz.append(linha)

return matriz
        
    

                
def l_matriz():
    linha = int(input("defina a linha dessa matriz: "))
    coluna = int(input("defina a coluna dessa matriz: "))
    cria_matriz(linha,coluna)
    