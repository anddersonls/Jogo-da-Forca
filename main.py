#jogo da forca
import random 
import lista

def menu():
  print("*********************************")
  print("***Bem vindo ao Jogo da Forca!***")
  print("*********************************\n")
  print('1 - Vamos jogar Forca!')
  print('2 - Sair do Jogo')
  usuario = int(input('Sua escolha: '))
  
  if usuario == 1:
    game()
  elif usuario == 2:
    print('\nObrigado por jogar! Não esqueça de vir mais vezes!')
  else: 
    print('\nVoce digitou um valor inválido, tente novamente!\n\n')
    menu()
  
def game():
  print('\nEscolha o tema do jogo!\n')
  print('1 - Objetos')
  print('2 - Frutas')
  print('3 - Voltar para o Menu!')
  tema = int(input('Sua escolha: '))

  if tema == 1:
    palavra = random.choice(lista.objetos)
    forca(palavra)
  if tema == 2:
    palavra = random.choice(lista.frutas)
    forca(palavra)
  if tema == 3:
    menu()
  else:
    print('\nVoce digitou um valor inválido, tente novamente!')
    game()
    
    
def forca(palavra):
  jogando = True
  errou = 0
  qtd_letras = len(palavra)
  letras_descobertas = list(qtd_letras*'_')
  
  while jogando:
    desenha_forca(errou)
    for i in range(len(letras_descobertas)):
      print(letras_descobertas[i], end=' ')
    
    chute = input('Chute uma letra: ')

    if chute not in palavra:
      errou += 1
      if errou == 7:
        desenha_forca(errou)
        perdeu(palavra)
        jogando = False
        
    for j in range(qtd_letras):
      if palavra[j] == chute:
        letras_descobertas[j] = palavra[j]
    
    if '_' not in letras_descobertas:
      for i in range(len(letras_descobertas)):
        print(letras_descobertas[i], end=' ')
      ganhou()
      jogando = False  

def desenha_forca(errou):
    print("  _______     ")
    print(" |/      |    ")

    if(errou == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errou == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errou == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errou == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errou == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errou == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errou == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def perdeu(palavra):
  print("\n\nInfelizmente você não venceu, talvez na próxima!")
  print(f"A palavra era {palavra}")
  print("    _______________         ")
  print("   /               \       ")
  print("  /                 \      ")
  print("//                   \/\  ")
  print("\|   XXXX     XXXX   | /   ")
  print(" |   XXXX     XXXX   |/     ")
  print(" |   XXX       XXX   |      ")
  print(" |                   |      ")
  print(" \__      XXX      __/     ")
  print("   |\     XXX     /|       ")
  print("   | |           | |        ")
  print("   | I I I I I I I |        ")
  print("   |  I I I I I I  |        ")
  print("   \_             _/       ")
  print("     \_         _/         ")
  print("       \_______/           \n\n")
  menu()

def ganhou():
  print("\n\nParabéns, você venceu o jogo!")
  print("       ___________      ")
  print("      '._==_==_=_.'     ")
  print("      .-\\:      /-.    ")
  print("     | (|:.     |) |    ")
  print("      '-|:.     |-'     ")
  print("        \\::.    /      ")
  print("         '::. .'        ")
  print("           ) (          ")
  print("         _.' '._        ")
  print("        '-------'       \n\n")
  menu()
  
menu()
  