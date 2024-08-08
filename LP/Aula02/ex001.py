print("Faixa Etaria")

idade = int(input("Qual a sua idade: "))

if idade < 5:
    print("Acesso negado")
elif idade < 15:
    print("Criança")
elif idade < 20:
    print("Adolecente")
else:
    print("Adulto")