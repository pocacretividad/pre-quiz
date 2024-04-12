import numpy as np
import pandas as pd

#punto 1
matriz_4= np.random.rand(30,20,10,2000)
print(matriz_4.size)

#punto 2
matriz_3=matriz_4.copy()[:,:,:5]

#punto 3
print("dimensiones:", matriz_3.ndim)
print("tamaño:", matriz_3.size)
print("forma:", matriz_3.shape)

#punto 4
matriz_2=matriz_3.reshape(-1,matriz_3.shape[-1])
print("dimensiones matriz 2D:", matriz_2.ndim)