import matplotlib.pyplot as plt
import numpy as np
from random import sample

x = np.linspace(0,5,10)
y = x * 2
z = x * 3

# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y,color="purple",linewidth=3, alpha=0.5, linestyle="-.", marker="*") # alpha is used for transparency

# Set lower and upper bounds for axis
# axes.set_xlim(0, 1)
# axes.set_ylim(0, 2)
# plt.show()

# Special plot types
data = sample(range(1, 1000), 100)
print(data)
plt.hist(data)
plt.show()
plt.scatter(x,y)
plt.show()