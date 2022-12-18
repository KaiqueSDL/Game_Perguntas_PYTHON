print('Jogo de perguntas')

jogar = input('Voce quer jogar? Digite -> (SIM) ')

if jogar != 'sim' : 
    quit()


pontos = 0 

print('Vamos começar as perguntas! ')

print(' 1 - BARCO \n 2 - LUA \n 3 - BUSSOLA')

resposta = int(input('Oque é a logo do PROA ? '))


match resposta:
    case 1:
       print(" ******* CORRETO !! ******")
       pontos += 1
    case 2:
        print('INCORRETO, TENTE OUTRA!')
    case 3:
         print('INCORRETO, TENTE NOVAMENTE!')




print(' 1 - 7 minutos \n 2 - 10 minutos \n 3 - 9 minutos')

resposta = int(input('Quanto tempo dura o pitch do demoday? '))


match resposta:
    case 1:
        print('INCORRETO, TENTE OUTRA!')
    case 2:
        print('INCORRETO, TENTE OUTRA!')
    case 3:
        print(" ******* CORRETO !! ******")
        pontos += 1



print(' 1 - Back End \n 2 - Front end \n 3 - Machine Learning')

resposta = int(input('Python é mais usado em qual área '))


match resposta:
    case 1:
        print(" ******* CORRETO !! ******")
        pontos += 1
    case 2:
        print('INCORRETO, TENTE OUTRA!')
    case 3:
       print('INCORRETO, TENTE OUTRA!')


print("Sua pontuação total ficou em -- " + str(pontos))