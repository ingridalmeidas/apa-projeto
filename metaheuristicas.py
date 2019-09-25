import vizinhancas
import funcoesGenericas
import copy
import math
import random
import pprint
import os

MAXIMO = 4 # Maximo de vizinhanças
TEMPERATURA_MAXIMA = 1e100

def vnd(lista_de_rotas,lista_de_demandas,matriz_de_distancias,capacidade):
	rota_melhorada = None # salgvará as novas rotas
	sucesso = False # Avisa se teve sucesso na melhora
	total_atual = funcoesGenericas.total_percorrido(lista_de_rotas,matriz_de_distancias)
	k = 1 #marca a vizinhança sendo visitada
	while(k <= MAXIMO):
    	#vizita vizinhança de acordo com o valor de k
		if(k == 1):
			# salva vizinhança
			rota_melhorada = vizinhancas.vizinhanca_1(lista_de_rotas)
			#print("1 - {0} {1}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias),rota_melhorada))
		elif(k == 2):
    			# salva vizinhança
			rota_melhorada = vizinhancas.vizinhanca_2(lista_de_rotas,\
											lista_de_demandas,capacidade)
			#print("2 - {0} {1}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias),rota_melhorada))
		elif(k == 3):
			# salva vizinhança
			rota_melhorada = vizinhancas.vizinhanca_3(lista_de_rotas,\
						lista_de_demandas,matriz_de_distancias,capacidade)
			#print("3 - {0} {1}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias),rota_melhorada))
		else:
			# salva vizinhança
			rota_melhorada = vizinhancas.vizinhanca_4(lista_de_rotas)
			#print("4 - {0} {1}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias),rota_melhorada))

		# Verifica se a nova solução é melhor
		if(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias) \
															< total_atual):
			#print("entrou aqui! {0} {1}".format(total_atual,funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias)))
			# salva a nova solução
			lista_de_rotas = copy.deepcopy(rota_melhorada)
			# atualiza o total
			total_atual = funcoesGenericas.total_percorrido(rota_melhorada,\
														matriz_de_distancias)
			sucesso = True # avisa que houve sucesso
			k = 1 # recomeça a visita às vizinhanças
		else:
			# caso contrário tenta achar uma melhora em outra vizinahnça
			k = k+1

	return lista_de_rotas, sucesso


def anelamento_simulado(lista_de_rotas, maximo_de_iteracoes,\
		maximo_de_perturbacoes_por_iteracao, maximo_de_sucessos_por_iteracao,\
		fator_de_reducao_de_temperatura, funcao_objetivo, matriz_de_distancias,\
		lista_de_demandas,capacidade):
		
	rota_melhorada = None

	delta_objetivo = 0
	Temperatura = TEMPERATURA_MAXIMA
	j = 1
	numero_de_sucessos = 0
	while(True):
		#print("prints {0}, {1}, {2}".format(j, funcao_objetivo(lista_de_rotas,\
		#												matriz_de_distancias), Temperatura))
		#pprint.pprint(rota_melhorada)
		numero_de_sucessos = 0
		i = 1
		# realiza as pertubações
		#debug_contador = 0
		while(True):
			
			# Realiza uma perturbação na solução
			rota_melhorada = vizinhancas.vizinhanca_1(lista_de_rotas)#,\
				 #lista_de_demandas, matriz_de_distancias, capacidade)
			
			# Verifica a diferença entre o atual e o riginal	
			delta_objetivo = funcao_objetivo(rota_melhorada,\
				matriz_de_distancias) - funcao_objetivo(lista_de_rotas,\
														matriz_de_distancias)
			# Se o delta for menor ou igual a 0, houve uma melhora 
			# (ou não houve piora)
			# Caso não tenha tido uma melhora o processo é mais probabilistico
			# Neste caso há uma probabilidade de aceitar a melhora de acordo
			# com a temperatura quanto maior a temperatura maior a chance de 
			# aceitar
			# Isto é dado pelo calculo e^(-delta_objetivo / temperatura)
			# A probabilidade P é dada pelo random()
			#print("prints(2) {0}, {4}, {1}, {2}, {3}".format(i, numero_de_sucessos, Temperatura, delta_objetivo,j))
			if(delta_objetivo <= 0 or \
							math.exp(-1 * delta_objetivo / Temperatura) 
														> random.random()):
				#print("Aceitou")
				lista_de_rotas = copy.deepcopy(rota_melhorada)
				numero_de_sucessos = numero_de_sucessos + 1

			i = i+1
			#debug_contador = debug_contador +1
			"""if(debug_contador == 100):
				os.system("PAUSE")
				debug_contador = 0"""
			if(numero_de_sucessos >= maximo_de_sucessos_por_iteracao\
							or i > maximo_de_perturbacoes_por_iteracao):
				break			
		
		Temperatura = fator_de_reducao_de_temperatura * Temperatura
		j = j+1

		if(numero_de_sucessos == 0 or j > maximo_de_iteracoes or Temperatura <= 1e-10):
    			break
	return 	rota_melhorada