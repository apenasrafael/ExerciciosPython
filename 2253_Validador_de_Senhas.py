'''
Rolien e Naej são os desenvolvedores de um grande portal de programação. Para ajudar no novo sistema de cadastro 
do site, eles requisitaram a sua ajuda. Seu trabalho é fazer um código que valide as senhas que são cadastradas 
no portal, para isso você deve atentar aos requisitos a seguir:

A senha deve conter, no mínimo, uma letra maiúscula, uma letra minúscula e um número;
A mesma não pode ter nenhum caractere de pontuação, acentuação ou espaço;
Além disso, a senha pode ter de 6 a 32 caracteres.
'''

from string import ascii_uppercase, ascii_letters


while True:
    try:
        senha = input()
        if 6 <= len(senha) <= 32:
            numero, maiuscula, minuscula, senha_invalida = False, False, False, False
            for item in senha:
                if item not in ascii_letters + '0123456789':
                    senha_invalida = True
                    break
                elif item.isdigit():
                    numero = True
                elif item in ascii_uppercase:
                    maiuscula = True
                else:
                    minuscula = True

            print('Senha valida.') if numero and maiuscula and minuscula and not senha_invalida else print('Senha invalida.')

        else:
            print('Senha invalida.')

    except EOFError:
        break
