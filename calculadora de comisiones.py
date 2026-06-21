nombre = input("Ingrese su nombre: ")
ventas =float(input("Ingrese su  monto de ventas: "))
resultado = round (ventas * 1 /100, 2)
print(f"El empleado {nombre} tiene una comisión de {resultado:.2f}$")