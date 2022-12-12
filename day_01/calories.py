from more_itertools import split_at

with open("calories.txt") as f: 
    calories = [line for line in f]
    sublist = [ 
    sum([int(item.rstrip()) for item in sublist])
    for sublist in split_at(calories, lambda i: i == '\n')
    if sublist ]
    sublist.sort()
    print("largest element is:", sublist[-1])    
    print("sum of three largest elements ",sum(sublist[-1:-4:-1]))