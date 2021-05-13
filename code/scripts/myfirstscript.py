import numpy as np
import matplotlib.pyplot as plt

x=np.genfromtxt("../../data/x.csv")
y=np.genfromtxt("../../data/y.csv")
print(x,y)

plt.plot(x,y)
plt.show()
