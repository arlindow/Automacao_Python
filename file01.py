"""
o arquivo SecretPasswordFile.txt é aberto  e a senha secreta
#contida nele é lida. Em seguida, o usuário é solicitado a fornecer uma senha
#(por meio do teclado). Essas duas senhas são comparadas e, se forem
#iguais, o programa exibe Access granted (Acesso concedido).
 
"""
# o arquivo de senha
passwordFile = open('SecretPasswordFile.txt')
# Lê a senha do arquivo e remove espaços em branco ou quebras de linha
secretPassword = passwordFile.read().strip()
# Fecha o arquivo de senha
passwordFile.close()

# Pede ao usuário para inserir a senha
print('Digite sua senha.')
typedPassword = input()

# Verifica se a senha digitada é igual à senha secreta
if typedPassword == secretPassword:
    print('Acesso concedido')
    print(secretPassword)
else:
    print('Acesso negado')
