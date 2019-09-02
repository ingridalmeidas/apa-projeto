
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def le_instancia(nome):
	
	arq = open(nome, 'r')
	linhas = arq.readlines()		#le as linhas do arquivo
	
	for i in range(len(linhas)):
		
		print(i, linhas[i])
	
		linha_quebrada = linhas[i].split()	#quebra primeira linha
		
		if len(linha_quebrada) > 0:
			if linha_quebrada[0] == "DIMENSION:":
				dimensao = int(linha_quebrada[1])
				print("dimensao: ", dimensao)
		
			elif linha_quebrada[0] == "VEHICLES:":
				qtd_veiculos = int(linha_quebrada[1])
				print("veículos: " , qtd_veiculos)
		
			elif linha_quebrada[0] == "CAPACITY:":
				capacidade = int(linha_quebrada[1])
				print("capacidade: " , capacidade)
			
			elif linha_quebrada[0] == "DEMAND_SECTION:":
				lista_demandas = demand_section(linhas, i+1, dimensao)
				print("demandas: ")
				print(lista_demandas)
		
			elif linha_quebrada[0] == "EDGE_WEIGHT_SECTION":
			
				matriz_distancias = edge_weight_section(linhas, i+1, dimensao)
				
	return dimensao, qtd_veiculos, capacidade, lista_demandas, matriz_distancias 
	
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def demand_section(linhas, j, dimensao):
	
	lista_demandas = []
	
	for i in range(j, j+dimensao):
		
		print(i, linhas[i])
		
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

print(le_instancia("instancias_teste/P-n45-k5.txt"))
