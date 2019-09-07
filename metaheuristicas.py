import vizinhancas
import funcoesGenericas
import copy

MAXIMO = 3

def vnd(lista_de_rotas,lista_de_demandas,matriz_de_distancias,capacidade):
	rota_melhorada = None # salgvará as novas rotas
	teve_melhoria = True # flag que avisa se teve melhoria
	sucesso = False
	total_atual = funcoesGenericas.total_percorrido(lista_de_rotas,matriz_de_distancias)
	k = 1
	while(k <= MAXIMO):
		if(k == 1):
			rota_melhorada = vizinhancas.vizinhanca_1(lista_de_rotas)
			print("1 - {0} {1}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias),rota_melhorada))
		elif(k == 2):
			rota_melhorada = vizinhancas.vizinhanca_2(lista_de_rotas,\
											lista_de_demandas,capacidade)
			print("2 - {0} {1}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias),rota_melhorada))
		else:
			# vizinhanca_3 necessita ser implementada
			rota_melhorada = vizinhancas.vizinhanca_3(lista_de_rotas,\
						lista_de_demandas,matriz_de_distancias,capacidade)
			print("3 - {0} {1}".format(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias),rota_melhorada))

		if(funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias) \
															< total_atual):
			print("entrou aqui! {0} {1}".format(total_atual,funcoesGenericas.total_percorrido(rota_melhorada,matriz_de_distancias)))
			lista_de_rotas = copy.deepcopy(rota_melhorada)
			teve_melhoria = True
			sucesso = True
			k = 1
		else:
			k = k+1

	return lista_de_rotas, sucesso