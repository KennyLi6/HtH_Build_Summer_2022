import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

game_sales_data = pandas.read_csv("Finding-an-Interesting-Dataset/game_sales.csv")

print(game_sales_data)