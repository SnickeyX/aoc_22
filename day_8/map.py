def num_visible_trees_left(grid, row_num, col_num, chall_num = 1):
    # check if the current cell's tree is invisible 
    current_tree_height = grid[row_num][col_num]
    num_trees_visible_left = 0
    # checking how many visible trees are there to the left
    for var_col_num in range(col_num - 1, -1, -1):
        if grid[row_num][var_col_num] >= current_tree_height:
            if(chall_num == 1):
                return num_trees_visible_left 
            else:
                return num_trees_visible_left + 1
        else:
            num_trees_visible_left += 1
    return num_trees_visible_left

def num_visible_from_right(grid, row_num, col_num, chall_num = 1):
    # check if the current cell's tree is invisible 
    current_tree_height = grid[row_num][col_num]
    num_trees_visible_right = 0
    # checking if visible from left
    for var_col_num in range(col_num + 1, len(grid[0])):
        if grid[row_num][var_col_num] >= current_tree_height:
            if(chall_num == 1):
                return num_trees_visible_right
            else:
                return num_trees_visible_right + 1
        else:
            num_trees_visible_right += 1
    return num_trees_visible_right

def num_visible_from_top(grid, row_num, col_num, chall_num = 1):
    # check if the current cell's tree is invisible 
    current_tree_height = grid[row_num][col_num]
    num_trees_visible_top = 0
    # checking if visible from left
    for var_row_num in range(row_num - 1, -1, -1):
        if grid[var_row_num][col_num] >= current_tree_height:
            if(chall_num == 1):
                return num_trees_visible_top
            else: 
                return num_trees_visible_top + 1
        else:
            num_trees_visible_top += 1
    return num_trees_visible_top

def num_visible_from_bottom(grid, row_num, col_num, chall_num = 1):
    # check if the current cell's tree is invisible 
    current_tree_height = grid[row_num][col_num]
    num_trees_visible_bottom = 0
    # checking if visible from left
    for var_row_num in range(row_num + 1, len(grid)):
        if grid[var_row_num][col_num] >= current_tree_height:
            if(chall_num == 1):
                return num_trees_visible_bottom
            else:
                return num_trees_visible_bottom + 1
        else: 
            num_trees_visible_bottom += 1
    return num_trees_visible_bottom

def tree_stat_provider(grid, chall_num = 1):
    num_visible_trees = 0
    scenic_scores = []
    max_col_len = len(grid[0])
    max_row_len = len(grid)
    for row_num in range(max_row_len):
        # current coords will be (row_num, col_num)
        for col_num in range(max_col_len):
            if(chall_num == 1):
                # trees on the edge are accounted for in one these functions since
                # they simply return True if they cant traverse the grid in any one direction
                num_trees_visible_to_left = num_visible_trees_left(grid, row_num, col_num)
                if (num_trees_visible_to_left == col_num):
                    num_visible_trees += 1
                    continue
                # visible from right
                num_trees_visible_to_right = num_visible_from_right(grid, row_num, col_num)
                if(num_trees_visible_to_right == max_col_len - col_num - 1):
                    num_visible_trees += 1
                    continue
                # visible from top
                num_trees_visible_from_top = num_visible_from_top(grid, row_num, col_num)
                if(num_trees_visible_from_top == row_num):
                    num_visible_trees += 1
                    continue
                # visible from bottom
                num_trees_visible_from_bottom = num_visible_from_bottom(grid, row_num, col_num)
                if(num_trees_visible_from_bottom == max_row_len - row_num - 1):
                    num_visible_trees += 1
                    continue   
            elif(chall_num == 2):
                num_trees_visible_to_left = num_visible_trees_left(grid, row_num, col_num,2)
                num_trees_visible_to_right = num_visible_from_right(grid, row_num, col_num,2)
                num_trees_visible_from_top = num_visible_from_top(grid, row_num, col_num,2)
                num_trees_visible_from_bottom = num_visible_from_bottom(grid, row_num, col_num,2)
                scenic_score = num_trees_visible_to_left * num_trees_visible_to_right * num_trees_visible_from_top * num_trees_visible_from_bottom
                scenic_scores.append(scenic_score)     
    if (chall_num == 1):
        return num_visible_trees
    else:
        return scenic_scores
            
with open("main_input.txt") as file:
    lines = file.readlines()
    tree_grid = [line.strip() for line in lines]
    total_num_tree = sum([len(row) for row in tree_grid])
    total_visible_trees = tree_stat_provider(tree_grid)
    all_scenic_scores   = tree_stat_provider(tree_grid, chall_num = 2)
    print("Total number of visible trees are : ", total_visible_trees)
    print("The highest scenic score is : ", max(all_scenic_scores))