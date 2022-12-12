# My failed attempt at a greedy hill climbing algorithm
# worked with the given example but not with the actual input
# I think the problem is that I'm not considering the possibility of moving to a lower elevation

import random

# greedy hill climbing algorithm
def generate_random_sols(map, starting_pos, goal_elevation, goal_pos = None):
    solution = []
    max_num_turns = 10000
    current_pos = [starting_pos[0], starting_pos[1]] 
    current_elevation = map[current_pos[0]][current_pos[1]] 
    turns_taken = 0

    while(current_elevation != goal_elevation or (current_elevation == 25 and current_pos != goal_pos)):
        if(turns_taken > max_num_turns):
            break 
        print("current pos: ", current_pos, " current elevation: ", current_elevation)
        # 0 = left, 1 = up, 2 = right, 3 = down
        possible_moves = [] 
        # try moving left
        if(current_pos[1] > 0):
            dest_elevation = map[current_pos[0]][current_pos[1] - 1]
            if(dest_elevation <= current_elevation + 1):
                possible_moves.append((0, dest_elevation))
        # try moving up
        if(current_pos[0] > 0):
            dest_elevation = map[current_pos[0] - 1][current_pos[1]]
            if(dest_elevation <= current_elevation + 1):
                possible_moves.append((1, dest_elevation))
        # try moving right
        if(current_pos[1] < len(map[0]) - 1):
            dest_elevation = map[current_pos[0]][current_pos[1] + 1]
            if(dest_elevation <= current_elevation + 1):
                possible_moves.append((2, dest_elevation))
        # try moving down
        if(current_pos[0] < len(map) - 1):
            dest_elevation = map[current_pos[0] + 1][current_pos[1]]
            if(dest_elevation <= current_elevation + 1):
                possible_moves.append((3, dest_elevation))
        print(possible_moves)
        move_chosen = random.choice([move for move in possible_moves if move[1] >= current_elevation])
        current_elevation = move_chosen[1]
        if(move_chosen[0] == 0):
            current_pos[1] -= 1
        elif(move_chosen[0] == 1):
            current_pos[0] -= 1
        elif(move_chosen[0] == 2):
            current_pos[1] += 1
        elif(move_chosen[0] == 3):
            current_pos[0] += 1 
        solution.append((current_pos[0], current_pos[1]))
        turns_taken += 1
        
    if(turns_taken > max_num_turns):
        return None
    else: 
        return (solution[-1][0], solution[-1][1], len(set(solution)) + starting_pos[2])

# generate random solutions and pick the best one (until no improvement is made for 100 cycles)
def find_fewest_steps(map, starting_pos, goal_elevation, goal_pos = None):
    destination_positions = set()
    destination_pos_with_steps = generate_random_sols(map, starting_pos, goal_elevation, goal_pos=goal_pos)
    if(destination_pos_with_steps == None):
        return []
    previous_minimum_steps = destination_pos_with_steps[2]
    cycles_without_improvement = 0
    while(True):
        if(cycles_without_improvement > 100):
            break
        if(destination_pos_with_steps[2] >= previous_minimum_steps):
            print("current minimum steps", previous_minimum_steps, " at cycle ", cycles_without_improvement)
            # if the current solution is the same as the previous minimum, add it to the set of solutions
            if(destination_pos_with_steps[2] == previous_minimum_steps):
                destination_positions.add(destination_pos_with_steps)
            cycles_without_improvement += 1
        else:
            cycles_without_improvement = 0
            destination_positions.clear()
            previous_minimum_steps = destination_pos_with_steps[2]
            destination_positions.add(destination_pos_with_steps)
        #while(destination_pos_with_steps == None):
        destination_pos_with_steps = generate_random_sols(map, starting_pos, goal_elevation, goal_pos=goal_pos)
        if(destination_pos_with_steps == None):
            return []
    return list(destination_positions)

with open("main_input.txt") as f:
    search_map = []
    starting_positions = None
    goal_pos = None
    # get the inputted map and find the starting position with it
    for i,line in enumerate(f):
        if(line.count("S") > 0):
            # starting_positions value of the form [row, col, steps_till_here]
            starting_positions = [[i, line.index("S"), 0]]
            line = line.replace("S", "a")
        if(line.count("E") > 0):
            goal_pos = [i, line.index("E")]
            line = line.replace("E", "z")
        search_map.append([ord(c) % 97 for c in line.strip()])
    # generate random solutions and pick the best one
    for i in range(1,26):
        new_starting_positions = []
        print("number of destination positions: ", len(starting_positions))
        for starting_pos in starting_positions:
            print("starting pos: ", starting_pos)
            if(i == 25):
                destination_positions = find_fewest_steps(search_map, starting_pos, i, goal_pos = goal_pos)
            else:
                destination_positions = find_fewest_steps(search_map, starting_pos, i)
            new_starting_positions.extend(destination_positions)
        starting_positions = new_starting_positions.copy()
    print(starting_positions)