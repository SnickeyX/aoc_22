from math import sqrt 
class Point:
    def __init__(self, x, y, id = 0) -> None:
        self.x = x 
        self.y = y 
        self.identifier = id
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
# set of all moves taken by T and knot 9
all_distinct_T_moves = set() 
all_distinct_9_moves = []
# current position of T
T = Point(0,0)
# for chall 2; all the 9 tail knots
T1 = Point(0,0,1)
T2 = Point(0,0,2)
T3 = Point(0,0,3)
T4 = Point(0,0,4)
T5 = Point(0,0,5)
T6 = Point(0,0,6)
T7 = Point(0,0,7)
T8 = Point(0,0,8)
T9 = Point(0,0,9)
# adding origin to both sets
all_distinct_T_moves.add((0,0)) 
all_distinct_9_moves.append((0,0))
# current position of H
H = Point(0,0)

# move T by x amount to right and y amount up 
def move_point(point, x, y):
    point.x += x
    point.y += y
    if(point.identifier == 0):
        all_distinct_T_moves.add((point.x, point.y))
    elif(point.identifier == 9):
        all_distinct_9_moves.append((point.x, point.y))
        
# a bit unneccessary but geometrically correct
def are_points_touching(point1, point2):
    hypotenuse = sqrt((point2.y - point1.y)**2 + (point2.x - point1.x)**2)
    if(hypotenuse <= 1.42):
        return True 
    else: 
        return False

def parse_move(move, head, tail, move_head = True):
    if(move == "R"):
        curr_H = Point(head.x, head.y)
        # move H to the right
        if(move_head):
            head.x += 1
        if(not are_points_touching(tail, head)):
            # if H is above T
            if(curr_H.y > tail.y):
                move_point(tail, 1,1)
            # if H is below T
            if(curr_H.y < tail.y):
                move_point(tail, 1,-1)
            if(head.x - 1> tail.x):
                move_point(tail, 1,0)
            assert are_points_touching(tail, head)
    elif(move == "L"):
        curr_H = Point(head.x, head.y)
        # move H to the left
        if(move_head):
            head.x += -1
        if(not are_points_touching(tail, head)):
            # if H is above T
            if(curr_H.y > tail.y):
                move_point(tail, -1,1)
            # if H is below T
            if(curr_H.y < tail.y):
                move_point(tail, -1,-1)
            if(head.x + 1 < tail.x):
                move_point(tail, -1,0)
            assert are_points_touching(tail, head)
    elif(move ==  "U"):
        curr_H = Point(head.x, head.y)
        # move H up
        if(move_head):
            head.y += 1
        if(not are_points_touching(tail, head)):
            # if H is to the right of T
            if(curr_H.x > tail.x):
                move_point(tail, 1,1)
            # if H is to the left of T
            if(curr_H.x < tail.x):
                move_point(tail, -1,1)
            if(head.y - 1 > tail.y):
                move_point(tail, 0,1)
            assert are_points_touching(tail, head)
    elif(move == "D"):
        curr_H = Point(head.x, head.y)
        # move H down
        if(move_head):
            head.y += -1
        if(not are_points_touching(tail, head)):
            # if H is to the right of T
            if(curr_H.x > tail.x):
                move_point(tail, 1,-1)
            # if H is to the left of T
            if(curr_H.x < tail.x):
                move_point(tail, -1,-1)
            if(head.y + 1 < tail.y):
              move_point(tail, 0,-1)   
            assert are_points_touching(tail, head) 

# needs heavy refactoring
with open("main_input.txt") as file:
    moves = file.readlines()
    moves = "".join([move[0]*int(move.strip()[2:]) for move in moves])
    for move in moves:
        parse_move(move, H, T)
    # resetting H for chall 2
    H = Point(0,0)
    for move in moves:
        parse_move(move, H, T1)
        parse_move(move, T1, T2, False)
        parse_move(move, T2, T3, False)
        parse_move(move, T3, T4, False)
        parse_move(move, T4, T5, False)
        parse_move(move, T5, T6, False)
        parse_move(move, T6, T7, False)
        parse_move(move, T7, T8, False)
        parse_move(move, T8, T9, False)
        
    print("the total number of distinct locations T visits is: ", len(all_distinct_T_moves))
    print("the total number of distinct locations T9 visits is: ", len(all_distinct_9_moves))