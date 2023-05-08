import pandas

csv_file = pandas.read_csv("nato_phonetic_alphabet.csv")
# reading the csv file through pandas modulas module

dictionary = csv_file.to_dict()
# converting the csv_file into dictionary

nato_words_dictionary = {}

for i in range(len(dictionary["letter"])):
    nato_words_dictionary[dictionary['letter'][i]] = dictionary['code'][i]
    # Storing the dictionary separated values into ordered form on nato_words_dictionary/
    
user_input = list(input("Enter a Word: "))
# Getting input from the user to generate the nato word

user_nato_word = []

for i in user_input:
    letter = nato_words_dictionary[i.capitalize()]
    user_nato_word.append(letter)

print(user_nato_word)