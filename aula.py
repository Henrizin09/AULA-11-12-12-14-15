# ACESSAMOS UM ARQUIVO TXT E  EFETUAMOS A LEITURA DAS
# import os


# with open("teste.txt", "r") as arquivo:
#  content = arquivo.read()
# print(content)


# with open("C:/Users/aluno/aula13", "w") as diretorio:
#     os.mkdir("novo_arquivo")



# **Exercício 1: Criar e ler um Arquivo**
import os 
import shutil


 with open('arquivo.txt', 'w') as arquivo:
      c =  arquivo.write()
      print('feito')
     



# **Exemplo 2: Entrar em um Diretório**


 with open('C:/Users/aluno/aula11/arquivo.txt', 'r') as arquivo:
      c1 =  arquivo.read()
      print(c1)


 with os.scandir('C:/Users/aluno/aula11/teste1') as teste:
     for n in teste:
         if n.is_file():
             print(n)



# **Exercício 3: Renomear um Diretório**

 os.rename('teste1', 'test3')

# **Exercício 4: Remover um Diretório**

 shutil.rmtree('C:/Users/aluno/aula11/test3')

#  **Exercício 5: Listar Arquivos em um Diretório** 
 with os.scandir('C:/Users/aluno/aula11/teste2') as teste:
     for n in teste:
         if n.is_file():
             print(n)

# **Exercício 6: Copiar Arquivos em um Diretório**
            
shutil.copy('teste2/teste2.txt','teste5.txt')            










# # ACESSAMOS UM ARQUIVO TXT E EFETUAMOS A LEITURA DAS INFOS
# import os
# import shutil


# # with open('teste.txt', 'r') as arquivo:
# #     content =  arquivo.read()
# #     print(content)

# # criação de Pastas 
# # with open('aula12', 'w') as arquivo:
#     #  content = arquivo.read()

# # os.mkdir('novo')
# # os.rename('C:/Users/aluno/aula11/aula16', 'aula17')



# # with os.scandir('C:/Users/aluno/aula11/') as arquivo:
# #      for n in arquivo: 
# #           print(n) 

# # with os.scandir('C:/Users/aluno/aula11/') as entrada:
# #      for arquivo in entrada: 
# #           if arquivo.is_file():
# #              print(arquivo.name) 


# # shutil.rmtree('C:/Users/aluno/aula11/')

# shutil.copytree('teste1', 'teste2')

        





