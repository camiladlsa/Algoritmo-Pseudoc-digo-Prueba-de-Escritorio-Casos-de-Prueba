Cont = 1

while True:
	Number = input("\nIngrese el numero entero cuya persistencia aditiva desea saber: ")
	try: 
		Number = int(Number)
		if Number < 0:
			print("Debe ingresar un numero entero positivo! Intente nuevamente...")
			continue
		break
	except ValueError:
		print("Debe ingresar un numero entero! Intente nuevamente")

if (Number < 10):
	Cont = 0

def digits(Number):

	Sum_Of_Digits = 0
	while (Number > 0):
		Sum_Of_Digits += Number % 10
		Number = Number//10 

	print("")
	print(Sum_Of_Digits)
	return(Sum_Of_Digits)

ANS = digits(Number)

while (ANS > 9):
	ANS = digits(ANS)
	Cont += 1

print("\nLa persistencia aditiva de {} es {}.".format(Number, Cont))