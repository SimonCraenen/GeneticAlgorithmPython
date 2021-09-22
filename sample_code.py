import sys

class Soda:
    def __init__(self, name: str, price: float) -> None:
        self.price: float = price
        self.name: str = name

    def __repr__(self) -> str:
        return 'name={name}, price={price}'.format(name=self.name, price=self.price)

# generators
sodas = [Soda('Cola', 1.5), Soda('Fanta', 1.2), Soda('Ice Tea', 1.6)]
# get a property of an object with a generator
soda_prices = [soda.price for soda in sodas]
soda_prices_doubled = [soda.price * 2 for soda in sodas]

temp = [[1, 2, 3], [4, 5, 6]]
print([b for a in temp for b in a])

# max functie
most_expensive_soda = max(sodas, key=lambda s: s.price)
print(most_expensive_soda)

# randoms
from random import choice, choices, sample, uniform
## choices and sample select items from a list 
## choices selects with replacement, sample selects without replacement
## you can select multiple items in one go, and give probability weights for each item to be selected
temp = [1, 2, 3]
print(choice(temp))
print(choices(temp, k=4))
print(sample(temp, k=3)) # k <= len(list), no replacement
print()
for i in range(10):
    print(choices(temp, k=2, weights=[5, 3, 1]))
print()
print('uniform', uniform(-1, 1)) # lower bound and upper bound

# numpy
import numpy as np
temp:np.ndarray = np.array([[1, 2], [3, 4], [5, 6]])
print(temp.shape)
zeros = np.zeros(shape=(3, 2))
ones = np.ones(shape=(3, 2))
print(np.vstack([zeros, ones]))
shape = temp.shape
for j in range(shape[0]):
    for i in range(shape[1]):
        print(temp[j,i])

# casting
a = 5 / 3
print(a, int(a)) # integer division makes floats in python