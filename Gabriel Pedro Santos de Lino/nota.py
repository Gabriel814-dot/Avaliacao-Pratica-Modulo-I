nome = input("digite o nome do aluno")
nota = float(input("digite a nota "))
nota2 = float(input("digite a outra nota"))
nota = float(input("digite outra nota"))
media = (nota1 + nota2 + nota3 ) / 3 

if media >= 7: 
    print("APROVADO")
elif media > 4:
    print("RECUPERAÇAO")
else:
    print("REPROVADO")