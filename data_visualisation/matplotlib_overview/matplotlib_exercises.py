import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import alpha
from sympy.printing.pretty.pretty_symbology import line_width

x = np.arange(0,100)
y = x * 2
z = x ** 2

# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# plt.show()

#Or
fig,(axes1,axes2) = plt.subplots(nrows=1, ncols=2)
axes1.plot(x,y,color="blue",lw=3,alpha=0.5,ls="--",marker="*")
axes1.set_xlim(0,10)
axes1.set_ylim(0,50)

axes2.plot(x,z)
axes2.set_xlim(0,10)
axes2.set_ylim(0,100)

plt.show()

# x-limits and y-limits
