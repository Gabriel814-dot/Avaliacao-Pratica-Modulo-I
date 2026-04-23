peso = float(input("digite seu peso"))
altura = float (input("digite seu altura"))
imc = peso / altura **2

if imc >=30.0:
    print("cuidado com a saude ")
else:
    print("tudo ok!")
