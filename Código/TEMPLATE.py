# -*- coding: utf-8 -*-

'''1. trabalhoGrupoXXX.docx com:
 SEUS DADOS: nome completo, matrícula, turma
 O Rótulo do seu Grupo e os nomes completos de todos os componentes do
GrupoXXX
 fonte dos dados (endereço completo de onde a base está)
 descrição da base de dados, isto é, o que representam as colunas
 Perguntas a serem respondidas – Todas devem ser numeradas
OBS1: as bases devem ser abertas, ou seja, não podem ser utilizadas bases fechadas, pagas ou
internas de empresas, que não permitam acesso para verificação da base.
OBS2:É terminantemente proibido se basear em provas ou trabalhos de períodos anteriores de
qualquer disciplina de manipulação de dados.


2. templateTrabalhoDoGrupoXXX.py com:
 SEUS DADOS: nome completo, matrícula, turma
 O Rótulo do seu Grupo e os nomes completos de todos os componentes do
GrupoXXX
 Para cada pergunta do docx
print("\n-----------------------------------------------------")
print("\n número e texto da questão: \n")
print("\n-----------------------------------------------------")


3. gabaritoTrabalhoGrupoXXX.py com:
 SEUS DADOS: nome completo, matrícula, turma
 O Rótulo do seu Grupo e os nomes completos de todos os componentes do
GrupoXXX
 Para cada pergunta do docx
print("\n-----------------------------------------------------")
print("\n número e texto da questão: \n")
print( sua resposta para a questão)
print("\n-----------------------------------------------------")


4. Arquivo excel com os dados (colocar o rótulo do grupo no início do nome do arquivo)
As perguntas formuladas por você devem ser elaboradas e, para serem respondidas, devem
fazer uso dos seguintes recursos do pandas vistos em aula (no mínimo):
ATENÇÃO : OS QUESITOS ABAIXO TÊM QUE OBRIGATORIAMENTE SER TODOS UTILIZADOS
PARA RESPONDER ÀS PERGUNTAS ELABORADAS, UMA OU MAIS VEZES, MAS NÃO PRECISAM
APARECER NA ORDEM EM QUE ESTÃO RELACIONADOS

1) Uma concatenação ( em qualquer eixo) (NESSE PERÍODO A CONCATENAÇÃO É
OPCIONAL – único opcional)

2) Duas estratégias distintas de preenchimento de valores ausentes
Por ex: substituir por um valor fixo (0 ou a média) e substituir pelo valor médio de
um agrupamento

3) Uma estratégia para substituição de valores
Por exemplo, df[col].replace ( {1:'UM',2:’DOIS'})

4) A) Criar Categorias em função do valor de uma coluna ( pd.cut) com bins igual à
quantidade de categorias desejadas => inclusão de nova coluna

 4) B) Criar Categorias em função do valor de uma coluna ( pd.cut) com bins igual à
 lista com os extremos de cada faixa => inclusão de nova coluna

5) Três Filtros : um filtro de valor, um filtro de índice, um filtro composto

6) Duas Tabelas de Frequência: uma com valores absolutos sobre uma variável (uma
coluna) e outra com valores percentuais (de alguma outra coluna)

7) Dois gráficos de tipos diferentes

8) Medidas de Sumarização:

a. Geral (total , máximo , mínimo, alguma medida de uma linha ou coluna).
(Também podem ser consideradas aqui interessantes medidas ao longo
do eixo do index ou ao longo do eixo das columns)

b. Grupos simples (agrupar por uma coluna/series/categoria)=> tendo
agrupado por um único agrupador (s.groupby(uma coluna ou uma series
ou uma categoria)) e obtido medidas de interesse

c. Grupos estruturados ( agrupar por mais de uma coluna/series/categoria)
)=> tendo agrupado por mais de um agrupador (s.groupby( [ prim , seg]) e
obtido medidas de interesse


9) Quatro cruzamentos de colunas

a. simples (1 X 1) => crosstab com índice e coluna com só 1 series cada
 - contagem no cruzamento
 - medida de uma outra variável (coluna) no cruzamento

b. estruturados ( nXm) => crosstab com índice e/ou coluna com mais de 1
 series (ao menos um deles)
 - contagem no cruzamento
 - medida de uma outra variável (coluna) no cruzamento '''




############################################################################################
################################     Trabalho do G2   ######################################

#Declaração de autoria: declaro que este documento foi produzido pelo grupo em sua totalidade,
#           sem consultas a outros alunos, professores ou qualquer outra pessoa.
############################################################################################


import pandas as pd
import matplotlib.pyplot as plt

print('\=================================')
print('\n Trabalhando com PANDAS \n')
print('\=================================')
'''
explicação do arquivo.......
.
.
.
'''

"""
**** Questão 1 ****
Modificando o DataFrame criado
    dfDadosYt: Alterar os nomes das colunas do Inglês para o Português:
"""
print('\n==============================================')
print('Questão 1\n')
#======================================================================
# ENUNCIADO
#======================================================================

print('\n==============================================')
print('Questão 2\n')
#======================================================================
# ENUNCIADO
#======================================================================
print('/n------------------------------------------------------')
print('2.a')
print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('2.b')
print('------------------------------------------------------')


print('\n==============================================')
print('Questão 3\n')
#======================================================================
# ENUNCIADO
#======================================================================
print('/n------------------------------------------------------')
print('3-')
print('------------------------------------------------------')




print('\n==============================================')
print('Questão 4\n')
#======================================================================
# ENUNCIADO
#======================================================================
print('/n------------------------------------------------------')
print('4.a')
print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('4.b')
print('------------------------------------------------------')


print('\n==============================================')
print('Questão 5 \n')
#======================================================================
# ENUNCIADO
#======================================================================
print('/n------------------------------------------------------')
print('5.a')
print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('5.b')
print('/n------------------------------------------------------')


print('/n------------------------------------------------------')
print('5.c')
print('------------------------------------------------------')


print('\n==============================================')
print('Questão 6\n')
#======================================================================
# ENUNCIADO
#======================================================================
print('\n------------------------------------------------------')
print('6.a')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('6.b')
print('------------------------------------------------------')


print('\n==============================================')
print('Questão 7\n')
#======================================================================
# ENUNCIADO
#======================================================================
print('\n------------------------------------------------------')
print('7.a')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('7.b')
print('------------------------------------------------------')




print('\n==============================================')
print('Questão 8\n')
#======================================================================
# ENUNCIADO
#======================================================================

print('------------------------------------------------------')
print('8.a')
print('------------------------------------------------------')

print('\n------------------------------------------------------')
print('8.b')
print('------------------------------------------------------')


print('\n------------------------------------------------------')
print('8.c')
print('------------------------------------------------------')



print('\n==============================================')
print('Questão 9\n')
#======================================================================
# ENUNCIADO
#======================================================================
print('------------------------------------------------------')
print('9.a')
print('------------------------------------------------------')

print('/n------------------------------------------------------')
print('9.b')
print('------------------------------------------------------')


print('/n------------------------------------------------------')
print('9.c')
print('------------------------------------------------------')
