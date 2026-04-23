valor_original = float(input("digite o preco do produto"))
desconto = int(input("digite a porcetagem do desconto: "))
valor_desconto = valor_original * (desconto/100)
preco_final = valor_original - valor_desconto
print(f"o preço final da compra sera de R$ {preco_final}")