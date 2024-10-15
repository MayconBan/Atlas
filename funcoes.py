n = "Atlas:"
#Mensagem de desligar
#Hang up message
class desligar(object):
   def __init__(self):
   	self.msg = print("Atlas: Tchau")
   	self.off =exit()
   	def desligar(self):
   		print()
   		
#taboada
#multiplication table
class taboada(object):
	def __init__(self):
         taboada =int(input('{} digite um numero - '.format(n)))
         print('=-=-'*20)
         print('{}×1={}'.format(tab,tab*1))
         print('{}×2={}'.format(tab,tab*2))
         print('{}×3={}'.format(tab,tab*3))
         print('{}×4={}'.format(tab,tab*4))
         print('{}×5={}'.format(tab,tab*5))
         print('{}×6={}'.format(tab,tab*6))
         print('{}×7={}'.format(tab,tab*7))
         print('{}×8={}'.format(tab,tab*8))
         print('{}×9={}'.format(tab,tab*9))
         print('{}×10={}'.format(tab,tab*10))
         print('=-=-'*20)
         def taboada(self):
         	print()

#antessesor e sucessor
#predecessor and successor
class antessesor(object):
   def __init__(self):
   	n =int(input('{}digite um numero -').format(n))
   	a = n - 1
   	s = n + 1
   	print('o numero digitado foi {}, seu anterssesor e {}, e seu sucessor e {}'.format(n,a,s))
   	def antessesor(self):
   		print()

#Calculadora 
#calculator
class calculadora(object):
	def __init__(self):
		
		expressao_matematica = input('{}digite uma expresão matematica-'.format(n))
		
		resposta = eval(expressao_matematica)
		
		print('o resutado e ',resposta)
		
		def calculadora(self):
			print()
#akineitor number			
class adivinha(object):
	def __init__(self):
		
		h = input('{}pense num numero e digite-o '.format(n))
		
		print('{}voce pensou no numero {} '.format(n,h))
		
		def adivinha(self):
			print()

