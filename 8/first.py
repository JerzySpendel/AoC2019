import collections
from operator import itemgetter

import numpy as np


data = [int(char) for char in open('input', 'r').read()]

array = np.array(data).reshape(-1, 6, 25)

counters = [collections.Counter(layer.reshape(-1)) for layer in array]

fewest_0 = min(counters, key=itemgetter(0))
print(fewest_0[1] * fewest_0[2])
