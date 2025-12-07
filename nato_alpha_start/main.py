import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pd.read_csv("nato.csv")
# dict_df = nato_data.to_dict()
# print(dict_df)
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato_list = [nato_dict[letter] for letter in word]
print(nato_list)