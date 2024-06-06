# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:30:55 2018
autor: JOISA

TESTE1: CELULAR

POSSIVEL SOLUCAO
Pode conter erros: nao sofreu revisao
"""

'''
No arquivo CelularNoBoaCompra.xlsx ha´ 3 planilhas com dados sobre um mesmo grupo de celulares.
Na planilha caracteristicas estao caracteristicas dos aparelhos.
Na planilha precos estao os precos dos aparelhos em alguns sites.
Na planilha avaliacao estao as notas dadas pelos usuarios aos aparelhos 
nos quesitos tela, camera e desempenho.
'''

import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_rows",None)
pd.set_option("display.max_columns",None)

'''
1- Crie o dataframe dfCaracCel a partir da planilha caracteristicas do arquivo 
CelularGeral.xlsx, considerando o nome do celular como indice. A primeira linha do arquivo 
contem o nome das colunas
'''
print('\n1-O dfCaracCel')
dfCaracCel= pd.read_excel('CelularGeral.xlsx',sheet_name='caracteristicas', index_col=0,
                         header=0)
print(dfCaracCel)

print('\n2-Exiba as informacoes do dfCaracCel')
dfCaracCel.info()

print('\n3-Exiba a coluna fabricante')
print(dfCaracCel.fabricante)

print('\n4.A-Renomeie as colunas sistema operacional(SO) e tamanho tela (tela). Exiba')
dfCaracCel.rename(columns={"sistema operacional":"SO","tamanho tela":"tela" },inplace=True)
print(dfCaracCel)

print('\n4.B-Renomeie as colunas bateria ligado (bateria) e bateria repouso (autonomia). Exiba')
dfCaracCel.rename(columns={"bateria ligado":"bateria","bateria repouso":"autonomia" },inplace=True)
print(dfCaracCel)

print('\n5-Crie e exiba um DF (dfCel1) so com as colunas tela,SO,fabricante')
colunasEscolhidas=['tela','SO','fabricante']
dfCel1=dfCaracCel[colunasEscolhidas]
print(dfCel1,'\n')
# dfCel1.loc['SSS2000','tela']=99 #altera na copia
# print(dfCel1,'\n')
# print(dfCaracCel)


print('\n6-Alterar ordem das colunas: SO,fabricante,tela,camera,bateria,autonomia','peso')
novaordem=['SO','fabricante','tela','camera','bateria','autonomia','peso']
dfCaracCel=dfCaracCel[novaordem]
print(dfCaracCel)

print('\n7-Exibir ordenado descrescentemente por tela, fabricante')
print(dfCaracCel.sort_values(['tela','fabricante'], ascending=False))

print('\n8-Tratando NaN nas  colunas bateria e autonomia')
print('\nNas colunas bateria e autonomia NaN deve ser substituido pelo valor minimo na coluna')
dfCaracCel.fillna({'bateria':dfCaracCel.bateria.min(), 'autonomia':dfCaracCel.autonomia.min()},inplace=True)
print(dfCaracCel)

'''
9- Crie o dataframe dfPrecosCel a partir da planilha precos do arquivo 
CelularGeral.xlsx, considerando o nome do celular como indice. A primeira 
linha do arquivo contem o nome das colunas
'''
print('\n9-O dfPrecosCel')
dfPrecosCel= pd.read_excel('CelularGeral.xlsx',sheet_name='precos', index_col=0,
                         header=0)
print(dfPrecosCel)

print('\n10-Exiba as informacoes do dfPrecosCel')
dfPrecosCel.info()

print('\n11-Tratando NaN: colunas com preco NaN devem ser descartadas. Exiba')
dfPrecosCel.dropna(axis=1, inplace=True)
print(dfPrecosCel)

'''
12- Crie o dataframe dfNotasCel a partir da planilha avaliacao do arquivo 
CelularGeral.xlsx, considerando o nome do celular como indice. A primeira 
linha do arquivo contem o nome das colunas
'''
print('\n12-O dfNotasCel')
dfNotasCel= pd.read_excel('CelularGeral.xlsx',sheet_name='avaliacao', index_col=0,
                         header=0)
print(dfNotasCel)

print('\n13-Exiba as informacoes do dfNotasCel')
dfNotasCel.info()

print('\n14-Renomeie Nota Tela (NTT), Nota Camera(NTC), Nota Desempenho (NTD)')
dfNotasCel.rename(columns={'Nota Tela':'NTT','Nota Camera':'NTC', 
                           'Nota Desempenho':'NTD'}, inplace=True)
print(dfNotasCel)


print('\n15- Concatene os 3 dataframes, criando o dfCelular. Exiba')
dfCelular = pd.concat([dfCaracCel,dfPrecosCel,dfNotasCel],axis=1)
print(dfCelular)

print('\nInfo:')
dfCelular.info()

print('\n16- Incluindo Preco Medio (PrecoMed). Exiba' )
dfCelular['PrecoMed']= dfPrecosCel.mean(axis=1)
print(dfCelular)

print('\n17- Incluindo Nota Global(NTG) = 1XTela(nota)+1XCamera(nota)+2XDesempenho(nota). Exiba' )
#PESOS 1, 1 e 2
dfCelular['NTG']= (dfCelular['NTT']+dfCelular['NTC']+2*dfCelular['NTD'])/4
print(dfCelular)

print('\n18-Graficamente (barras juntas) precos no SuperCel e no TemTudo' )
dfCelular[['SuperCel','TemTudo']].plot.bar(title='Precos em 2 sites', figsize=(8,6))
plt.show()

print('\n19- Graficamente: PrecoMedio X Nota Desempenho')
dfCelular.plot.scatter(x='PrecoMed',y='NTD')
plt.show()


print('\n20- Exibir os celulares com tela >= 5.7 e com preco na CasaTecno menor que 3000')
dfResposta= dfCelular.query('tela >= 5.7 and CasaTecno <3000')
# dfResp = dfCelular.loc[ (dfCelular.tela>=5.7 ) & (dfCelular.CasaTecno <3000) ]
#print(dfResposta)
print('APENAS OS NOMES dos Modelos que atendem o criterio')
print(dfResposta.index.values)


print('\n21-Categorias (faixas) de nota global: de 0 a 6, de 6(exc) a 7,de 7 a 8, de 8 a 9, acima de 9')
print('\n- Rotular com "RUIM", "REGULAR","BOM","MUITO BOM","EXCELENTE"')
print('\n Exibir TabFreq das categorias de nota')
srFxNotG= pd.cut(dfCelular.NTG,bins=[0,6,7,8,9,10], include_lowest=True,
                 labels=["RUIM", "REGULAR","BOM","MUITO BOM","EXCELENTE"])
print('\nModelos e suas faixas (categorias):')
print(srFxNotG)
print('\nTab de Freq das Categorias')
tabFreqCat= srFxNotG.value_counts()
print(tabFreqCat)

#ATENCAO:
print('\nTabela de Frequencia Percentual (RELATIVA) graficamente')
tabFreqCat.plot.pie(title='Tab Freq Perc das Cat de Nota',
                    autopct="%.1f")
plt.show()

#ATENCAO 2:
print('\nTabela de Frequencia Percentual (RELATIVA) NUMERICAMENTE')
tfp=tabFreqCat*100/dfCelular.shape[0]  #dfCelular.NTG.size
print(tfp)

print("\n22- Qual(is) o(s) celular(es) de pior desempenho?")
ntMinDesemp= dfCelular['NTD'].min()
dfCelPiorDesemp=dfCelular.loc[dfCelular['NTD']==ntMinDesemp]
#print(dfCelPiorDesemp)
print(dfCelPiorDesemp.index.values)


print("\n23- Qual(is) o(s) celular(es) de melhor desempenho e seus precos medios?")
dfCelMelhorDesemp=dfCelular.loc[dfCelular['NTD']==dfCelular['NTD'].max()]
#print(dfCelMelhorDesemp)
print(dfCelMelhorDesemp.PrecoMed)

print("\n24-Qual(is) o(s) celular(es) de maior nota global , seu menor preco e onde ocorre seu menor preco")
dfCelMaiorNotaG= dfCelular.loc[dfCelular['NTG']==dfCelular['NTG'].max()]
print(dfCelMaiorNotaG)
dfResposta = dfPrecosCel.loc[dfCelMaiorNotaG.index]
rr= pd.concat([dfResposta.min(axis=1),dfResposta.idxmin(axis=1)])
print(dfResposta.min(axis=1),'-',dfResposta.idxmin(axis=1))
print(rr)


