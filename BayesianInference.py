import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

ACTUAL_PROBABILITY= 0.5
class CoinToss:
    def __init__(self):
        self.alpha = 1
        self.beta = 1
        
    def update(self,x):
        self.alpha += x
        self.beta += 1-x


def plot():
    x = np.linspace(0,1,2000)
    y = beta.pdf(x,c.alpha,c.beta)
    plt.plot(x, y)
    plt.show()


intervals = [1, 5, 10, 100, 1000, 10000,100000, 1000000]
j = 0
c = CoinToss()
for i in range(1000000):
    num = np.random.random()
    c.update( num>=.5 )
    if i + 1 == intervals[j]:
        j += 1
        plot()

mean = c.alpha/(c.alpha+c.beta)
accuracy = (mean / ACTUAL_PROBABILITY) * 100
print(accuracy)
