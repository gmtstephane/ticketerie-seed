import pandas as pd

# CREATE TABLE IF NOT EXISTS "championship" (
# 	"id" serial PRIMARY KEY NOT NULL,
# 	"name" text NOT NULL,
# 	"sport_id" integer NOT NULL,
# 	"icon" text NOT NULL,
# 	"created_at" timestamp DEFAULT now() NOT NULL,
# 	"updated_at" timestamp,
# 	CONSTRAINT "championship_name_unique" UNIQUE("name"),
# 	CONSTRAINT "championship_id_name_unique" UNIQUE("id","name")
# );

# Defining each sport's details in a list of lists. Each inner list is a row.
sports_data = [
    [
        1,
        "Ligue 1",
        2,
        "https://upload.wikimedia.org/wikipedia/fr/c/ca/Logo_Ligue_1_Uber_Eats_2020.svg",
    ],
    [
        2,
        "Ligue 2",
        2,
        "https://upload.wikimedia.org/wikipedia/fr/4/4f/Logo_Ligue_2_BKT_2020.svg",
    ],
    [
        3,
        "Ligue des Champions",
        2,
        "https://upload.wikimedia.org/wikipedia/fr/9/9a/Logo_UEFA_Champions_League_-_2021.svg",
    ],
]

# Specifying the column names for the DataFrame
columns = ["id", "name", "sport_id", "icon"]

# Creating the DataFrame from the row-based sports data
sports_df = pd.DataFrame(sports_data, columns=columns)

# Generating the CSV content, excluding the DataFrame index
csv = sports_df.to_csv(index=False)
# # Returning the CSV content
with open("output/3-championships.csv", "w") as f:
    f.write(csv)
