# -*- coding: utf-8 -*-
"""
Created on 2021/1

@author: JOISA

Criacao de DF (dataframe) a partir de dic de dic

index/columns/values/shape/size

selecao de linha/coluna/elemento

medida (pelos diferentes eixos)

DF transposto

Inclusao de colunas e de linhas,

Uso de funcoes:
    - no eixo index (axis=0/default) => "geraria uma nova linha"
    - no eixo columns (axis=1)  => "geraria uma nova coluna"
    
Ordenacao

Preenchimento de valores ausentes

Concatenacao de DataFrames

Renomeando colunas

Filtro (selecao usando filtros simples/compostos)
"""

import pandas as pd
import matplotlib.pyplot as plt

dicGraus={ 'Grau1': {'LALA':5.5,'LELE':2.4,'LILI':3.7,'DUDU':7.9},
           'Grau2': {'LALA':9.5,'LELE':6.5,'LILI':6.4,'DUDU':9.1}
        }

print('\n-------AULA1---------')
dfGraus= pd.DataFrame(dicGraus)

print('\n----------1----------')
print(dfGraus)

print('\n----------2----------')
print(dfGraus.index)
print('\n----------3----------')
print(dfGraus.columns)
print('\n----------4----------')
print(dfGraus.values)
print('\n----------5----------')
print(dfGraus.size)
print('\n----------6----------')
print(dfGraus.shape)
print('\n----------7----------')
print(dfGraus.shape[0])
print('\n----------8----------')
print(dfGraus.shape[1])
print('\n----------9----------')
print(dfGraus.head(2))
print('\n----------10---------')
print(dfGraus.tail(2))
print('\n----------11---------')
dfGraus.info() #ja exibe na tela
print('\n----------12---------')
print(dfGraus.describe())

######### Medidas (funcoes) e eixos #########
print('\n----------13---------')
print('\nMedia dos GRAUS') # => default: axis=0 ou axis='index'
print(dfGraus.mean())
print('\n----------14---------')
print('\nMedia dos ALUNOS') # =>  axis=1 ou axis='columns'
print(dfGraus.mean(axis=1))

######### Selecao de Elementos #########
print('\n----------15---------')
print(dfGraus.loc['LELE']) # retorna uma series
print('\n')
print(dfGraus.loc[['LELE']]) # retorna um DF
print('\n')
print(dfGraus.loc[['LELE','DUDU']]) # retorna um DF

print('\n----------16---------')
print(dfGraus['Grau1'])#  retorna series
print('\n')
print(dfGraus.Grau1) # pode usar dfGraus.Grau1: retorna series
print('\n')    
print(dfGraus[['Grau2','Grau1']])    # retorna DF

print('\n----------17---------')
print(dfGraus.loc['LELE','Grau1']) #Elemento (celula). Tambem para alteracao

print('\n----------18---------')
print(dfGraus.loc['LELE']['Grau1']) #CORRETO: dfGraus.loc['LELE'].loc['Grau1']

print('\n----------19---------')
print(dfGraus)

print('\n----------20---------')
print(dfGraus.T)
print(dfGraus.T.index)
print(dfGraus.T.columns)
dfGraus.T.loc['Grau1','LELE']=10   #Alteracao do valor de uma celula

print('\n----------21---------')
print(dfGraus.T)

print('\n----------22---------')
print(dfGraus)

###############  VISUALIZACAO ###############
print('\n---------23----------')
#VISUALIZACAO: Barras => Todos os Graus juntos em um grafico unico
dfGraus.plot.bar(title='GRAUS JUNTOS', figsize=(6,4))
plt.show()

#VISUALIZACAO: Barras => Graus Separados
dfGraus.plot.bar(title='GRAUS SEPARADOS', subplots=True, figsize=(6,6))
plt.show()

###############  INCLUSOES ###############
print('\n---------24----------')
#INCLUSAO DE NOVA LINHA
srVava=pd.Series([9.4, 7.8], index=['Grau1','Grau2'])
#print(srVava)
#Incluindo uma linha correspondente ao Vava
dfGraus.loc['VAVA']= srVava # poderia usar diretamente [9.4, 7.8]
print(dfGraus)

dfGraus.loc['KUKA']=0
print(dfGraus)

dfGraus.loc['TETE']=[3.6,9]
print(dfGraus)

print('\n---------25----------')
#INCLUSAO DE NOVA COLUNA
dicGrau3= {'LALA':9.5,'LELE':5.5,'LILI':6.2,'VAVA':8.2,'DUDU':2.7}
#Inclusao da coluna Grau3=
dfGraus['Grau3']=pd.Series(dicGrau3) 
print(dfGraus)


############## Descartando NaN #############
print('\nCopia com linhas com NaN descartadas')
dSemLinhasNaN= dfGraus.dropna(axis=0)   # axis='index'
print(dSemLinhasNaN)

print('\nCopia com colunas com NaN descartadas')
dSemColunasNaN= dfGraus.dropna(axis=1)   # axis='columns'
print(dSemColunasNaN)

print('\nDescarte da linhas com NaN no proprio')
dfGraus.dropna(axis=0, inplace=True)
print(dfGraus)

###############  Aplicacao de FUNCAO  ###############

#Maior nota
print('\nMaior Nota (de cada Grau)')
print(dfGraus.max(axis=0)) #default => 'index'

print('\n')
print('\nUm Aluno com Maior Nota  (de cada Grau)')
print(dfGraus.idxmax(axis=0))

print('\nMaior nota e Um Aluno com Maior Nota')
print(dfGraus.agg(['max','idxmax'] , axis=0  ))

print('\nMaior Nota (de cada aluno)')
print(dfGraus.max(axis=1)) # axis ='columns'

print('\nUm Grau de Maior Nota (de cada aluno)')
print(dfGraus.idxmax(axis=1))

print('\nMaior nota e Um Grau de Maior Nota (de cada aluno)')
print(dfGraus.agg( ['max','idxmax'] ,axis=1 ))


print('\n')

print('\n---------26----------') ###PLUS!!!

#APLICACAO DE FUNCAO SOBRE  DF
#Quantidade de notas acima de 7
def qtdAcimaDe7(srLinOuCol):
    srBoolAcima7 = srLinOuCol>7  # resulta em series de True(vale 1)/False(vale 0)
    # se quisermos a quantidade total na linha ou coluna, somar booleanos=>total de True
    return srBoolAcima7.sum()



#APLICACAO DE FUNCAO NO EIXO DOS INDICES (a funcao atua col a col=>gera nova linha ao final)
print("\nQuant de Notas acima de 7 por GRAU")
print(dfGraus.apply(qtdAcimaDe7, axis=0 ))

#APLICACAO DE FUNCAO NO EIXO DAS COLUNAS (a funcao atua linha a linha=> gera nova coluna ao final)
print("\nQuant de Notas acima de 7 por Aluno")
print(dfGraus.apply(qtdAcimaDe7, axis=1 ))


###############  ORDENACAO  ###############
print('\n---------27----------')
#Um segundo DataFrame
dicOutros= {'NENE':{ 'Grau1':7.6, 'Grau3':2.8},
            'BUBA':{'Grau2':5.0},
            'GIGI':{'Grau1':5.4,'Grau2':8.6 },
            'TATA':{ 'Grau1':5.4, 'Grau2':7.8, 'Grau3':8.1}}
dfOutro= pd.DataFrame(dicOutros)
print(dfOutro,'\n')
dfOutro= dfOutro.T
print(dfOutro,'\n')

#Exibindo ordenado por ALUNO (index)
print('\nExibindo ordenado por ALUNO (index)  ')
print(dfOutro.sort_index())

#E se quiser deixar ordenado?
print('\n')
dfOutro.sort_index(inplace=True)
print(dfOutro)

#Exibindo ordenado pelos ROTULOS das colunas
print('\nExibindo ordenado pelos ROTULOS das colunas  ')
print(dfOutro.sort_index(axis=1))

#exibe uma copia ordenada
#E se quiser deixar ordenado?
dfOutro.sort_index(axis=1, inplace=True)
print(dfOutro)

#Exibindo ordenado pelos valores do Grau1
print('\nExibindo ordenado pelos valores do Grau1  ')
print(dfOutro.sort_values(by='Grau1'))

#Exibindo ordenado pelos valores do [Grau1,Grau2]
print('\nExibindo ordenado pelos valores do [Grau1,Grau2]  ')
print(dfOutro.sort_values(by=['Grau1','Grau2'] ))



###########  Preenchimento de Valores Ausentes ###########
# Obs: Ha´ outras formas

print('\n---------28----------')
#PREENCHIMENTO DE VALORES AUSENTES => COPIAS
#Copia1: Preenchendo todos os NaN por 1
print(dfOutro.fillna(1))
print('\n')
#Copia2: Preenchendo NaN pela media das colunas (dos graus)=>eixo index
srMediasGraus= dfOutro.mean()
print(dfOutro.fillna(srMediasGraus))
print('\n')

#Copia3: Preenchendo NaN pela media das linhas (notas de cada aluno)=>eixo columns
# ATENCAO: nao implementado. Assim so trabalhando com o DF Transposto


#Copia4: Preenchendo NaN =>Grau1: 0, Grau2: media do Grau2, Grau3:mediana do Grau3
print(dfOutro.fillna( value= {'Grau1':0,
                              'Grau2':dfOutro['Grau2'].mean(),
                              'Grau3':dfOutro['Grau3'].median()}))


########### CONCATENACAO #############
print('\n---------29----------')
#JUNTANDO DataFrames => concatenacao: default axis=0 e join = 'outer'
#dfOutro com NaN
print('\n----------------')
print(dfGraus)
print('\n----------------')
print(dfOutro)
print('\n----------------')
dfJuntos1= pd.concat([dfGraus, dfOutro])
print(dfJuntos1,'\n')


dic3={ 'EXTRA1': {'LELE':8.4, 'VAVA':8.8, 'DUDU': 8.9, 'MIMI':8.6},
        'EXTRA2': {'LELE':6.4, 'VAVA':7.8, 'DUDU': 6.9, 'MIMI':7.6}
      }

df3= pd.DataFrame(dic3)
print(df3,'\n')

#Outras concatenacoes: a default nao eh interessante

#print(pd.concat([dfGraus,df3 ])) #RUIM

print('\n****')
# axis=1, considerando TODOS os elementos join='outer' (join default)
dfJuntos3= pd.concat([dfGraus,df3 ], axis=1,join = 'outer')
print(dfJuntos3)
print('\n')
# axis=1, considerando somente os que tem todas as colunas join='inner' (intersecao)

dfJuntos3= pd.concat([dfGraus,df3 ], axis=1,join = 'inner')
print(dfJuntos3)
print('\n---------30----------')
#Renomeando Colunas (já feito em outro exemplo)



############################################################
# Vamos prosseguir apenas com  dfGraus
# Alteraremos o dfGraus para ter resultados interessantes
############################################################

print('\nSeguindo com dfGraus: ')
print(dfGraus)

print('\ndfGraus: alterando elementos p resultados interessantes')
# alterar o grau3 da LALA para 9.8
# alterar o grau2 da DUDU para 5.8
dfGraus.loc['LALA','Grau3']=9.8
dfGraus.loc['DUDU','Grau2']=5.8
print(dfGraus)
########### FILTRO #############
print('\n---------31----------')
print('\nDf Alunos com nota de Grau1 >= 6')

print('\ndfGraus.Grau1>=6 ??')
print(dfGraus.Grau1>=6)

print('\nDf resposta:')
dfG1ac6= dfGraus.loc[dfGraus.Grau1>=6]
print(dfG1ac6)


print('\nDF Alunos com nota de Grau1 < Grau2')
print(dfGraus.loc[dfGraus['Grau1'] < dfGraus['Grau2']])
print(dfGraus.loc[dfGraus.Grau1 < dfGraus.Grau2])


print('\nDF Alunos com nota de Grau1 e de Grau2 >=6')
print(dfGraus.loc[ (dfGraus.Grau1>=6) & (dfGraus.Grau2>=6)])


print('\nDF Alunos em dfGraus que tambem estao em df3')
print('\ndfGraus')
print(dfGraus)
print('\ndf3')
print(df3)
print('\nDf resposta')
print(dfGraus.loc[dfGraus.index.isin(df3.index)])
# # dfGraus.loc[df3.index] da erro por causa de MIMI q nao esta em dfGraus
# #Usar filtro de indice



########### Op Aritm #############

print('\n---------32----------')
# Na verdade esta operando com series
print('\n Media ponderada')
srMedia= (2*dfGraus.Grau1+ 3*dfGraus.Grau2+5*dfGraus.Grau3)/10
print(srMedia)
########### Mais inclusao de coluna  #############
print('\n---------33 A----------')
# Inclusao de coluna com a media

# dfGraus['Med'] = srMedia
# print(dfGraus)

#Pode fazer diretamente
dfGraus['Media']=(2*dfGraus.Grau1+ 3*dfGraus.Grau2+5*dfGraus.Grau3)/10
print(dfGraus)

# print('\n---------33 B----------')

# Inclusao de coluna por funcao aplicada POR linha (ao longo do eixo das colunas)

#Incluir uma coluna com a avaliacao do desempenho do aluno ao longo 
# curso, a partir dos graus, informando se MELHOROU,PIOROU ou 
# INDETERMINADO. 

def avalDesempenho(laluno):
    if (laluno.Grau1 < laluno.Grau2) & (laluno.Grau2 < laluno.Grau3):
        return 'MELHOROU'
    if (laluno.Grau1 > laluno.Grau2) & (laluno.Grau2 > laluno.Grau3):
        return 'PIOROU'
    return 'INDETERMINADO'
    

#srDesempenho= dfGraus.apply(avalDesempenho,axis=1)
#print(srDesempenho)
dfGraus['DESEMPENHO']= dfGraus.apply(avalDesempenho,axis=1)
print('\n')
print(dfGraus)

print('\nMostre graficamente a tabela de freq do desempenho')
dfGraus.DESEMPENHO.value_counts().plot.pie(title='Desempenho',
                                           figsize=[5,5],
                                           autopct='%.1f')
plt.show()




