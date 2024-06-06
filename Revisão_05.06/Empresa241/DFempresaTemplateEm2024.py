# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:48:24 2020

@author: lcam

Algumas das questoes e possiveis solucoes
Nao sofreu revisao e pode conter erros
Nem todas as questoes do teste foram consideradas

Por Joisa
"""
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows",200)
pd.set_option("display.max_columns",100)

'''
O arquivo cadastroempresas2020.xlsx armazena informações de algumas empresas
nas seguintes planilhas:
    
A planilha dados:
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente
    AreaAtividade: área de atuação da empresa. Por exemplo, uma academia ou 
                   centro esportivo atua na área de ESPORTES
    NumeroDeUnidades: quantidade de filiais da empresa
    QtdDeFuncionarios: número de funcionários considerando todas as filiais	
    SalarioMedio: salário médio dos funcionários, medido em número de 
                  salários mínimos
    AnoDeCriacao: ano de fundação da empresa
    
A planilha desempenho:
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente
    Lucro2017: faturamento líquido no ano de 2017, em mil reais
    Lucro2018: faturamento líquido no ano de 2018, em mil reais       
    Lucro2019: faturamento líquido no ano de 2019, em mil reais 
    
A planilha situação
    NomeEmpresa: nome fantasia da empresa que a identifica unicamente        
    SituacaoFiscal: situação fiscal ( REGULAR ou IRREGULAR) no ano atual
'''

dfDados=pd.read_excel('cadastroempresas2020.xlsx',sheet_name='Dados',index_col=0,header=0)

dfLucro=pd.read_excel('cadastroempresas2020.xlsx',sheet_name='Desempenho',index_col=0,header=0)

dfSit=pd.read_excel('cadastroempresas2020.xlsx',sheet_name='SituacaoFiscal',index_col=0,header=0)



print('\n--------------------dfDados----------------------------')
print(dfDados)
print('\n--------------------dfLucro-----------------------------')
print(dfLucro)
print('\n---------------------dfSit------------------------------')
print(dfSit)
print('\n--------------------------------------------------------')

#======================================================================
print('\n==================================================================')
#Questao1:
# Conhecendo os DataFrames:
print('\nQuestao1:')
#  1A) dfDados: Exiba o percentual de empresas com mais de 20 funcionários e 
#               que tenham até 10 filiais
#  1B) dfLucro: Exiba o percentual de valores ausentes
#  1C) dfSit:   Exiba os 4 últimos elementos ordenados por NomeDaEmpresa'
#  1D) dfDados: Exiba os 8 primeiros elementos ordenados por NumeroDeUnidades/QtdDeFuncionarios 
#  1E) dfLucro: Exiba o percentual de empresas cujo lucro em 2018 foi superior ao lucro de 2019 
#  1F) dfSit:   Exiba a situação das empresas Fominha,KurtExames e VemSerFit

print('\n1A -dfDados: perc de empresas > 20 funcionarios e com ate  10 filiais ')
# acimaDe20 = dfDados[(dfDados['QtdDeFuncionarios'] > 20) & (dfDados['NumeroDeUnidades']<=10)]
# linhas, colunas= dfDados.shape
# print(acimaDe20/linhas)

print('\n1B) dfLucro: Exiba o percentual de valores ausentes ')
print(dfLucro.isna().count())

print('\n1C) dfSit:   Exiba os 4 últimos elementos ordenados por NomeDaEmpresa')
print(dfSit.sort_values(by='NomeEmpresa').tail(4))

print('\n1D) dfDados: os 8 prim ordenados por NumeroDeUnidades/QtdDeFuncionarios ')
print(dfDados.sort_values(by=['NumeroDeUnidades','QtdDeFuncionarios']).head(8))


print('\n1E) dfLucro: percentual de empresas com lucro em 2018 > lucro de 2019  ')


print('\nExtra1: DF com as empresas')
print(dfDados)

print('\nExtra2: So nome das empresas')
print(list(dfDados.index.unique()))

print('\n1F) dfSit:   Exiba a situação das empresas Fominha,KurtExames e VemSerFit')
print(dfSit.loc[['Fominha','KurtExames','VemSerFit']])

#======================================================================
print('\n=========================================================')


#Questao2:
#  Consertando os Dataframes :

# Consertando os Dataframes 
#      dfDados: valores ausentes na coluna NumeroDeUnidades devem ser 
#               substituídos pela média da coluna',
#      dfDados: valores ausentes na coluna SalarioMedio devem ser
#               substituídos pelo menor valor de empresas de mesma área
#               de atividade
#      dfDados: renomeie as colunas para que sejam identificadas por
#               rótulos com até 6 caracteres, todos maiúsculos',


# OBS: o numero de unidades deve ser um inteiro

print('\n*********************************************')
print('******************  Q2  ********************')
print('*********************************************')
media = dfDados.NumeroDeUnidades.mean()
dfDados.fillna({'NumeroDeUnidades':media}, inplace=True)
agrupado = dfDados.groupby(by='AreaAtividade', axis= 0)
print(agrupado.min())
# dfDados.fillna({'SalarioMedio'})

print('\nNovo dfDados')
print(dfDados)
print('\n*********************************************')

#      dfLucro: substitua os valores ausentes de cada empresa pelo lucro 
#               mediano da empresa,
#      dfLucro: inclua a coluna LUCRO com o maior lucro nos 3 anos 
#               de cada empresa


print('\nPreenchidos usando DF transposto')
#MELHOR FORMA: trabalhar com DF transposto




print('\n*********************************************')


print('\n*********************************************')

# Apresente:
#     os novos nomes das colunas de dfDados 
#     os 5 primeiros elementos de dfDados e  
#     um gráfico de linha de cada coluna dos 5 primeiras empresa
#     Usar  dfLucro.T (transposta)'


print('\n2A) Colunas de dfDados')


print('\n2B)5 primeiros elementos de dfDados sem valores ausentes')


print('\n2C) Gráfico de linha com o lucro por ano de cada empresa') 


#======================================================================
print('\n=========================================================')
#Questao3:
# Responda as seguintes perguntas:
  
print('\n3a)Quantas pessoas trabalham em cada área?')



print('\n3b)Qual a soma do LUCRO das empresas com mais de 10 anos de fundação?')
anoAtual = 2022 # dependera do ano corrente


print('\n3c)Qual o ano de fundação das empresas com situação IRREGULAR?')


print('\n3d) Número de filiais mín, máx, mediano e médio por area de ativ/situação?')


print('\n3e)Qual(is) empresa(s) paga(m) pior?')



      
#======================================================================
print('\n=========================================================')

#Questao4:
# Criando categorias:
    
#    dfDados: 
#     - Categorize a existência da empresa levando em consideração 
#       o ano de fundação nas seguintes faixas:
#              0  a  1999 (inclusive) - ANTIGA,
#              a partir de 1999 até 2010 (inclusive) - NORMAL,
#              acima de 2010 - JOVEM,

#    dfLucro: 
#     - Considerendo a coluna LUCRO, categorize a lucratividade das 
#       empresas em 3 faixas de mesma amplitude identificando as faixas 
#       como POUCO,MEDIO,MUITO' 
    
# Mostre as tabelas de frequências resultante do cruzamento de: 
#              existência x lucratividade  
#              área de atividade X existência,lucratividade
# Mostre o salário médio por lucratividade X área de atividade,existência





print('\n4A -Tabela de frequência existência x lucratividade') 


  
print('\n4B -Tabela de frequência área de atividade X existência,lucratividade') 


print('\n4C -Salário médio por lucratividade X área de atividade,existência')  



#======================================================================
print('\n=================FIM  =============================') 

    

    