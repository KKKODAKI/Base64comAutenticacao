import encodeSha
import decode
import encode
import os

escolha = 1

# Resposta 
# 3) Expansão da Mensagem com mais palavras e realizar mais processo de compressão, pois a hash ficaria maior e ela passaria por mais mudanças

while(escolha):
    os.system('cls')

    print('===========================')
    print('1 - Criptografar mensagem')
    print('2 - Validar documento')
    print('0 - Sair')
    print('===========================')

    escolha = int(input('Digite: '))

    if(escolha == 1):
        os.system('cls')
        encoded = input('Escreva uma palavra para ser decodificada: ')
        os.system('cls')

        palavra = decode.decode(encoded)

        print('Palavra original: ' + palavra)
        print('Palavra codificada: ' + encoded + '\n')

     
        encodedPalavra = encodeSha.sha256(palavra, 's')

        f = open('mensagem.txt', 'w', encoding='utf-8')
        f.write(encodedPalavra)
        f.close()
   
        print('criptografada: ' + encodedPalavra)

        print('\n1 - Continuar')
        print('0 - Sair')
        escolha = int(input('Digite: '))

    if escolha == 2:
        os.system('cls')
        encoded = input('Escreva uma palavra para ser decodificada: ')
        os.system('cls')

        palavra = decode.decode(encoded)

        print('Palavra original: ' + palavra)
        print('Palavra codificada: ' + encoded + '\n')
        
        encodedPalavra = encodeSha.sha256(palavra, 's')

        f = open('mensagem.txt', 'r', encoding='utf-8')
        key = f.read()
        f.close()

        if(encodedPalavra == key):
            print('Arquivo original')
        else:
            print('Arquivo alterado!!!')

        print('\n1 - Continuar')
        print('0 - Sair')
        escolha = int(input('Digite: '))
