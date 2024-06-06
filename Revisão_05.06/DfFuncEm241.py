# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:39:46 2024

@author: PC-PROF
"""

import pandas as pd
import matplotlib.pyplot as plt

lfunc  = [['lala', 'RH', 4000, 40], 
          ['tutu', 'INF', None, 30],
          ['vava', 'ADM', 3000, None],
          ['nena', 'INF', 6000, None],
          ['gigi', 'PROJ', 5000, 46],
          ['kaka', 'PROJ', None, 33],
          ['lulu', 'PROJ', 9000, 66],
          ['dudu', 'INF', 3000, 23],
          ['buba', 'ADM', 7000, 48],
          ['pepe', 'ADM', 4000, 34],
          ['didi', 'RH', 2000, 55], 
          ['juju', 'RH', None, 38],
          ['zizi', 'INF', 4500, 27]]

dfFunc= pd.DataFrame(lfunc,
                     columns=['nome','departamento','salario','idade'])

print('\n---------1 ----------')
print(dfFunc)

print('\n---------2 ----------')
dfFunc.set_index('nome',inplace=True)
print(dfFunc)

print('\n---------3 ----------')
print('Exibindo sem  elementos com NaN na coluna idade')
print(dfFunc.dropna(subset=['idade']))

print('\n---------4 ----------')
print('Substituindo NaN do salario pela menor salario POR DEPARTAMENTO')
# método transform
agDep = dfFunc.groupby('departamento')
#print(agDep.groups)

# print('-------')
# print('\nSó para exibição, nunca para medidas')
# for grupo, elems in agDep:
#     print('\n---> Grupo: ',grupo)
#     print(elems)
# print('-------')

print('\n----Menor Salario Por Departamento--')
print(agDep['salario'].min())

print('-- outra forma--')
print(agDep.salario.apply('min'))

print('==== NOVO: transform ====')
print('\nCADA FUNCIONARIO COM O MENOR SALARIO DO SEU DEPARTAMENTO')
print(agDep.salario.transform('min'))

print('\nFazendo a substituição: ')
print('salario ausente pelo menor salario por departamente, e')
print('idade ausente pela mediana das idades')
print('\n')

dfFunc.fillna(value={'salario': agDep.salario.transform('min'),
                       'idade': dfFunc.idade.median() },
              inplace=True)

print(dfFunc)

print('\n---------5 ----------')
print('\nGraficamente: salario X idade')
dfFunc.plot.scatter(x='idade', y='salario' )
plt.show()





