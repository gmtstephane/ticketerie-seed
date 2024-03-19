import pandas as pd

# Defining each sport's details in a list of lists. Each inner list is a row.
sports_data = [
    [1, "Basketball", "Team"],
    [2, "Football", "Team"],
    [3, "Volleyball", "Team"],
]

# Specifying the column names for the DataFrame
columns = ["id", "name", "sport_type"]

# Creating the DataFrame from the row-based sports data
sports_df = pd.DataFrame(sports_data, columns=columns)

# Generating the CSV content, excluding the DataFrame index
csv = sports_df.to_csv(index=False)
# # Returning the CSV content
with open("output/2-sports.csv", "w") as f:
    f.write(csv)
