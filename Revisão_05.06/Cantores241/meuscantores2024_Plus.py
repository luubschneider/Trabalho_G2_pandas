# -*- coding: utf-8 -*-
"""
Dataframe  - Concurso Meus Cantores
autor: Joisa
"""

import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_rows",100)
pd.set_option("display.max_columns",100)
"""
Os votos dos diferentes candidatos do concurso MiorVoiz estão
armazenados no arquivo votoscantores.xlsx.
Há duas planilhas:
    nacional: com os votos recebidos por cada candidato, por região
    exterior: com os votos recebidos pelos candidatos no exterior
"""
'''
1- Criar o dataframe dfCantores a partir da planilha nacional 
   do arquivo votoscantores.xlsx 

Exibir
'''

print('1-Dataframe dos votos no concurso de cantores')
dfCantores = pd.read_excel('votoscantores.xlsx',sheet_name='nacional',index_col=0,header=0 )

print(dfCantores)


print('\n2- Exibir indices')
dfCantores.index.name='CANTORES'
print(dfCantores.index)



print('\n3 - Exibir colunas:')
dfCantores.columns.name='REGIOES'
print(dfCantores.columns)




print('\n4 - Exibir valores:')

print(dfCantores.values)


print('\n5 - Exibir shape: linhas X colunas :')

print(dfCantores.shape)

print('\n6 -Votos no SONECA:')

print(dfCantores.loc['SONECA'])

print('\n7 -Votos em MILORDE e em KANKAN')

print(dfCantores.loc[['MILORDE','KANKAN' ]])

'''
8 - Criar uma copia dfCop1 com linhas com NaN eliminadas
'''
print( '\n8- Copia sem linhas com NaN')
dfCop1= dfCantores.dropna() #axis=0 ou axis='index'
print(dfCop1)

'''
9- Criar uma copia dfCop2  com colunas com NaN eliminadas
'''
print( '\n9- Copia sem colunas com NaN')
dfCop2= dfCantores.dropna(axis=1)
print(dfCop2)

print('\nDF Original')
print(dfCantores)

'''
10- Substituir NaN por 0
'''
print( '\n10- Trocando NaN por 0')
dfCantores.fillna(0, inplace=True)
#Usando valor específico por coluna
#dfCantores.fillna(value={'NORTE':0,'SUL':1 },inplace=True)
print(dfCantores)


print('\n11-Votos do NORDESTE em NANINHA :')
print(dfCantores.loc['NANINHA','NORDESTE'])
#A forma de acesso  acima é a única q permite tb alterar o valor

print(dfCantores.loc['NANINHA']['NORDESTE']) # aceitavel
print(dfCantores.loc['NANINHA'].loc['NORDESTE'])# mais correto
print(dfCantores['NORDESTE'].loc['NANINHA'])
print(dfCantores.NORDESTE.loc['NANINHA'])

print('\n12-Criando srSudeste so com votos do SUDESTE')
srSudeste = dfCantores['SUDESTE']
print(srSudeste)
print(type(srSudeste))

print('\n13- Exibindo so votos do SUDESTE e do SUL')
print(dfCantores[['SUDESTE','SUL']])


print('\n14-Exibindo o total de votos (por regiao)')
print(dfCantores.sum()) #axis=0 ou axis ='index'

print('\n15-Exibindo o total de votos por CANTOR')
print(dfCantores.sum(axis=1)) #axis='columns'

print('\n15.A- Total de votos no TENORIO' )
print(dfCantores.loc['TENORIO'].sum())

print('\n15.B- Total de votos na regiao NORDESTE')
print(dfCantores['NORDESTE'].sum())


print('\n16- Visualizacao (separada) por Regiao ')
dfCantores.plot.bar(figsize=(4,12),
                    subplots=True,
                    legend=True,
                    color='ybrgm')
plt.show()

print('\n17- Visualizacao por Regiao (Juntas)')
dfCantores.plot.bar(figsize=(8,6),
                    legend=True,
                    color='ybrgm')
plt.show()

print('\n18- Transposta')
dft= dfCantores.T
print(dft)


print('\n19- Quantidade total de votos')
print(dfCantores.sum().sum())


print('\n20-Qual o vencedor do concurso? Quantos votos ele teve?')
srTotPorCantor= dfCantores.sum(axis=1)
print(srTotPorCantor)
print(srTotPorCantor.idxmax(),'-',srTotPorCantor.max())
#print(srTotPorCantor.agg(['idxmax','max']))

print('\n21- Cantores que no SUL tiveram mais votos do que no SUDESTE (DataFrame)')

#print(dfCantores.SUL> dfCantores.SUDESTE)

DFmaisNoSul= dfCantores.loc[ dfCantores.SUL> dfCantores.SUDESTE]
print(DFmaisNoSul)


print('\n22- Cantores (DataFrame) que tiveram mais do que 10000 votos no total' )


# print(srTotPorCantor>10000)
dfMaisQue10 = dfCantores.loc[ srTotPorCantor>10000 ]
print(dfMaisQue10)

"""
INCLUSÃO DE NOVOS ELEMENTOS
"""
'''
Acrescentando o queridinho eliminado que retornou com 100 votos por região --> linha
'''
print('\n23- Incluindo a linha "QUERIDINHO"' )
dfCantores.loc['QUERIDINHO']=100
print(dfCantores)


'''
Acrescentando os votos do EXTERIOR --> coluna
'''
print('\n24- Incluindo a coluna EXTERIOR' )
srExt=pd.read_excel('votoscantores.xlsx',sheet_name='exterior',index_col=0,
                    header=0).squeeze().copy()
print(srExt)


dfCantores['EXTERIOR']=srExt
print(dfCantores)

'''
Alteração de célula
Como o QUERIDINHO não recebeu votos do exterior, atualizar este valor para 0
'''
print('\n25- Alteração da célula na linha "QUERIDINHO", coluna "EXTERIOR"' )
dfCantores.loc['QUERIDINHO','EXTERIOR']=0
print(dfCantores)

#COMPLEMENTOS NA AULA 2 de DataFrame

# ORDENACAO
print('\n26A- Ordenado pelos cantores')
# sort_index() default => pelos rótulos dos índices
print(dfCantores.sort_index())

# sort_index() => pelos rótulos das colunas
print('\n26B- Ordenado pelas regioes')
print(dfCantores.sort_index(axis='columns'))

# ORDENACAO POR VALORES
print('\n27-Ordenado pelos valores da coluna SUDESTE')
print(dfCantores.sort_values(by='SUDESTE',ascending=False))


#Apenas para exemplificar
print('\nDF alterado para exemplo de ordenação')
dfCantores.loc[['BISCOITO','KANKAN'], 'SUDESTE']=1000
print(dfCantores)
print('\n27A-Ordenado pelos valores da coluna SUDESTE, secundario NORDESTE')
print(dfCantores.sort_values(by=['SUDESTE','NORDESTE'],
                             ascending=False))

print('\n28- Estrutura do DF ou INFORMACOES sobre o DF')
dfCantores.info()

#Series com estilo da musica do cantor

lestilo=['country','pop','samba','rock','sertanejo',
         'country','pop','samba','samba','rock',
         'rock','sertanejo']

srEstiloDosCantores= pd.Series(lestilo, index= dfCantores.index)
print('\n29 Series com estilos de música')
print(srEstiloDosCantores)

print('\nTotal de votos por ESTILO de música')

srTotalVotosPorCantor= dfCantores.sum(axis=1)
#Agrupando por uma series (pode ou não ser uma coluna)
agEstilo= srTotalVotosPorCantor.groupby(by=srEstiloDosCantores)
print(agEstilo.sum())




