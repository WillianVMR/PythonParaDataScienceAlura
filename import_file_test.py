from random import randrange, seed
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# random seed > defines a pattern for the random number generation

seed(10)

randrange(0, 11)

notas_matematica = []

for notas in range(8):
    notas_matematica.append(randrange(0, 11))

x = list(range(1, 9))
y = notas_matematica

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()


print(notas_matematica)