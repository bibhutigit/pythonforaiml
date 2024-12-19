import pandas as pd

squirrel_data = pd.read_csv("./squirrel-data.csv")
gray_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"]=="Gray"]["Primary Fur Color"]
black_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"]=="Black"]["Primary Fur Color"]
cinnamon_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"]=="Cinnamon"]["Primary Fur Color"]

result_data_dict = {
    "Fur_Color":["Gray","Black", "Cinnamon"]
    ,"Count":[gray_squirrel_data.count(),black_squirrel_data.count(),cinnamon_squirrel_data.count()]
}

result_df = pd.DataFrame(result_data_dict)
result_df.to_csv("./squirrel_color_counts.csv")