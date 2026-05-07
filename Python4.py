while True : 
    numero = int(input())
    if numero >= 0 :
        break
    
if numero == 0 :
    print("0 tiene 1 dígito(s)")
else:
    largo = 0 
    copia_numero = numero
    while numero != 0 :
        largo = largo + 1
        numero = numero // 10

    print(copia_numero, "tiene", largo, "dígito(s)")