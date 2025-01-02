import matplotlib.pyplot as plt
import numpy as np
from IPython.core.pylabtools import figsize

x = np.linspace(0,5,11)
y = x * 2
z = x * 3

# Instead of using figure and axes we can use subplots
# fig,(ax1,ax2) = plt.subplots(1,2)
# ax1.plot(x, y)
# ax1.set_xlabel("One_X_label")
# ax1.set_ylabel("One_Y_label")
# ax1.set_title("One_Title")
#
# ax2.plot(y, x)
# ax2.set_xlabel("Two_X_label")
# ax2.set_ylabel("Two_Y_label")
# ax2.set_title("Two_Title")

# Set figure size
# fig,(ax1,ax2) = plt.subplots(2,1, figsize=(8,8))
# ax1.plot(x, y)
# ax1.set_xlabel("One_X_label")
# ax1.set_ylabel("One_Y_label")
# ax1.set_title("One_Title")
#
# ax2.plot(y, x)
# ax2.set_xlabel("Two_X_label")
# ax2.set_ylabel("Two_Y_label")
# ax2.set_title("Two_Title")
# plt.tight_layout()

# Legends
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,label="X squared")
ax.plot(x,z,label="X Cubed")
ax.legend(loc="best")
plt.show()


