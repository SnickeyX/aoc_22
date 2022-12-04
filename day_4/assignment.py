def count_complete_overlap(elf_1_set, elf_2_set):
    return 1 if (elf_1_set.issubset(elf_2_set) or elf_2_set.issubset(elf_1_set)) else 0
    
def count_overlap(elf_1_set, elf_2_set):
    return 1 if any(x in elf_1_set for x in elf_2_set) else 0 

with open("assignment.txt") as f: 
    assignment_content = [line for line in f]
    num_overlaps= 0
    num_subsets = 0
    for assignment in assignment_content:
        split_assignment = assignment.split(",")
        elf_1_assignment = split_assignment[0].split("-")
        elf_2_assignment = split_assignment[1].split("-")
        elf_1_set = set(range(int(elf_1_assignment[0]), int(elf_1_assignment[1]) + 1))
        elf_2_set  = set(range(int(elf_2_assignment[0]), int(elf_2_assignment[1]) + 1))
        num_subsets  += count_complete_overlap(elf_1_set, elf_2_set)
        num_overlaps += count_overlap(elf_1_set, elf_2_set)
    print("Number of complete overlaps: ", num_subsets)
    print("Number of overlaps: ", num_overlaps)
    