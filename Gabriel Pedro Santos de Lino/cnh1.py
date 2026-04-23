nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
possui_cnh = input("voce possui cnh ? \n1-sim\n2-Não ")

if idade >= 18:
    if possui_cnh == "1":
        print("Pode dirigir.")
    else:
        print("Não pode dirigir.")
else:
    print("Menor de idade")