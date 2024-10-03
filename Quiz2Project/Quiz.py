nombre = input("Nombre : ")
dias = int(input("Días: "))
salario = int (input("salario: "))


prima = salario * dias / 360
cesantias = salario * dias / 360
intereses_cesantias = cesantias * 0.12 / dias
vacaciones = salario * dias / 720
liquidacion = prima + cesantias + intereses_cesantias + vacaciones


print(f"Señor {nombre} para los {dias} días laborados y salario ${salario}, su liquidación se compone así:")
print(f"Prima: ${prima:.2f}")
print(f"Cesantía: ${cesantias:.2f}")
print(f"Intereses cesantías: ${intereses_cesantias:.2f}")
print(f"Vacaciones: ${vacaciones:.2f}")
print(f"Liquidación: ${liquidacion:.2f}")







