import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x * 2

# plt.plot(x, y,'r--') # third argument is the line type and color
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.title("Title")
#
# plt.subplot(1,2,1)
# plt.plot(x, y, "r")
#
# plt.subplot(1,2,2)
# plt.plot(y, x, "b")
# plt.show()

# Object-Oriented Way
figure = plt.figure()
# axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y)
# axes.set_xlabel("X-label")
# axes.set_ylabel("Y-label")
# axes.set_title("Title")
# plt.show()

# Putting 2 figures in one canvas
axes_one = figure.add_axes([0.1, 0.1, 0.3, 0.8])
axes_one.plot(x, y,"r--")
axes_one.set_xlabel("One_X_label")
axes_one.set_ylabel("One_Y_label")
axes_one.set_title("One_Title")

axes_two = figure.add_axes([0.5, 0.1, 0.3, 0.8])
axes_two.plot(y, x,"b--")
axes_two.set_xlabel("Two_X_label")
axes_two.set_ylabel("Two_Y_label")
axes_two.set_title("Two_Title")

plt.show()