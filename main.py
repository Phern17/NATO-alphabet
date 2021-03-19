import pandas


student_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}
print(nato_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_in = input("What's your name?: ").upper()
    try:
        output_nato = [nato_dict[alphabet] for alphabet in user_in]
    except KeyError:
        print("Please enter letters only~")
        generate_phonetic()
    else:
        print(output_nato)


generate_phonetic()
