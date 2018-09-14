import matplotlib.pyplot as plt
import numpy as np
import random as rd

data = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
dados = []

for i in range(10):
    dados.append(rd.randint(0,10))

print(dados)
np_data = np.array(data)
np_dados = np.array(dados)
print(np_dados)

plt.plot(np_data,np_dados)
plt.show()