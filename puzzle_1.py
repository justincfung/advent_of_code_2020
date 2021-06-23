import pandas as pd

df = pd.read_csv('puzzle_1_input.csv', header=None)
rows = df.shape[0]
# lst_size = len(lst)

# for counter in range(0, lst_size):
#     sample = [1721,979,366,299,675,1456]
#     num1 = lst[counter]
#     sample.remove(num1)
#     for item in sample:
#         if item + num1 == 2020:
#             print(item*num1)
#         else:
#             pass


for counter in range(0, rows):
    actual = df[0].tolist()
    num1 = actual[counter]
    actual.remove(num1)
    for item in actual:
        if item + num1 == 2020:
            print(item*num1)
        else:
            pass