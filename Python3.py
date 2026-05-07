n = int(input())

es_primo = True

if n == 1:
    es_primo = False
else:
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número {n} SI es PRIMO")
else:
    print(f"El número {n} NO es primo")