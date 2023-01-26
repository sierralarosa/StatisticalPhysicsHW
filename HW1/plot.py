import matplotlib.pyplot as plt
import numpy as np
from math import comb

# Define the number of coins
n = 50

# Create an array of possible number of heads
heads = np.arange(0, n+1)

# Calculate the probability of getting n heads
prob = [comb(n, h) * (1/2)**h * (1/2)**(n-h) for h in heads]

# Create the plot
plt.plot(heads, prob)
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title(f'Probability of Getting n Heads for {n} Coins')
plt.show()

