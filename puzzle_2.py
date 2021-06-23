import re
import pandas as pd

input = pd.read_csv('puzzle_2_input.csv', delim_whitespace=True, header=None)
row_size = input.shape[0]


least_regex = re.compile(r'(\d{1,2})\-(\d{1,2})')
least_lengths = [int(least_regex.search(item).group(1)) for item in input[0].tolist()]
greatest_lengths= [int(least_regex.search(item).group(2)) for item in input[0].tolist()]

letters = [item.replace(':', '') for item in input[1].tolist()]
passwords = input[2].tolist()


cuanto = 0
# print(letter)
for counter in range(0, row_size):
    letter = letters[counter]
    least_length = least_lengths[counter]
    greatest_length = greatest_lengths[counter]
    password = passwords[counter]

    count = password.count(letter)
    if count >= least_length and count <= greatest_length:
        cuanto += 1
    else:
        pass

print(f'There are {cuanto} valid passwords.')
