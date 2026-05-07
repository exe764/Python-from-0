numero = int(input())

if numero == 0 :
    print("El número 0 tiene infinitos divisores")
else :
    valor_absoluto =abs(numero)
    contador_divisores = 0 
    for divisor in range (1, valor_absoluto + 1) : 
        if numero % divisor == 0 :
            contador_divisores = contador_divisores + 1
    print(f"El número {numero} tiene {contador_divisores} divisores (positivos)")