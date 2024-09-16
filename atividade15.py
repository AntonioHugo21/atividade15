# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

num1 = float(input("digite o numero 1"))
num2 = float(input("digite o numero 2"))
operacao = input("escolha uma operação : soma, subtração, multiplicação ou divisão")

if operacao == "soma":
    print(num1+num2)
elif operacao == "subtração":
    print(num1-num2)
elif operacao == "multiplicação":
    print(num1*num2)
elif operacao == "divisão":
    print(num1/num2)