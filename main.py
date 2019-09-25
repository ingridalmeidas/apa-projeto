import funcoesGenericas
from metaheuristicas import *
import math

def main():

	# Dados da instância
	dimensao = 0 # Quantidade de demandas
	qtd_veiculos = 0 # Quantidade de veículos
	capacidade = 0 # Capacidade dos veículos
	lista_demandas = [] # Lista com o valor de todas as demandas
	matriz_distancias = [] # Lista com as referências das distâncias
	
	dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias = \
				  funcoesGenericas.le_instancia("instancias_teste/P-n23-k8.txt")
	
	#rota_veiculos = construcao_gulosa_distancia(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias)
	rota_veiculos = construcao_gulosa_razao(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias)
	#rota_veiculos = construcao_extra(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias)
	
	#busca_local(rota_veiculos, lista_demandas, matriz_distancias, capacidade)
	

	
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def construcao_gulosa_distancia(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias):
	
	rota_veiculos = [] #Esta será uma lista de rotas, onde cada rota corresponde a rota de um veiculo
	rota = [] #Esta lista servirá para criar as rotas e adicionar na lista de rotas
	
	local_atual = 0 #Vai indicar o cliente onde o veículo se encontra. Inicia no depósito
	capacidade_atual = 0 #Vai indicar a capacidade do veículo que já foi atendida
	
	menor_distancia = math.inf #Vai auxiliar a encontrar o cliente de menor distancia, iniciado com infinito para as comparações
	clientes_possiveis = [] #Lista que vai armazenar os clientes possíveis de serem visitados que não estouram a capacidade do veículo
	
	clientes_visitados = [] #Essa lista vai armazenar os clientes que já foram visitados
	clientes_visitados.append(0) #Adiciona o depósito na lista de clientes já visitados, pois os veículos iniciam lá
	
	for v in range(qtd_veiculos): #Para cada veículo
	
		rota.append(0) #Adiciona o depósito ao início da rota
	
		#Esse for e o conteudo dele verificam os clientes que ainda não foram visitados e os que não estouram a capacidade do veículo
		for cliente in range(dimensao):
			
			capacidade_temporaria = capacidade_atual + lista_demandas[cliente]
			
			if (cliente not in clientes_visitados) and (capacidade_temporaria <= capacidade):
				clientes_possiveis.append(cliente)
		
		while(len(clientes_possiveis) > 0): #Enquanto existir clientes que podem ser visitados sem que a capacidade do veículo estoure
			
			#Esse for vai percorrer os possíveis clientes e vai escolher o de menor distância para que seja o próximo local visitado
			for cliente in clientes_possiveis:				
				if matriz_distancias[local_atual][cliente] < menor_distancia:
					menor_distancia = matriz_distancias[local_atual][cliente]
					cliente_escolhido = cliente
		
			local_atual = cliente_escolhido #Atualiza o local atual
			rota.append(local_atual) #Adiciona o local a rota
			capacidade_atual += lista_demandas[local_atual] #Atualiza a capacidade que o veículo está carregando
			clientes_visitados.append(local_atual) #Indica o local como um cliente que já foi visitado
			menor_distancia = math.inf 
			clientes_possiveis = []
			
			#Esse for e o conteudo dele verificam os clientes que ainda não foram visitados e os que não estouram a capacidade do veículo
			for cliente in range(dimensao):
			
				capacidade_temporaria = capacidade_atual + lista_demandas[cliente]
			
				if (cliente not in clientes_visitados) and (capacidade_temporaria <= capacidade):
					clientes_possiveis.append(cliente)
					
		rota.append(0) #Adiciona o depósito ao fim da rota
		rota_veiculos.append(rota) #Adiciona a rota construída a lista que armazena a rota de cada veículo
		rota = []
		local_atual = 0
		capacidade_atual = 0

	print("Construção gulosa distância:  \n")
	print("Distância inicial: ", funcoesGenericas.total_percorrido(rota_veiculos,matriz_distancias))
	print(rota_veiculos)
	print("\n")
	print(clientes_visitados)
	
	contador_clientes = 0
	
	for i in range(dimensao):
		if i in clientes_visitados:
			#print(i)
			contador_clientes += 1
	
	print(contador_clientes)
	
	return rota_veiculos

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def construcao_gulosa_razao(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias):

	rota_veiculos = [] #Esta será uma lista de rotas, onde cada rota corresponde a rota de um veiculo
	rota = [] #Esta lista servirá para criar as rotas e adicionar na lista de rotas
	
	local_atual = 0 #Vai indicar o cliente onde o veículo se encontra. Inicia no depósito
	capacidade_atual = 0 #Vai indicar a capacidade do veículo que já foi atendida
	
	menor_razao = math.inf #Vai auxiliar a encontrar o cliente de menor distancia, iniciado com infinito para as comparações
	clientes_possiveis = [] #Lista que vai armazenar os clientes possíveis de serem visitados que não estouram a capacidade do veículo
	
	clientes_visitados = [] #Essa lista vai armazenar os clientes que já foram visitados
	clientes_visitados.append(0) #Adiciona o depósito na lista de clientes já visitados, pois os veículos iniciam lá
	
	for v in range(qtd_veiculos): #Para cada veículo
	
		rota.append(0) #Adiciona o depósito ao início da rota
	
		#Esse for e o conteudo dele verificam os clientes que ainda não foram visitados e os que não estouram a capacidade do veículo
		for cliente in range(dimensao):
			
			capacidade_temporaria = capacidade_atual + lista_demandas[cliente]
			
			if (cliente not in clientes_visitados) and (capacidade_temporaria <= capacidade):
				clientes_possiveis.append(cliente)
		
		while(len(clientes_possiveis) > 0): #Enquanto existir clientes que podem ser visitados sem que a capacidade do veículo estoure
			
			#Esse for vai percorrer os possíveis clientes e vai escolher o de menor distância para que seja o próximo local visitado
			for cliente in clientes_possiveis:
				
				razao = matriz_distancias[local_atual][cliente]/lista_demandas[cliente]
				
				if razao < menor_razao:
					menor_razao = razao
					cliente_escolhido = cliente
		
			local_atual = cliente_escolhido #Atualiza o local atual
			rota.append(local_atual) #Adiciona o local a rota
			capacidade_atual += lista_demandas[local_atual] #Atualiza a capacidade que o veículo está carregando
			clientes_visitados.append(local_atual) #Indica o local como um cliente que já foi visitado
			menor_razao = math.inf 
			clientes_possiveis = []
			
			#Esse for e o conteudo dele verificam os clientes que ainda não foram visitados e os que não estouram a capacidade do veículo
			for cliente in range(dimensao):
			
				capacidade_temporaria = capacidade_atual + lista_demandas[cliente]
			
				if (cliente not in clientes_visitados) and (capacidade_temporaria <= capacidade):
					clientes_possiveis.append(cliente)
					
		rota.append(0) #Adiciona o depósito ao fim da rota
		rota_veiculos.append(rota) #Adiciona a rota construída a lista que armazena a rota de cada veículo
		rota = []
		local_atual = 0
		capacidade_atual = 0

	print("Construção gulosa razao:  \n")
	print("Distância inicial: ", funcoesGenericas.total_percorrido(rota_veiculos,matriz_distancias))
	print(rota_veiculos)
	print("\n")
	
	contador_clientes = 0
	
	for i in range(dimensao):
		if i in clientes_visitados:
			#print(i)
			contador_clientes += 1
	
	print(contador_clientes)
	
	if contador_clientes < dimensao:
		rota_veiculos = construcao_extra(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias)
	
	print("Construção gulosa por demanda:  \n")
	print("Distância inicial: ", funcoesGenericas.total_percorrido(rota_veiculos,matriz_distancias))
	print(rota_veiculos)
	print("\n")
	
	
	
	
	return rota_veiculos
	
	
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def construcao_extra(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias):
	
	rota_veiculos = [] #Esta será uma lista de rotas, onde cada rota corresponde a rota de um veiculo
	rota = [] #Esta lista servirá para criar as rotas e adicionar na lista de rotas
	
	local_atual = 0 #Vai indicar o cliente onde o veículo se encontra. Inicia no depósito
	capacidade_atual = 0 #Vai indicar a capacidade do veículo que já foi atendida
	
	maior_demanda = 0 #Vai auxiliar a encontrar o cliente de menor distancia, iniciado com infinito para as comparações

	clientes_possiveis = [] #Lista que vai armazenar os clientes possíveis de serem visitados que não estouram a capacidade do veículo
	
	clientes_visitados = [] #Essa lista vai armazenar os clientes que já foram visitados
	clientes_visitados.append(0) #Adiciona o depósito na lista de clientes já visitados, pois os veículos iniciam lá
	
	for v in range(qtd_veiculos): #Para cada veículo
	
		rota.append(0) #Adiciona o depósito ao início da rota
	
		#Esse for e o conteudo dele verificam os clientes que ainda não foram visitados e os que não estouram a capacidade do veículo
		for cliente in range(dimensao):
			
			capacidade_temporaria = capacidade_atual + lista_demandas[cliente]
			
			if (cliente not in clientes_visitados) and (capacidade_temporaria <= capacidade):
				clientes_possiveis.append(cliente)
		
		while(len(clientes_possiveis) > 0): #Enquanto existir clientes que podem ser visitados sem que a capacidade do veículo estoure
			for cliente in clientes_possiveis:
				if lista_demandas[cliente] > maior_demanda:
					maior_demanda = lista_demandas[cliente]
					cliente_escolhido = cliente
		
			local_atual = cliente_escolhido #Atualiza o local atual
			rota.append(local_atual) #Adiciona o local a rota
			capacidade_atual += lista_demandas[local_atual] #Atualiza a capacidade que o veículo está carregando
			clientes_visitados.append(local_atual) #Indica o local como um cliente que já foi visitado
			maior_demanda = 0 
			clientes_possiveis = []
			
			#Esse for e o conteudo dele verificam os clientes que ainda não foram visitados e os que não estouram a capacidade do veículo
			for cliente in range(dimensao):
			
				capacidade_temporaria = capacidade_atual + lista_demandas[cliente]
			
				if (cliente not in clientes_visitados) and (capacidade_temporaria <= capacidade):
					clientes_possiveis.append(cliente)
					
		rota.append(0) #Adiciona o depósito ao fim da rota
		rota_veiculos.append(rota) #Adiciona a rota construída a lista que armazena a rota de cada veículo
		rota = []
		local_atual = 0
		capacidade_atual = 0
	
	contador_clientes = 0
	
	for i in range(dimensao):
		if i in clientes_visitados:
			#print(i)
			contador_clientes += 1
	
	print(contador_clientes)
	
	return rota_veiculos



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def busca_local(rota_veiculos, lista_demandas, matriz_distancias, capacidade):
	
	sucesso = False
	while(not sucesso):	
		nova_rota,sucesso = vnd(rota_veiculos,lista_demandas,matriz_distancias,capacidade)
		#print("Tentando...\n")
	nova_rota_2 = anelamento_simulado(nova_rota, 200,200,200,0.75,\
		funcoesGenericas.total_percorrido,matriz_distancias,lista_demandas,\
			capacidade)
	
	for i in range(len(rota_veiculos)):
		print("rota {0}: {1}".format(i,rota_veiculos[i]))
	print("distância total percorrida: {0}\n".format(funcoesGenericas.\
							total_percorrido(rota_veiculos,matriz_distancias)))
	
	print("Após realizar alteração")
	for i in range(len(rota_veiculos)):
			print("rota {0}: {1}".format(i,nova_rota[i]))
	print("distância total percorrida: {0}\n\n".format(funcoesGenericas.\
							total_percorrido(nova_rota,matriz_distancias)))

	print("Após realizar a segunda alteração")
	for i in range(len(rota_veiculos)):
			print("rota {0}: {1}".format(i,nova_rota_2[i]))
	print("distância total percorrida: {0}\n\n".format(funcoesGenericas.\
							total_percorrido(nova_rota_2,matriz_distancias)))



main()