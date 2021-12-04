def cpfMain():
	import random

	numeros = []
	j = 0

	qnt = input("Quantos CPF's você deseja gerar? ")
	if (qnt.isdigit() == True and int(qnt) >= 1):
		for j in range(0, 9):
			numeros.append(str(j))
		def gerarCpf():
			cpf = ''
			i = 0
			for i in range(0, 11):
				numero = random.choice(numeros)
				cpf += str(numero)
				if (i == 2 or i == 5):
					cpf += '.'
				elif (i == 8):
					cpf += '-'
			print(cpf)
		k = 0
# gerando a quantia de cpfs solicitados
		while (k < int(qnt)):
			gerarCpf()
			k += 1
	elif (qnt.isdigit() == False):
		print("Por favor, escolha uma quantidade válida.")
	elif (int(qnt) < 1):
		print("")
		print("ta aí, os seus 0 cpf, aproveite.")