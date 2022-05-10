import pandas
pandas_list = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))
words_dict = {row.letter: row.code for (index, row) in pandas_list.iterrows()}
user_input = input("What is the word you want to explain? ").upper()
output_list = [words_dict[letter] for letter in user_input]
print(output_list)
