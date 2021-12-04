from Gerador_CPF import geradorcpf as cpf
from Gerador_CNPJ import geradorcnpj as cnpj
print('1 => Gerador de CPF')
print('2 => Gerador de CNPJ')
print('')
escolha = 0
i = 0;

escolha = input('Escolha uma das opções: ')
print('')

while (i == 0):
	if (escolha == '1'):
		cpf.cpfMain()
		break;
	elif (escolha == '2'):
		cnpj.cnpjMain()
		break;
	elif (escolha.isdigit() == False or escolha > '2' or escolha < '1'):
		print("Por favor, escolha uma opção válida.")
		break;