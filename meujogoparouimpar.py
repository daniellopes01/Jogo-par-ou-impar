# -*- coding: utf-8 -*-
"""MeuJogoParOuImpar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aeYLlNUAbjwoL10ZpSwYIyxy-HWm8uea

# JOGO PAR OU ÍMPAR

1. Definir quem serão os jogadores
2. Definir quem escolhe primeiro
3. Definir a escolha entre PAR ou ÍMPAR
4. Coletar os números escolhidos pelos jogadores
5. Calcula se a soma dos números é PAR ou ÍMPAR
5. Informar quem ganhou!
"""

jogador1 = input("-> digite o nome do primeiro jogador")
jogador2 = input("-> digite o nome do segundo jogador")

print(f"Quem escolhe primeiro, {jogador1} ou {jogador2}")
primeiro_jogador = input(f"digite 1 para escolher {jogador1} ou 2 para escolher {jogador2}.")
segundo_jogador = None

if primeiro_jogador == "1":
  primeiro_jogador = jogador1
  segundo_jogador = jogador2
elif primeiro_jogador == "2":
  primeiro_jogador = jogador2
  segundo_jogador = jogador1

print("Digite 1 para escolher PAR ou 2 para escolher IMPAR")
escolha = input(f"{primeiro_jogador}, voce quer par ou impar?")
escolha2 = None

if escolha == "ímpar" or escolha == "impar" or escolha == "1":
  escolha = "impar"
  escolha2 = "par"
elif escolha == "par" or escolha == "0":
  escolha = "par"
  escolha2 = "impar"

print(f"{segundo_jogador}, voce ficou com {escolha2}")

numero1 = int(input(f"{primeiro_jogador}, escolha um numero:"))
numero2 = int(input(f"{segundo_jogador}, escolha um numero:"))

soma = numero1 + numero2

if soma % 2 == 0:
  vencedor = "par"
else:
  vencedor = "impar"

if vencedor == escolha:
  print(f"{primeiro_jogador} venceu! 😎😎")
else:
  print(f"{segundo_jogador} venceu! 😎😎")