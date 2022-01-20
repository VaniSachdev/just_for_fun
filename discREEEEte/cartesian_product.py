import itertools

#calculates cartesian product of lists 
#input: lists
#outputs: tuples (ordered pairs)

my_lists = [[1, 2, 3], [1, 2, 3]]

for pair in itertools.product(*my_lists):
    print(pair)
