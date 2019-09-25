import random
import math
import copy

# Na vizinhança não se deve permitir que um caminho ja tomado seja "desfeito" 
# ou refeito
# A vizinhança deve executar apenas um movimento por vizinhança (para VND)

# Recebe a lista de rotas  e então verifica se é possível encontrar uma rota 
# melhor dentro da lista.
# Nesta vizinhança são executadas trocas entre duas posições em uma mesma rota
# qualquer
# Ex:
#    [ 1, 2, 3, 4] --> [1,2,4,3]
# Parametros:
# lista_de_rotas - Lista com as rotas definidas com a heuristica inicial
# lista_de_demandas - Lista com as demandas de cada cliente
# capacidade - A capacidade máxima que o sistema demanda
def vizinhanca_1(lista_de_rotas):
    # a nova rota gerada será armazenada aqui
    # Uma copia é criada para evitar alterar a rota original
    # Para caso nenhuma solução melhor ser encontrada
    rotas_melhoradas = copy.deepcopy(lista_de_rotas) 
    
    # Seleciona a rota que será alterada
    indice_rota = random.randrange(0,len(rotas_melhoradas))

    # Pega o tamanho da rota
    tam_rota = len(rotas_melhoradas[indice_rota])

    # Seleciona os indices que serão alterados
    indice_selecionado_1 = random.randrange(1,tam_rota-1)
    indice_selecionado_2 = random.randrange(1,tam_rota-1)
    # Seleciona randomicamente um indice a ser trocado
    while(indice_selecionado_1 == indice_selecionado_2 and tam_rota != 3):
        indice_selecionado_1 = random.randrange(1,tam_rota-1)
        indice_selecionado_2 = random.randrange(1,tam_rota-1)
    
    # realiza a troca
    # salva o local que será tirado da rota 1
    temp = rotas_melhoradas[indice_rota][indice_selecionado_1]
    
    # Substitui esse valor por seu correspondente na rota 2
    rotas_melhoradas[indice_rota][indice_selecionado_1] = \
                            rotas_melhoradas[indice_rota][indice_selecionado_2]

    # Substitui o da rota 2 pelo retirado da rota 1
    rotas_melhoradas[indice_rota][indice_selecionado_2] = temp

    # Retorna a nova rota
    return rotas_melhoradas
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Recebe a lista de rotas  e então verifica se é possível encontrar uma rota 
# melhor dentro da lista.
# Nesta vizinhança são executadas trocas entre duas rotas quaisquer e entre
#  dois locais de posições identicas
# Ex:
#    [ 1, 2, 3, 4] e [5,6,7,8,9,19] --> [1,2,4,8] e [5,6,7,4,9,19]
# Parametros:
# lista_de_rotas - Lista com as rotas definidas com a heuristica inicial
# lista_de_demandas - Lista com as demandas de cada cliente
# capacidade - A capacidade máxima que o sistema demanda
def vizinhanca_2(lista_de_rotas,lista_de_demandas, capacidade):
    # a nova rota gerada será armazenada aqui
    # Uma copia é criada para evitar alterar a rota original
    # Para caso nenhuma solução melhor ser encontrada
    rotas_melhoradas = copy.deepcopy(lista_de_rotas) 
    
    # Variáveis que armazenarão as rotas
    indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
    indice_rota_2 = random.randrange(0,len(rotas_melhoradas))
    # Impede que selecionem a mesma rota para ambas as variáveis
    while(indice_rota_1 == indice_rota_2 and len(rotas_melhoradas) > 1):
        indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
        indice_rota_2 = random.randrange(0,len(rotas_melhoradas))

    # Descobre qual o valor da menor rota para evitar indices fora das
    #  rotas selecionadas
    tam_menor_rota = len(rotas_melhoradas[indice_rota_1]) \
                        if (len(rotas_melhoradas[indice_rota_1]) \
                                < len(rotas_melhoradas[indice_rota_2])) \
                        else len(rotas_melhoradas[indice_rota_2])
    repetir = 1
    # sem sucesso seleciona uma outra rota
    contador_de_tentativas = 0 
                            
    while(repetir):
        repetir = 0
        # Seleciona randomicamente um indice a ser trocado
        indice_selecionado = random.randrange(1,tam_menor_rota-1)
        
        # realiza a troca
        # salva o local que será tirado da rota 1
        temp = rotas_melhoradas[indice_rota_1][indice_selecionado]
        
        # Substitui esse valor por seu correspondente na rota 2
        rotas_melhoradas[indice_rota_1][indice_selecionado] = \
                            rotas_melhoradas[indice_rota_2][indice_selecionado]

        # Substitui o da rota 2 pelo retirado da rota 1
        rotas_melhoradas[indice_rota_2][indice_selecionado] = temp

        #Verifica se a nova rota se encontra dentro da capacidade máxima
        temp = 0 # reaproveitando temp
        
        for rota in [rotas_melhoradas[indice_rota_1],\
                        rotas_melhoradas[indice_rota_2]]:
            for cliente in rota:
                temp = temp + lista_de_demandas[cliente]
            if(temp > capacidade):
                repetir = 1
                break
            temp = 0
        contador_de_tentativas = contador_de_tentativas +1
        if(contador_de_tentativas > 100):
            contador_de_tentativas = 0
            # Variáveis que armazenarão as rotas
            indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
            indice_rota_2 = random.randrange(0,len(rotas_melhoradas))
            # Impede que selecionem a mesma rota para ambas as variáveis
            while(indice_rota_1 == indice_rota_2 and len(rotas_melhoradas) > 1):
                indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
                indice_rota_2 = random.randrange(0,len(rotas_melhoradas))
            tam_menor_rota = len(rotas_melhoradas[indice_rota_1]) \
                        if (len(rotas_melhoradas[indice_rota_1]) \
                                < len(rotas_melhoradas[indice_rota_2])) \
                        else len(rotas_melhoradas[indice_rota_2])
    # Retorna a nova rota
    return rotas_melhoradas
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Esta vizinhança é semelhante a vizinhança 2 porém a troca feita é entre 2
# locais selecionados aleatoriamente
def vizinhanca_3(lista_de_rotas,lista_de_demandas, matriz_de_distancias, \
                                                                    capacidade):
    # a nova rota gerada será armazenada aqui
    # Uma copia é criada para evitar alterar a rota original
    # Para caso nenhuma solução melhor ser encontrada
    rotas_melhoradas = copy.deepcopy(lista_de_rotas) 
    
    # Variáveis que armazenarão as rotas
    indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
    indice_rota_2 = random.randrange(0,len(rotas_melhoradas))
    # Impede que selecionem a mesma rota para ambas as variáveis
    while(indice_rota_1 == indice_rota_2 and len(rotas_melhoradas)):
        indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
        indice_rota_2 = random.randrange(0,len(rotas_melhoradas))

    # Descobre qual o valor da menor rota para evitar indices fora das
    #  rotas selecionadas
    tam_rota_1 = len(rotas_melhoradas[indice_rota_1])
    tam_rota_2 = len(rotas_melhoradas[indice_rota_2])
    repetir = 1

    contador_de_tentativas = 0
    while(repetir):
        repetir = 0
        # Seleciona randomicamente um indice a ser trocado
        indice_selecionado_1 = random.randrange(1,tam_rota_1-1)
        indice_selecionado_2 = random.randrange(1,tam_rota_2-1)
        
        # realiza a troca
        # salva o local que será tirado da rota 1
        temp = rotas_melhoradas[indice_rota_1][indice_selecionado_1]
        
        # Substitui esse valor por seu correspondente na rota 2
        rotas_melhoradas[indice_rota_1][indice_selecionado_1] = \
                        rotas_melhoradas[indice_rota_2][indice_selecionado_2]

        # Substitui o da rota 2 pelo retirado da rota 1
        rotas_melhoradas[indice_rota_2][indice_selecionado_2] = temp

        #Verifica se a nova rota se encontra dentro da capacidade máxima
        temp = 0 # reaproveitando temp

        for rota in [rotas_melhoradas[indice_rota_1],\
                        rotas_melhoradas[indice_rota_2]]:
            for cliente in rota:
                temp = temp + lista_de_demandas[cliente]
            if(temp > capacidade):
                repetir = 1
                break
            temp = 0
        contador_de_tentativas = contador_de_tentativas +1
        if(contador_de_tentativas > 100):
            contador_de_tentativas = 0
            # Variáveis que armazenarão as rotas
            indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
            indice_rota_2 = random.randrange(0,len(rotas_melhoradas))
            # Impede que selecionem a mesma rota para ambas as variáveis
            while(indice_rota_1 == indice_rota_2 and len(rotas_melhoradas) > 1):
                indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
                indice_rota_2 = random.randrange(0,len(rotas_melhoradas))
            tam_rota_1 = len(rotas_melhoradas[indice_rota_1])
            tam_rota_2 = len(rotas_melhoradas[indice_rota_2])

    # Retorna a nova rota
    return rotas_melhoradas
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Recebe a lista de rotas  e então verifica se é possível encontrar uma rota 
# melhor dentro da lista.
# Nesta vizinhança são executadas trocas entre duas posições consecutivas de uma mesma rota
# qualquer
# Ex:
#    [ 1, 2, 3, 4] --> [1,2,4,3]
# Parametros:
# lista_de_rotas - Lista com as rotas definidas com a heuristica inicial

def vizinhanca_4(lista_de_rotas):

    # a nova rota gerada será armazenada aqui
    # Uma copia é criada para evitar alterar a rota original
    # Para caso nenhuma solução melhor ser encontrada
    rotas_melhoradas = copy.deepcopy(lista_de_rotas) 
    
    # Seleciona a rota que será alterada
    indice_rota = random.randrange(0,len(rotas_melhoradas))
    
    while(len(rotas_melhoradas[indice_rota]) <= 3):
        indice_rota = random.randrange(0,len(rotas_melhoradas))

    # Pega o tamanho da rota
    tam_rota = len(rotas_melhoradas[indice_rota])
    #print("Tamanho: ", tam_rota)
    
    #Seleciona um indice
    indice_selecionado = random.randrange(1,tam_rota-2)
    
    # realiza a troca
    # salva o local que será tirado da rota 1
    temp = rotas_melhoradas[indice_rota][indice_selecionado]
    
    # Substitui esse valor por seu correspondente
    rotas_melhoradas[indice_rota][indice_selecionado] = rotas_melhoradas[indice_rota][indice_selecionado + 1]

    # Substitui o da rota 2 pelo retirado da rota 1
    rotas_melhoradas[indice_rota][indice_selecionado + 1] = temp

    # Retorna a nova rota
    return rotas_melhoradas
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""