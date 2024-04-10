import pandas as pd


# Sample Dataset
# Let's consider this small dataset containing statistics of basketball players:

df = pd.DataFrame({
    'Player': ['L. James', 'K. Durant', 'M. Jordan', 'S. Curry', 'K. Bryant'],
    'Points': [27.0, 26.0, 32.0, 24.0, 26.0],
    'Assists': [5.7, 4.7, 4.2, 6.6, 7.4]
})

# Note that there is a tie in Points between "K. Durant" and "K. Bryant".

# Learning How to Sort
# We can sort DataFrame values using the sort_values() function.

sorted_df = df.sort_values(by='Points', ascending=False)
print(sorted_df)
'''Output:
      Player  Points  Assists
2  M. Jordan    32.0      4.2
0   L. James    27.0      5.7
1  K. Durant    26.0      4.7
4  K. Bryant    26.0      7.4
3   S. Curry    24.0      6.6
'''

# In this example, the DataFrame is sorted by column Points in descending order using the by and ascending parameters. Thus, we can list the most successful players in terms of average points scored.

# Sorting by Multiple Columns
# In the previous example, pandas resolves a tie between "K. Durant" and "K. Bryant" by index, putting the player with the lower index first. Do you agree that a more reasonable decision would be to resolve ties by other players' characteristics – for example, putting players with higher Assists scores first?

# It is possible by providing multiple sorting columns.

sorted_df = df.sort_values(by=['Points', 'Assists'], ascending=False)
print(sorted_df)
'''Output:
      Player  Points  Assists
2  M. Jordan    32.0      4.2
0   L. James    27.0      5.7
4  K. Bryant    26.0      7.4
1  K. Durant    26.0      4.7
3   S. Curry    24.0      6.6
'''

# In this example, the DataFrame is sorted by column Points and any ties are resolved by the column Assists.

# Sorting by Multiple Columns in Different Order
# Let's alter the behavior and handle ties by sorting players alphabetically:

sorted_df = df.sort_values(by=['Points', 'Player'], ascending=False)
print(sorted_df)
'''Output:
      Player  Points  Assists
2  M. Jordan    32.0      4.2
0   L. James    27.0      5.7
1  K. Durant    26.0      4.7
4  K. Bryant    26.0      7.4
3   S. Curry    24.0      6.6
'''

# As ascending=False, player names' sorting is also descending, which results in reverse alphabetical order. To fix it we can pass two values to ascending, defining behavior of sorting differently for 'Points' and 'Player':

sorted_df = df.sort_values(by=['Points', 'Player'], ascending=[False, True])
print(sorted_df)
'''Output:
      Player  Points  Assists
2  M. Jordan    32.0      4.2
0   L. James    27.0      5.7
4  K. Bryant    26.0      7.4
1  K. Durant    26.0      4.7
3   S. Curry    24.0      6.6
'''

# 'Points' sorting is still in descending order, but 'Player' sorting is in ascending.