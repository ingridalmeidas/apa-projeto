import vizinhancas
import funcoesGenericas
import copy

MAXIMO = 3

def vnd(lista_de_rotas,lista_de_demandas,matriz_de_distancias,capacidade):
	rota_melhorada = None # salgvará as novas rotas
	teve_melhoria = 1 # flag que avisa se teve melhoria
	total_atual = funcoesGenericas.total_percorrido(lista_de_rotas,matriz_de_distancias)
	while(teve_melhoria):
		teve_melhoria = 0
		for i in range(MAXIMO):
			if(i == 0):
				rota_melhorada = vizinhancas.vizinhanca_1(lista_de_rotas)
				print("1 - {}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias)))
			elif(i == 1):
				rota_melhorada = vizinhancas.vizinhanca_2(lista_de_rotas,\
												lista_de_demandas,capacidade)
				print("2 - {}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias)))
			else:
    			# vizinhanca_3 necessita ser implementada
				rota_melhorada = vizinhancas.vizinhanca_3(lista_de_rotas,\
												 lista_de_demandas,capacidade)
				print("3 - {}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias)))

			if(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias) \
																< total_atual):
				print("entrou aqui! {0} {1}".format(total_atual,funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias)))
				lista_de_rotas = copy.deepcopy(rota_melhorada)
				teve_melhoria = 1
		
	return lista_de_rotas