print("Loja")

nome = input("Qual o nome do produto: ")
valor = float(input("Qual o valor do produto: "))
quantidade = int(input("Qual a quantidade do produto: "))

total = valor * quantidade

print(
  f"""
Compra aceita: 
Produto:{nome}
Valor Total: R${total}
"""
)