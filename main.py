'''
verificare de numar prim
'''

def is_prim(nr):
	if nr < 2:
		return False
	for i in range(2, nr):
		if nr % i == 0:
			return False
	return True

'''
produsul a n numere naturale 
'''
def produs(lst):
	p = 1
	for i in range(len(lst)):
		p = p * i
		return p

'''
cmmdc al doua numere x si y folosind primul algoritm
'''
def cmmdc1(x, y):
	while x != y:
		if x > y:
			x = x - y
		else:
			y = y - x
		return x

'''
cmmdc al doua numere x si y folosind al doilea algoritm
'''

def cmmdc2(x , y):
	while (y != 0):
		r = x % y
		x = y
		y = r
	return x


def main():
	while True:
		print ('1.verifica daca un numar este prim.')
		print ('2.produsul a n numere naturale.')
		print ('3.cmmdc primul algoritm.')
		print ('4.cmmdc al doilea algoritm.')
		print ('5.exit.')

		optiune = input('alegeti optiunea dorita:')

		if optiune == '1':
			nr = int(input('Numarul care doriti sa se verifice: '))
			if is_prim(nr):
				print('Numarul dat este prim!')
			else:
				print('Numarul dat nu este prim.')

		if optiune == '2':
			'''numar = input('Dati numerele separate prin spatiu: ')
			numar_split = numar.split(' ')
			numar_int = []
			for i in numar.split:
				numar_int.append(int(numar))
				produs(numar)
			'''
			nr = int(input('dau lungimea sirului de :'))
			produs = 1
			for i in range(1, nr + 1):
				x = int(input('dati caractere'))
				produs = produs * x
			print(produs)

		if optiune == '3':
			x = int(input('dati primul numar:'))
			y = int(input('dati al doilea numar:'))
			z= cmmdc1(x,y)
			print(z)

		if optiune == '4':
			x = int(input('dati primul numar:'))
			y = int(input('dati al doilea numar:'))
			z= cmmdc2(x,y)
			print(z)

main()