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
dfDados = pd.DataFrame(dfDados)
dfLucro=pd.read_excel('cadastroempresas2020.xlsx',sheet_name='Desempenho',index_col=0,header=0)
dfLucro = pd.DataFrame(dfLucro)
dfSit=pd.read_excel('cadastroempresas2020.xlsx',sheet_name='SituacaoFiscal',index_col=0,header=0)
dfSit = pd.DataFrame(dfSit)


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
sboolMa20funAte10fil= (dfDados.QtdDeFuncionarios>20)&(dfDados.NumeroDeUnidades<=10)
print(sboolMa20funAte10fil.sum()/sboolMa20funAte10fil.size*100)

#Alternativa
dfEmpDoCriterio= dfDados.loc[(dfDados.QtdDeFuncionarios>20)&(dfDados.NumeroDeUnidades<=10)]
print(dfEmpDoCriterio.shape[0]/dfDados.shape[0]*100)


print('\n1B) dfLucro: Exiba o percentual de valores ausentes ')
totVal= dfLucro.size
totValAusentes = dfLucro.isnull().sum().sum()
print(totValAusentes/totVal *100)

print('\n1C) dfSit:   Exiba os 4 últimos elementos ordenados por NomeDaEmpresa')
print(dfSit.tail(4).sort_index())
#print(dfSit.sort_index().tail(4)) #NAO A MAIS PROVAVEL

print('\n1D) dfDados: os 8 prim ordenados por NumeroDeUnidades/QtdDeFuncionarios ')
print(dfDados.head(8).sort_values(['NumeroDeUnidades','QtdDeFuncionarios']))
#print(dfDados.sort_values(['NumeroDeUnidades','QtdDeFuncionarios']).head(8))

print('\n1E) dfLucro: percentual de empresas com lucro em 2018 > lucro de 2019  ')
sBoolLucroMaior = dfLucro.LUCRO2018> dfLucro.LUCRO2019
print(sBoolLucroMaior.sum()/sBoolLucroMaior.size*100)

print('\nExtra1: DF com as empresas')
dfE= dfLucro.loc[sBoolLucroMaior]
print(dfE)

print('\nExtra2: So nome das empresas')
dfE= dfLucro.loc[sBoolLucroMaior]
print(list(dfE.index))


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
dfDados.fillna(value={'NumeroDeUnidades':int(dfDados.NumeroDeUnidades.mean())},
               inplace=True)

# OU
#mediaNumUnid= int( dfDados.NumeroDeUnidades.mean())
#dfDados.NumeroDeUnidades.fillna(mediaNumUnid,inplace=True)
              
agArea = dfDados.groupby('AreaAtividade') 

# Usando apply e funcao
# def ffsub(srg):
#     srg.fillna(srg.min(),inplace=True)   #OBS: aqui eh para usar min e nao mean
#     return srg

# dfDados.SalarioMedio = agArea['SalarioMedio'].apply(ffsub) 
# print(dfDados)

dfDados.fillna(value={'SalarioMedio': agArea['SalarioMedio'].transform(min) },
               inplace=True)


dfDados.rename(columns={'AreaAtividade':'ARATIV','NumeroDeUnidades':'NUMUNI',
                        'QtdDeFuncionarios':'QTDFUN','SalarioMedio':'SALMED',
                        'AnoDeCriacao':'ANOCRI'},
               inplace=True)
print('\n*********************************************')
print('******************  Q2  ********************')
print('*********************************************')
print('\nNovo dfDados')
print(dfDados)
print('\n*********************************************')

#      dfLucro: substitua os valores ausentes de cada empresa pelo lucro 
#               mediano da empresa,
#      dfLucro: inclua a coluna LUCRO com o maior lucro nos 3 anos 
#               de cada empresa


print('\nPreenchidos usando DF transposto')
#MELHOR FORMA: trabalhar com DF transposto
dfLucro.T.fillna(dfLucro.median(axis=1),inplace=True)
print(dfLucro)


#ALTERNATIVA: funcao atuando no eixo columns
def preenchePorLinha(emp):   # funcao deve atuar no eixo columns
    lucMedianoDaEmp = emp.median()
    emp.fillna(lucMedianoDaEmp,inplace=True)
    return emp
#dfLucro.apply(preenchePorLinha, axis=1)
print('\n*********************************************')

dfLucro['LUCRO'] = dfLucro.max(axis=1)
print('\nNovo dfLucro')
print(dfLucro)
print('\n*********************************************')

# Apresente:
#     os novos nomes das colunas de dfDados 
#     os 5 primeiros elementos de dfDados e  
#     um gráfico de linha de cada coluna dos 5 primeiras empresa
#     Usar  dfLucro.T (transposta)'


print('\n2A) Colunas de dfDados')
print(list(dfDados.columns))

print('\n2B)5 primeiros elementos de dfDados sem valores ausentes')
print(dfDados.head(5))

print('\n2C) Gráfico de linha com o lucro por ano de cada empresa') 
dfLucro.head(5).T.drop('LUCRO').plot.line()
plt.show()

dfL= dfLucro.drop('LUCRO', axis=1 )
dfL.head(5).T.plot.line(figsize=(8,6))
plt.show()

#======================================================================
print('\n=========================================================')
#Questao3:
# Responda as seguintes perguntas:
dfGeral= pd.concat([dfDados,dfLucro, dfSit],axis=1,join='inner') 
print(dfGeral)    
print('\n3a)Quantas pessoas trabalham em cada área?')
print(dfGeral.groupby('ARATIV')['QTDFUN'].sum())


print('\n3b)Qual a soma do LUCRO das empresas com mais de 10 anos de fundação?')
anoAtual = 2021 # dependera do ano corrente
print(dfGeral.loc[dfGeral.ANOCRI< anoAtual-10].LUCRO.sum())

print('\n3c)Qual o ano de fundação das empresas com situação IRREGULAR?')
print(dfGeral.loc[dfGeral.SITFISC=='IRREGULAR'].ANOCRI)

print('\n3d) Número de filiais mín, máx, mediano e médio por area de ativ/situação?')
agAtivSit = dfGeral.groupby(['ARATIV','SITFISC'])
print(agAtivSit['NUMUNI'].agg(['min','max','median','mean']))

print('\n3e)Qual(is) empresa(s) paga(m) pior?')
piorSal = dfGeral.SALMED.min()
srPiores = dfGeral.SALMED.loc[dfGeral.SALMED==piorSal]
print(list(srPiores.index))

#dfPiores = dfGeral.loc[dfGeral.SALMED==piorSal]
#print(list(dfPiores.index))
      
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


srCatExistencia = pd.cut(dfDados.ANOCRI,bins=[0,1999,2010,dfDados.ANOCRI.max()],
                         labels=['ANTIGA','NORMAL','JOVEM'])
srCatExistencia.name= 'CatExistencia'

srCatLucratividade = pd.cut(dfLucro.LUCRO, bins=3,
                            labels=['POUCO','MEDIO','MUITO'])

srCatLucratividade.name= 'CatLucratividade'


print('\n4A -Tabela de frequência existência x lucratividade') 

print(pd.crosstab(index= srCatExistencia, columns=srCatLucratividade))
  
print('\n4B -Tabela de frequência área de atividade X existência,lucratividade') 

print(pd.crosstab(index= dfDados.ARATIV , columns=[srCatExistencia,srCatLucratividade]))

print('\n4C -Salário médio por lucratividade X área de atividade,existência')  
print(pd.crosstab(index= srCatLucratividade  , columns=[dfDados.ARATIV,srCatExistencia],
                  values= dfDados.SALMED, aggfunc='mean'))

print('\nOutra forma: não minha preferida')
aggg=dfDados.groupby([dfDados.ARATIV,srCatExistencia,srCatLucratividade])
print(aggg.SALMED.mean())
#======================================================================
