n = int(input())

ncopia = n
invertido = 0

while ncopia > 0:
    resto = ncopia % 10
    invertido = invertido * 10 + resto
    ncopia = ncopia // 10
    
if n == invertido:
    print(f"El número {n} SI es palíndromo")
else:
    print(f"El número {n} NO es palíndromo")
    