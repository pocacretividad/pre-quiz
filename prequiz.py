import numpy as np
import pandas as pd

#punto 1
matriz_4= np.random.rand(30,20,10,2000)
print(matriz_4.size)

#punto 2
matriz_3=matriz_4.copy()[:,:,:5]
