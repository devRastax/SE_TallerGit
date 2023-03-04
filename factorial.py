num = int(input("Introduzca un número entero: "))
rest = 1
for i in range(1,num+1): rest = rest * i
print ("El factorial de %s es %s" % (num, rest))