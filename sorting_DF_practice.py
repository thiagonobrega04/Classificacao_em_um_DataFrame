import pandas as pd

# # Howdy, Space Voyager! As a data analyst, your space mission involves sorting stocks based on their closing prices from highest to lowest. For stocks that share the same closing prices, your task is to sort them in ascending order by their trading volume.

# # Your task focuses on two key aspects: closing prices and trading volume. These are highly significant parameters in stock analysis, so it's essential to handle them correctly.

# # Luckily, the functional code is provided. It will serve as a guide to assist you in deeper understanding of the topic. Just hit the Run button and see it in action!

# stock_df = pd.DataFrame({
#     'Stock': ['AAPL', 'GOOG', 'MSFT', 'FB', 'AMZN'],
#     'Close_Price': [284.91, 2719.79, 284.91, 3346.83, 3346.83],
#     'Trading_Volume': [78957282, 1271171, 23149516, 7689521, 2439136]
# })

# sorted_stock_df = stock_df.sort_values(by=['Close_Price', 'Trading_Volume'], ascending=[False, True])
# print(sorted_stock_df)

# # Hey, Stellar Navigator! You've brilliantly sorted the stock prices and volumes in descending order. Now, let's shift gears slightly. Could you modify the code to sort by 'Price' in descending order, and resolve ties alphabetically?

# stock_data = pd.DataFrame({
#     'Stock': ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB'],
#     'Price': [125.9, 234.5, 2029.4, 3054.2, 234.5],
#     'Volume': [90980867, 22653662, 1111934, 2941516, 17879803]
# })

# sorted_data = stock_data.sort_values(by=['Price', 'Stock'], ascending=[False, True])
# print(sorted_data)

# Excellent job, Celestial Traveler! Now, embark on a new quest. Are you able to sort the DataFrame by 'Price' and 'Volume', maintaining the highest price at the top and the lowest volume first? Go for it. You were made for this!

# df = pd.DataFrame({
#     'Stock': ['Apple', 'Amazon', 'Microsoft', 'Tesla', 'Facebook'],
#     'Price': [279.70, 3156.13, 217.69, 673.58, 217.69],
#     'Volume': [72291800, 17404000, 30931200, 41089200, 15290200]
# })

# # TODO: Sort dataframe by 'Price' and 'Volume', keeping higher 'Price' at top and lower 'Volume' first.
# sorted = df.sort_values(by=['Price', 'Volume'], ascending=[False, True])
# print(sorted)

# As an aspiring Stock Market Analyst, your task is to write a small Python program using a Pandas DataFrame. This program should be similar to the one you saw earlier, and its function is to track a company's stock information. The data should be sorted primarily by Market Cap and secondarily by Share Price. May the stellar sorting powers guide you!

df = pd.DataFrame({
    'Company': ['Micron Technology', 'Exxon Mobil', 'Facebook', 'Tesoro', 'Apple'],
    'Share Price': [73.12, 55.31, 280.83, 85.99, 119.03],
    'Market Cap': [80.72, 234.47, 2000, 80.72, 2000]
})

# TODO: Sort the DataFrame by 'Market Cap' in descending order
#       and for the ties, sort by 'Share Price' in ascending order.
sorted_df = df.sort_values(by=['Market Cap', 'Share Price'], ascending=[False, True])

# TODO: Print the sorted DataFrame.
print(sorted_df)