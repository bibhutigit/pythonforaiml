import pandas as pd
import matplotlib.pyplot as plt

my_dict_data = {"name":["Bibhuti","Plaban","Soumya","Ajit","Prashant","Rajat"]
                , "marks":[80,80,90,90,95,95]}
my_df = pd.DataFrame(my_dict_data)
# my_df["marks"].plot(kind="hist",bins=5)
# Or
# my_df["marks"].plot.hist()
my_df["marks"].plot.area(alpha=0.4)
plt.show()