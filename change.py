def change(): 
	gasto=float(input("Ingresar gasto:\n"))
	Recibido=float(input("Dinero recibido\n"))
	pesos=recibido-gasto
	centavos=(float(pesos)- int(pesos))*100


	print("\nVuelto")
	print("\nPesos:")
	print(int(pesos))
	print("\ncentavos:")
	print(int(centavos))
print(change())
