import json

def in_right_order(left,right):
    if(isinstance(left, int) and isinstance(right, int)):
        return 1 if left < right else 0 if left == right else -1 
    elif(isinstance(left, int) and isinstance(right, list)):
        return in_right_order([left], right)
    elif(isinstance(left, list) and isinstance(right, int)):
        return in_right_order(left, [right])
    else:
        if(len(left) == 0 and len(right) != 0):
            return 1
        elif(len(left) != 0 and len(right) == 0):
            return -1
        elif(len(left) == 0 and len(right) == 0):
            return 0
        else:
            compare_first = in_right_order(left[0], right[0])
            return compare_first if compare_first != 0 else in_right_order(left[1:], right[1:])

# stolen from geeks4geeks     
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if in_right_order(arr[j], arr[j+1]) == -1:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
        if not swapped:
            return
    return arr 

# before you judge me, know that this was purely for fun 
with open("main_input.txt") as f:
    print("the number of pairs in the right order is: ", sum([(idx + 1) for idx, pair in enumerate([list(map( lambda y : json.loads(y.strip()), input[i:i+2])) for input in [f.readlines()] for i in range(0, len(input), 3) ]) if in_right_order(pair[0], pair[1]) == 1]))
    
with open("main_input.txt") as f:
    print("the decoder key is: ", eval("*".join(str(item) for item in [(idx+1) for idx, value in enumerate(bubbleSort([list(map( lambda x : json.loads(x.strip()), filter( lambda x : x != "\n", input[:]))) for input in [f .readlines()]][0] + [[2]] + [[6]])) if value == [2] or value == [6]])))