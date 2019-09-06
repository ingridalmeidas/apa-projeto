
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def le_instancia(nome):
	
	arq = open(nome, 'r')
	linhas = arq.readlines()		#le as linhas do arquivo
	
	for i in range(len(linhas)):
	
		linha_quebrada = linhas[i].split()	#quebra primeira linha
		
		if len(linha_quebrada) > 0:
			if linha_quebrada[0] == "DIMENSION:":
				dimensao = int(linha_quebrada[1])
		
			elif linha_quebrada[0] == "VEHICLES:":
				qtd_veiculos = int(linha_quebrada[1])
		
			elif linha_quebrada[0] == "CAPACITY:":
				capacidade = int(linha_quebrada[1])
			
			elif linha_quebrada[0] == "DEMAND_SECTION:":
				lista_demandas = demand_section(linhas, i+1, dimensao)
		
			elif linha_quebrada[0] == "EDGE_WEIGHT_SECTION":
			
				matriz_distancias = edge_weight_section(linhas, i+1, dimensao)

	return dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias 
	
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def demand_section(linhas, j, dimensao):
	
	lista_demandas = []
	
	for i in range(j, j+dimensao):
		
		linha_quebrada = linhas[i].split()
		
		lista_demandas.append(int(linha_quebrada[1]))
		
	return lista_demandas
	
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def edge_weight_section(linhas, j, dimensao):

	matriz_distancias = []
	
	for i in range(j, j+dimensao):
		
		linha_quebrada = linhas[i].split()
		
		l = []
		
		for d in range(dimensao):
			l += [int(linha_quebrada[d])]
		
		matriz_distancias += [l]
	
	return matriz_distancias

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# calcula o caminho total percorrido
def total_percorrido(lista_de_rotas, matriz_de_distancias):
	total = 0
	for rota in lista_de_rotas:
		for local in range(len(rota)-1):
			total = total + matriz_de_distancias[rota[local]][rota[local+1]]
	
	return total
