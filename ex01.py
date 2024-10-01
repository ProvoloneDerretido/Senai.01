
usuarios = int(input("Digite o numero de usuarios a ser cadastrados:"))
Nusuarios = 0
Nnome = [None] * usuarios
Nidade = [None] * usuarios
def Menu():
   
 print('1- Cadastrar novo usuario: ')
 print('2- Listar todos os usuarios cadstrados: ')
 print('3- Sair: ')
 
while True:
 Menu()
 Selecionar = int(input('Digite uma opçao:'))
 
 if Selecionar == 1 :
    if usuarios > Nusuarios:
     nome = input('Digite o nome do usuario:')
     idade = input('Digite a idade do usuario:')
     Nnome[Nusuarios] = nome
     Nidade[Nusuarios] = idade
     Nusuarios += 1
     print('Usuario Cadastrado!')

    else :
     print('Limite de usuarios atingidos')
   
 elif Selecionar == 2:
   if Nusuarios == 0:
     print('Nenhum usuario cadastrado!')
   else:
     for i in range(Nusuarios):
       print(f"Usuario: {Nnome[i]}, {Nidade[i]}")
       
     
 elif Selecionar == 3:
     print('E isso.')
     break

 else: 
     print('Selecione uma opçao existente!')
    

