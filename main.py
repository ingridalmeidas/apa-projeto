import funcoesGenericas
import math

def main():

	dimensao = 0
	qtd_veiculos = 0
	capacidade = 0
	lista_demandas = []
	matriz_distancias = []
	
	dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias = funcoesGenericas.le_instancia("instancias_teste/P-n19-k2.txt")
	
	construcao(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias)
	
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def construcao(dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias):
	
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
		
	for i in range(len(rota_veiculos)):
		print(rota_veiculos[i])
			
			
		
		
			
			
	
		
			
		
	

main()