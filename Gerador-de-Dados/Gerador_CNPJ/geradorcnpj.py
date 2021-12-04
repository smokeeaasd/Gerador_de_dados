def cnpjMain():
	import random
	numeros = []
	j = 0
 
	qnt = input("Quantos CNPJ's você deseja gerar? ")

	if (qnt.isdigit() == True and int(qnt) >= 1):
		for j in range(0, 9):
			numeros.append(str(j))
		def gerarCnpj():
			cnpj = ''
			i = 0
			for i in range(0, 10):
				numero = random.choice(numeros)
				cnpj += str(numero)
				if (i == 1 or i == 4):
					cnpj += '.'
				elif (i == 7):
					cnpj += ('/000' + str(random.randint(1, 2)) + '-')
			print(cnpj)
		k = 0
# gerando a quantia de cnpjs solicitados
		while (k < int(qnt)):
			gerarCnpj()
			k += 1
	elif (qnt.isdigit() == False):
		print("Por favor, escolha uma quantidade válida.")
	elif (int(qnt) == 0):
		print("")
		print("Ta aí, os seus 0 cnpj, aproveite.")