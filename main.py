cont = int(0)
casos = int(input())
while cont < casos:
    poder = int(input())
    if poder > 8000:
        print("Mais de 8000!")
    else:
        print("Inseto!")
    cont = cont + 1