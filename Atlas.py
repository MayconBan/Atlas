import funcoes 
import random 
import os

#variaveis que estão sendo usadas
n = str("ATLAS")
i = 0
Senha_de_adimim = 

#mensagem inicial
print("{}olá bom dia ".format(n))
print('{}''Como vc gostaria de ser chamado'.format(n))

#gerador de nuneros aleatorios 
na = random.randint(0,100)

#define seu nome
NomePlayer = input("???: ")

#loop de perguntas e respostas
while True:
	
	#Onde pega a pergunta
	pergunta = input("{}:".format(NomePlayer))
	
	#funções
	if pergunta in ["sair", "desligar", "off"]:
		funcoes.desligar()
	
	elif pergunta in ["adivinha", "adivinha "]:
				while i < 1:
					funcoes.adivinha()
					p = input('Quer continuar(s/n) ')
					if p == "n" :
						i += 1
				i -= 1
	
	elif pergunta in ["calculadora", "calculadora "]:
		while i < 1:
			funcoes.calculadora()
			p = input('Quer continuar(s/n)')
			if p == "n":
				i += 1
		i -= 1
	
	elif pergunta in["apagar ", "apagar", "dessito", "dessito "]:
		while i < 3:
			s = input("Senha de adimim:")
			if s == Senha_de_adimim:
				os.romove("/storage/emulated/0/Atlas")
				funcoes.desligar()
			else:
				i += 1
		i -= 3
	elif pergunta in["redefinir nome"]:
		NomePlayer = input("novo nome: ")

	#respostas
	elif pergunta in ["ola", "oi", "ei", "olá", "ola ", "oi ", "ei ", "olá " ]:
		print("{}Olá {} como vai".format(n, NomePlayer))
		
	elif pergunta in ["tudo bem", "tudo bem?", "tudo bem ", "tudo bem?", "como vai ", "como vai", "como vai?", "como vai ?"]:
		
		if na == 69:
			print("{}Estou levando a vida e a cada dia esta pior ".format(n))
		
		else:print("{}Estou bem sim gracas ao algoristimo ".format(n))
	
	#comandos de teste
	match pergunta:
		case "taboada":
			funcoes.taboada()
		case "/":
			print(na)
		case "£":
			print()

