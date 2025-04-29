def decode(encoded):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    letras_encoded = []
    letras_bin = ''
    nova_letra = ''
    palavra = ''
    
    # Bom, pelo q eu percebi, o igual é pra encher linguiça
    # Então aqui eu removo os iguais
    igual = encoded.count('=')
    if(igual == 1):
        encoded = encoded[:-1]
    elif(igual == 2):
        encoded = encoded[:-2]

    # Nesse for eu tranformo as letras em binarios com base na tabela de base64
    for i in range(len(encoded)):
        letras_encoded = bin(base64_chars.find(encoded[i]))
        # Aqui eu removo o "0b" do começo do binario, para ficar só os números
        letras_encoded = letras_encoded[2:]

        # Aqui eu deixo todos os binarios com 6 caracteres
        # Caso tenha menos de 6, adiciono zeros à esquerda
        while(len(letras_encoded) != 6):
            letras_encoded = '0' + letras_encoded

        # Passo todos os binarios para uma só string
        letras_bin = letras_bin + letras_encoded
    # Inicializo a variavel i=1 para usar na lógica mais abaixo
    i=1

    # Aqui nesse for eu vou pegar a variavel que tem todos o binários das letras e separa-los em 8 caracteres
    for j in range(len(letras_bin)):
        nova_letra = nova_letra + letras_bin[j]

        # Sempre que i passa pelo for eu adiciono +1, quando i=8 ele entra dentro do if a variavel nova_letra está com 8 caracteres
        if(i == 8):
            
            # Aqui eu pego o binário de 8 caracteres e transformo ele em um int
            # E com esse int ele pega a letra com base na tabela ascii
            # Todas as letras são "somadas" para formar a palavra
            palavra = palavra + chr(int(int(nova_letra,2)))
        
            # i=0 e nova_letra = '' para começar de novo o processo de criar uma nova_letra com 8 caracteres
            i = 0
            nova_letra = ''

        i = i + 1

    return palavra