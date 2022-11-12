# -*- coding: utf-8 -*-
""" #TODO: terminar docstring
Essa seção importa todos os dados do query em arrays chamados value1 e value2.

Returns:
    _type_: _description_
"""

import numpy as np

path = '/home/matheus/prog/python/noale/data/'
value1, value2 = np.loadtxt(path+'values.txt', delimiter='\t', dtype=float, unpack=True)

# url generator:
"""
Esta seção gera um arquivo lista de urls com todos os i-ésimos queries.
"""

key1    = 'c'
key2    = 's'

urls    = open(path+'urls.txt','w')
for i in range(0,len(value1)):
    URL     = f'https://globalsolaratlas.info/map?{key1}={value1[i]},{value2[i]},10&{key2}={value1[i]},{value2[i]}&m=site\n'
    urls.write(URL)