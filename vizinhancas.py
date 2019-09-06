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
    indice_selecionado_1 = random.randrange(1,tam_rota)
    indice_selecionado_2 = random.randrange(1,tam_rota)
    # Seleciona randomicamente um indice a ser trocado
    while(indice_selecionado_1 == indice_selecionado_2):
        indice_selecionado_1 = random.randrange(1,tam_rota)
        indice_selecionado_2 = random.randrange(1,tam_rota)
    
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
    indice_rota_1 = 0
    indice_rota_2 = 0
    # Impede que selecionem a mesma rota para ambas as variáveis
    while(indice_rota_1 == indice_rota_2):
        indice_rota_1 = random.randrange(0,len(rotas_melhoradas))
        indice_rota_2 = random.randrange(0,len(rotas_melhoradas))

    # Descobre qual o valor da menor rota para evitar indices fora das
    #  rotas selecionadas
    tam_menor_rota = len(rotas_melhoradas[indice_rota_1]) \
                        if (len(rotas_melhoradas[indice_rota_1]) \
                                < len(rotas_melhoradas[indice_rota_2])) \
                        else len(rotas_melhoradas[indice_rota_2])
    repetir = 1
    while(repetir):
        # Seleciona randomicamente um indice a ser trocado
        indice_selecionado = random.randrange(1,tam_menor_rota)
        
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

        for rota in rotas_melhoradas:
            for cliente in rota:
                temp = temp + lista_de_demandas[cliente]
            if(temp > capacidade):
                repetir = 0
                break
            temp = 0

    # Retorna a nova rota
    return rotas_melhoradas
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def vizinhanca_3(lista_de_rotas,lista_de_demandas, capacidade):
    return lista_de_rotas