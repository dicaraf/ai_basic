"""calcola l'errore quadratico per più insiemi di valori di coefficienti e
 stampa l'indice dell'insieme che produce il più piccolo errore quadratico: 
 questa è una versione povera del metodo dei minimi quadrati, 
 in cui consideriamo solo un insieme fisso di vettori di coefficienti alternativi 
 invece di trovare l'ottimo globale."""
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    conta = -1
    for coeff in c:
        conta+=1
        x = X @ coeff
        diff = 0
        for i in range(len(x)):
            diff += (x[i] - y[i])**2
        if diff<smallest_error:
            smallest_error = diff
            best_index = conta
    print("the best set is set %d" % best_index)


find_best(X, y, c)

  