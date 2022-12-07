TOTAL_SIZE = 70000000
UPDATE_SIZE = 30000000
filesystem_size = dict()

def replace_dir_name(parent, old_dir_name, new_dir_name):
    parent_list = filesystem_size[parent]
    parent_list = [word.replace(old_dir_name, new_dir_name) for word in parent_list]
    filesystem_size[parent] = parent_list

def calculate_size_of_dir(input_dir):
    total_size = 0
    for idx, item in enumerate(filesystem_size[input_dir]):
        if item.isdigit():
            total_size += int(item)
        elif item == "dir":
            dir = filesystem_size[input_dir][idx+1]
            total_size+= calculate_size_of_dir(dir)
    return total_size

with open("big_filesystem.txt") as f: 
    # format input for easy parsing
    cmd_output = list(map(str.strip," ".join([line.strip() for line in f]).split("$")))
    # curr_dir will be at the top
    dir_stack = []
    dup_dirs  = []
    # parse input to create a hashmap of the filesystem
    for line in cmd_output:
        if line.startswith("cd"):
            dir = line.split(" ")[-1]
            if(dir == ".."):
                dir_stack.pop()
            else:
                dir_stack.append(dir)
                # dealing with duplicate directories by appending a number to the end
                # very hacky but i really wanted to use a dict for this
                if(dir in filesystem_size.keys()):
                    for i in range(0,len(cmd_output)):
                        new_dir_name = dir + str(i)
                        if(new_dir_name not in filesystem_size.keys()):
                            filesystem_size[new_dir_name] = []
                            replace_dir_name(dir_stack[-2], dir, new_dir_name)
                            dir_stack.pop()
                            dir_stack.append(new_dir_name)
                            break
                else:
                    filesystem_size[dir] = []
        elif line.startswith("ls"):
            files = line.split(" ")[1:]
            filesystem_size[dir_stack[-1]] = files

if __name__ == "__main__":
    all_dir_sizes = [calculate_size_of_dir(dir) for dir in filesystem_size]
    unused_space = TOTAL_SIZE - calculate_size_of_dir("/")
    curr_min_space = all_dir_sizes[0]
    print("Total size of all dirs less that 100000 in size are: {}".format(sum([n for n in all_dir_sizes if n <= 100000])))
    for dir_size in all_dir_sizes:
        if(dir_size + unused_space  >= UPDATE_SIZE):
            curr_min_space = min(curr_min_space, dir_size)
    print("Minimum size of a dir that can be updated is: {}".format(curr_min_space))
        