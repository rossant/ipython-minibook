import numpy as np
import matplotlib.pyplot as plt
def myfun():
    dx = np.random.randn(1000, 10000)
    x = np.sum(dx, axis=0)
    plt.hist(x, bins=np.linspace(-100, 100, 20))
    