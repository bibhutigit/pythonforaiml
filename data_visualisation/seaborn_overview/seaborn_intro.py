import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")
my_head = tips.head()

# sns.displot(tips["total_bill"],bins=40)
# plt.show()

# Joint Plots
# sns.jointplot(data=tips,x="total_bill",y="tip",kind="hex")
# plt.show()

# sns.jointplot(data=tips,x="total_bill",y="tip",kind="kde") #kind can be hex, reg and kde
# plt.show()

# Pair plot
# Plots for each numerical data against each other.
# sns.pairplot(tips,hue="sex",kind="reg")

# Categorical Plots
sns.barplot(data=tips,x="sex",y="total_bill", estimator=np.std)
plt.show()