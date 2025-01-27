"""
Abbiamo due dadi nel cassetto della scrivania. Uno è un dado normale, 
semplice, con sei facce, in modo che ciascuna faccia abbia la stessa 
probabilità di 1/6. L'altro è un dado truccato che ha anche sei facce, 
ma che tuttavia dà come risultato 6 ogni secondo tentativo in media, 
con le altre cinque facce ugualmente probabili.

Quindi con il primo dado normale le probabilità di ogni lato sono le stesse, 0,167 (o 16,7%). 
Con il secondo dado caricato, la probabilità di 6 è 0,5 (o 50%) e ciascuno 
degli altri cinque lati ha probabilità 0,1 (o 10%).

Il programma seguente riceve come input la scelta del dado e poi simula una sequenza di dieci lanci.

Poi usa il metodo naive Bayes per aggiornare le probabilità dopo ogni risultato per decidere quale 
dei dadi è più probabile, se truccato o meno. 
"""
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # loaded

def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1 
    for roll in sequence:
        print("rolled %d" % roll)
        
    return sequence

def bayes(sequence):
    odds = 1.0           # start with odds 1:1
    for roll in sequence:
        odds = odds*p2[roll-1]/p1[roll-1]
                     # edit here to update the odds
    if odds > 1:
        return True
    else:
        return False

sequence = roll(True)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")

  