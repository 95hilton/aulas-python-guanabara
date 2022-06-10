import menu


def atualizaPessoa():

      # Solicita ao usuário que digite o nome de quem deseja alterar a idade
      while True:
        try:
           nome = str(input('Digite o nome da pessoa que deseja atualizar a idade, ou digite SAIR para ir para o menu inicial: ')).upper().strip()
           if nome == 'SAIR':
              menu.menuPrincipal()
              break
           elif nome == '':
              print('Digite um nome válido!')
           # else:
           #     break
        except KeyboardInterrupt:
            print('Digitação interrompida pelo usuário.')

        else:
            try:
              #Lista pessoas de acordo com o nome digitado anteiormente
              arquivo = open('cadastro.txt', 'r+')
              lista = arquivo.readlines()
              # antigo = ''
              for l in lista:
                  if nome not in l:
                      print(f'Não foi possível localizar o nome {nome}. Tente novamente mais tarde')
                      menu.menuPrincipal()
                      break
                  else:
                     antigo = l
                     arquivo.close()
                     break
            except Exception as e:
               print(f'Não foi possível localizar o nome {nome}. Erro {e.__class__}')
               print('Tente novamente.')
            else:
         #Solicita nova idade
              try:
                 while True:
                     idade = int(input(f'Digite a nova idade para {nome}: '))
                     if idade == '':
                         print('Digite uma idade válida.')
                     else:
                        break
              except KeyboardInterrupt:
                     print('Digitação interrompida pelo usuário.')
              except (ValueError, TypeError):
                     print('Digite uma idade válida.')
              else:
               # Faz a substituição da idade da pessoa
                  try:
                     arquivo = open('cadastro.txt', 'r+')
                     lista = arquivo.read()
                     lista = lista.replace(antigo, f'{nome}\t\t\t{idade} anos\n')
                     arquivo.close()
                  except FileNotFoundError:
                     print('Não existem pessoas cadastradas!')
                  else:
                     # Reescreve o arquivo de texto com a lista atualizada
                     try:
                        arquivo = open('cadastro.txt', 'w+')
                        arquivo.write(lista)
                        arquivo.close()
                     except FileNotFoundError:
                        print('Não existem pessoas cadastradas!')
                     else:
                        print('Atualizado com sucesso.')
                        menu.menuPrincipal()
                        break

