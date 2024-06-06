# -*- coding: utf-8 -*-
"""
Spyder Editor

Bio 2021/2

Joisa

Exemplo com:

- substituicao de de NaN nas colunas:
    . usando valor fixo
    . usando a moda na coluna
    . usando a media na coluna
    
    
- tabela de frequencia de uma coluna
- tabela de frequencia percentual de uma coluna
- visualizacao grafica 


- crosstab: 
    tabela de frequencia especial que relaciona
    duas (ou mais) variaveis (colunas do DataFrame)
    Por exemplo, quantidade de pessoas (numero 
    de ocorrencias) da cada cor de OLHOS por 
    cada cor de CABELO)
    
- scatter: dataframe.plot.scatter(x= col1, y=col2)) 
    visualizacao grafica da relacao entre os valores 
    de duas colunas numericas
    
- funcao aplicada sobre a linha de um dataframe:
    O parametro da funcao e a linha.
    No apply, fornecer a funcao e axis=1
    
- agrupamento: medidas de uma variavel (coluna) do agrupamento

"""

"""
No arquivo dadosbio.xlsx encontram-se os dados biometricos 
de um grupo de pessoas
"""


import pandas as pd
import matplotlib.pyplot as plt

dfBio = pd.read_excel('dadosbio.xlsx',
                      index_col=0,
                      header=0)


print('\n-----------1-------------')
print('\nO DataFrame dfBio:')
print(dfBio)

print('\n-----------2-------------')
print('\nAs 4 primeiras linhas:')
print(dfBio.head(4))

print('\n-----------3-------------')
print('\nSubstituicao de NaN nas colunas')
print('SEXO->G, OLHOS->moda, CABELO->moda,PESO->media,ALTURA->media')
modaOlhos= dfBio.OLHOS.mode()
print(modaOlhos)
print(type(modaOlhos))

modaCabelo= dfBio.CABELO.mode()
print(modaCabelo)
print('\n-----------4-------------')

dfBio.fillna({'SEXO':'G','OLHOS':modaOlhos.loc[0], 
              'CABELO':modaCabelo.loc[0],
              'PESO':dfBio.PESO.mean(),
              'ALTURA':dfBio.ALTURA.mean()},
              inplace=True)

print(dfBio)

print('\n-----------5-------------')
print('\nTabela de Frequencia da variavel (coluna) OLHOS')
srTabFreqOlho=dfBio.OLHOS.value_counts()
print(srTabFreqOlho)

print('\n-----------6-------------')
print('\nTabela de Frequencia Percentual (RELATIVA) da coluna OLHOS')
# tot = srTabFreqOlho.sum()
# srTabFreqOlhoPerc= srTabFreqOlho*100/tot
srTabFreqOlhoPerc= dfBio.OLHOS.value_counts(normalize=True)*100
print(srTabFreqOlhoPerc)

print('\n-----------7-------------')
print('\nVisualizacao Grafica da TabFreq de OLHOS (BARRA)')
srTabFreqOlho.plot.bar(title='Tab Freq Olho')
plt.show()
print('\nVisualizacao Grafica da TabFreq de OLHOS (PIZZA)')
print('\n-----------8-------------')
srTabFreqOlho.plot.pie(title='Tab Freq Olho',autopct='%.1f')
plt.show()

print('\n------------------------')
print('*********CROSSTAB*********')
print('\n-----------9-------------')
print('\nRelacao da variaveis: Cor dos OLHOS por CABELO')
dfCab_Olho= pd.crosstab(index=dfBio.CABELO,
                       columns= dfBio.OLHOS)
print(dfCab_Olho)
print('\n----------10--------------')
print('\nRelacao das variaveis:Cor dos OLHOS por IDADE')
dfIdade_Olho=pd.crosstab(index=dfBio.IDADE,
                       columns= dfBio.OLHOS)
print(dfIdade_Olho)
print('Obs: essa relacao nao ficou interessante nesse caso')
print('\n-----------11-------------')
print('Melhor criar faixas (categorias)de idade:')
print('Ate 25->jovem, de 26 a 60->adulto, de 61 em diante->idoso')
srFaixasIdade=pd.cut(dfBio.IDADE, bins=[0,25,60,dfBio.IDADE.max()],
                     labels=['jovem','adulto','idoso'],
                     include_lowest=True)
print('\nFaixas (Categorias) de IDADE:')
print(srFaixasIdade)
print('\n-----------12-------------')
print('\nRelacao das variaveis:Cor dos OLHOS por FAIXAdeIDADE')
dfFaixaIdade_Olho=pd.crosstab(index=srFaixasIdade,
                       columns= dfBio.OLHOS)
print(dfFaixaIdade_Olho)
print('\n------------13------------')
print('\nRelacao das variaveis:Cor dos OLHOS por SEXO,FAIXAdeIDADE')
dfSexoFaixaId_Olho=pd.crosstab(index=[dfBio.SEXO,srFaixasIdade],
                       columns= dfBio.OLHOS)
print(dfSexoFaixaId_Olho)

print('\n------------14------------')
print('Resultado e multiIndice:acessando')
print('\n------------------------')
print(dfSexoFaixaId_Olho.loc['M'])
print('...........')
print(dfSexoFaixaId_Olho.loc['M','jovem'])
print('...........')
print(dfSexoFaixaId_Olho.xs('F',level=0))
print('...........')
print(dfSexoFaixaId_Olho.xs('jovem',level=1))


print('\n------------15------------')
print('**********SCATTER*********')
print('\n------------------------')
dfBio.plot.scatter(x='IDADE',y='ALTURA')
plt.show()
print('\n----------16--------------')

print('\nInclusao da coluna IMC= Peso/Altura*Altura')
print('\nPode ser feita diretamente operando com as colunas')
#dfBio['IMC']= dfBio.PESO/(dfBio.ALTURA *dfBio.ALTURA )
#print(dfBio.head(6))

print('\nMas pode ser feita com funcao aplicada na linha da pessoa')
def calculaIMC(linhaDaPessoa):
    imc= linhaDaPessoa.PESO/(linhaDaPessoa.ALTURA * linhaDaPessoa.ALTURA)
    #suponha (falso) que o imc do sexo masculino fosse o valor acima -3
    if linhaDaPessoa.SEXO=='M':
        imc = imc-3
    return imc


dfBio['IMC']= dfBio.apply(calculaIMC, axis=1)
print(dfBio)


print('\n------------------------')
print('********AGRUPAMENTO*******')
print('\n------------------------')
print('\n------------17A------------')

print('\nAgrupando por sexo')
print('\n==SO EXIBICAO, NUNCA MEDIDA==')

agSEXO= dfBio.groupby('SEXO')
for g, elems in agSEXO:
    print('\n--->Grupo:',g)
    print('Elems:')
    print(elems)


print('================================')
print('\nPeso max, min e medio por SEXO')
print(agSEXO.PESO.agg(['max','min','mean']))

print('\n------------17B------------')
print('\nPeso max e min  por OLHOS/CABELO')
agOC= dfBio.groupby(['OLHOS','CABELO'])
print(agOC.PESO.agg(['max','min']))

print('\n------------17C------------')
print('\nAltura media e idades minima e maxima por SEXO')
print(agSEXO.agg({'ALTURA':'mean', 'IDADE':['min','max']} ))


















