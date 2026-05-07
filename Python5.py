while True:
    numero_original  = int(input())
    if numero_original >= 0:
        break
    
sumaresto = 0
numero = numero_original 

while numero > 0:
    resto = numero % 10
    sumaresto = sumaresto + resto 
    numero = numero // 10
    
print(f"La suma de los dígitos de {numero_original} es {sumaresto}")


