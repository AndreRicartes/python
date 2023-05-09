#Comando para saída de dados
print("Olá Mundo!")

#Entrar com 'n' valores e mostrar o menor

n = float(input("Quantos valores serão inseridos? "))
cont = 0

menor = valor
while cont < n:
    valor = float(input("Entre com o valor: "))
    cont += 1
    if menor > valor:
        menor = valor
    print(valor)
print(menor)






