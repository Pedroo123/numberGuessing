# Jogo de adivinhação de numeros aleatorios

## Imports
import random

n = random.randint(1, 10)


def score_calculator(typed_number):
    score = 100

    if (typed_number == n):
        print("Resposta Correta!")
        print("Seu Score final é: ", score)
    else:
        print("Resposta Incorreta")
        score = score - 10

    return score


def number_tips(typed_number):

    if(n in range(1, 5) and typed_number != n):
        print("O numero gerado está entre 1 e 5")
    elif(n in range(6, 10) and typed_number != n):
        print("O numero gerado está entre 6 e 10")
    else:
        print("Valor digitado é invalido")


def guess_number():
    print("Adivinhe o numero! Ele está entre 1 e 10")

    typed_number = ""

    while (typed_number != n):
        typed_number = input("Digite um numero: ")

        number_tips(typed_number)
        final_score = score_calculator(typed_number)

        print(final_score)

guess_number()
