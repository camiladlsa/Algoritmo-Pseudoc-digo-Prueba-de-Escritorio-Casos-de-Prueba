# Persistencia Aditiva | Python 

START

1. Cont = 1
2. While True: 
	3. Number = input("Ingrese el numero entero cuya persistencia aditiva desea saber: ")
	4. Try: 
		5. Number = int(Number)
		6. If Number < 0 
			7. Print("Debe ingresar un numero entero positivo! Intente nuevamente")
		8. Number != int 
			9. Print("Debe ingresar un numero entero! Intente nuevamente")

10. def digits(Number)
	11. Define Sum_of_Digits = 0 
	12. while(Number > 0)
		13. Sum_Of_Digits =+ Number % 10 
		14. Number = Number//10 
	15. print(Sum_Of_Digits)
	16. return(Sum_Of_Digits)

	END of def

17. ANS = digits(Number)

18. while (ANS > 9)
	19. ANS = digits(ANS)
	20. Cont += 1

	END of while

21. Print("La persistencia aditiva de {} es {}.".format(Number, Cont))


END