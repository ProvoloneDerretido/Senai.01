usuarios = int(input("Digite o numero de usuarios a ser cadastrados:"))
Nusuarios = 0
Nnome = [None] * usuarios
Nidade = [None] * usuarios
def Menu():
   
 print('\n1- Cadastrar novo usuario: ')
 print('2- Listar todos os usuarios cadastrados: ')
 print('3- Sair: ')
 print('4- Buscar usuario pelo nome')
 print('5- Remover usuario')
 
while True:
 Menu()
 Selecionar = int(input('\nDigite uma opçao:'))
 
 if Selecionar == 1 :

    if usuarios > Nusuarios:
     nome = input('\nDigite o nome do usuario:')
     idade = int(input('Digite a idade do usuario:'))
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
       print(f"\nUsuario: {Nnome[i]}, {Nidade[i]}")   
 elif Selecionar == 3:
     print('E isso.')
     break
 
 elif Selecionar == 4:
    Buscar = input('\nDigite o nome do usuario que deseja buscar: ')
    if Buscar in Nnome:
        NBuscar = Nnome.index(Buscar)
        print(f'Usuario encontrado: Nome: {Nnome[NBuscar]}, Idade: {Nidade[NBuscar]}')
    else:
        print('Usuario não encontrado!')

 elif Selecionar == 5:
    Remover = input('\nDigite o nome do usuario a ser removido: ')
    if Remover in Nnome:
        NRemover = Nnome.index(Remover)
        del Nnome[NRemover] 
        del Nidade[NRemover] 
        Nusuarios -= 1 
        print(f'Usuario {Remover} removido')
    else:
        print(f'Usuario {Remover} nao encontrado')
        
 else: 
     print('Selecione uma opçao existente!')