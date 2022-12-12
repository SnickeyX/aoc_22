# method uses an implementation of Dijkstra's shortest pathfinding algorithm 
# (I simply could not figure out hill climbing :/)
# TODO: implement this with a hill climbing algorithm

def find_fewest_steps(search_map, start_pos, end_pos):
    visited = set()
    current_pos = [start_pos[0], start_pos[1], 0]
    queue = []
    queue.append(current_pos)
    while len(queue) != 0:
        curr_row, curr_col, curr_steps = queue.pop(0)
        if(curr_row, curr_col) == (end_pos[0], end_pos[1]):
            return curr_steps
        if((curr_row, curr_col) in visited):
            continue
        visited.add((curr_row, curr_col))
        # trying one step in each direction
        for delta_y in range(curr_row-1, curr_row+2):
            for delta_x in range(curr_col-1, curr_col+2):
                # check if the new position is within the map and only one direction is changed
                if(len(search_map) > delta_y > 0 and len(search_map[0]) > delta_x > 0 and (delta_y == curr_row or delta_x == curr_col)):
                    if((search_map[curr_row][curr_col]+1 >= search_map[delta_y][delta_x])):
                        queue.append((delta_y, delta_x, curr_steps+1))

with open("main_input.txt") as f:
    search_map = []
    positions_of_a = []
    starting_pos = None
    goal_pos = None
    # get the inputted map and find the starting position with it
    for i,line in enumerate(f):
        if(line.count("S") > 0):
            starting_pos = [i, line.index("S")]
            line = line.replace("S", "a")
        if(line.count("E") > 0):
            goal_pos = [i, line.index("E")]
            line = line.replace("E", "z")
        if(line.count("a") > 0):
            all_a_indexes = [i for i, c in enumerate(line) if c == "a"]
            positions_of_a.extend([[i, a_index] for a_index in all_a_indexes])
        search_map.append([ord(c) % 97 for c in line.strip()])
    get_minimum_steps = find_fewest_steps(search_map, starting_pos, goal_pos)
    print("minimum steps from S: ", get_minimum_steps)
    minimum_steps_from_all_a = []
    for a_pos in positions_of_a:
        min_steps = find_fewest_steps(search_map, a_pos, goal_pos)
        # if E is not reachable, it will return None
        if(min_steps != None):
            minimum_steps_from_all_a.append(min_steps)
    print("minimum steps from all a: ", min(minimum_steps_from_all_a))