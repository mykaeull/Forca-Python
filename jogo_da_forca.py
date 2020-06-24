import time

print("="*20)
print("   JOGO DA FORCA ")
print("="*20)

while True:
    palavra = str(input("PALAVRA SECRETA: ")).upper()
    dica = str(input("DICA(máx. 50 caracteres): ")).upper()
    while len(dica) > 50:
        print("--"*25)
        print("DICA ULTRAPASSOU O LIMITE DE CARACTERES PERMITIDO!")
        print("DIGITE NOVAMENTE...")
        print("--"*25)
        dica = str(input("DICA(máx. 50 caracteres): "))
    digitadas = []
    letras_digitadas = []
    vidas = 6
    c = 0

    print("--"*25)
    print("O JOGO VAI COMEÇAR...")
    print("--"*25)
    time.sleep(3)

    while True:
        print(f"VOCÊ TEM {vidas} VIDAS")
        print(f"DICA: {dica}")
        letra = str(input("LETRA: ")).upper()
        while len(letra) > 1 or letra.isnumeric() == True:
            print("--"*25)
            print("ERRO!")
            print("DIGITE APENAS UMA LETRA")
            print("--"*25)
            letra = str(input("LETRA: ")).upper()
        digitadas.append(letra)
        #if c == 0:
            #letras_digitadas.append(letra)
        #else:
            #while letra in letras_digitadas:
                #print(f"A LETRA '{letra}' JÁ FOI ESCOLHIDA")
                #print("DIGITE OUTRA LETRA")
                #letra = str(input("LETRA: ")).upper()
        #c += 1
        if letra in palavra:
            print("--"*25)
            print(f"A LETRA '{letra}' EXISTE NA PALAVRA")
        else:
            print("--"*25)
            print(f"A LETRA '{letra}' NÃO EXISTE NA PALAVRA")
            digitadas.pop()
            vidas = vidas - 1
        palavra_comp = ''
        for letra_secreta in palavra:
            if letra_secreta in digitadas:
                palavra_comp += letra_secreta
            else:
                palavra_comp += '*'
        print(f"PALAVRA: {palavra_comp}")
        print("--"*25)
        if vidas < 1:
            print("VOCÊ PERDEU!")
            print(f"A PALAVRA ERA: {palavra}")
            break
        elif palavra_comp == palavra:
            print("VOCÊ VENCEU!")
            break
    print("--"*25)
    resp = str(input("DESEJA JOGAR NOVAMENTE? [S/N]")).upper()
    print("--"*25)
    while resp not in "SN":
        print("DADO INVÁLIDO...")
        resp = str(input("DESEJA JOGAR NOVAMENTE? [S/N]")).upper()
    if resp == "N":
        break
print("FIM DO JOGO!")







