print ("Vamos jogar um jogo legal, de adivinhação:")
SN= (input("y/n: "))

if SN == "y" :
    print ( "Então Vamos a diga: eu tenho menos que 40 e mais que 20:")
    idade = 30 #minha variavel idade exata
    rodada = 5

# 
    for tentativa_numero in range (1,rodada + 1):

        tentativa = int(input("Rodada {} : Qual é a minha idade?".format(tentativa_numero)))
        if tentativa == idade:
            print ("Parabens você acertou")
            break 
        else:
            print("Você errou!")
    
    # usando  para caso nao acerte todas as tentativas ele vai dar a resposta.
    if tentativa != idade:
        print ("A tu errou tudo, minha idade é {}".format (idade))


    else:
        print("Que pena seria legal brincar")
    



