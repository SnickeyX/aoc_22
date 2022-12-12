def find_common_item(comp1, comp2):
    l = list(set(comp1).intersection(comp2))
    return l[0]

def calculate_pts(letter):
    if(letter == None):
        return 0 
    ord_num = ord(letter)
    if ord_num >= 97:
        return ord_num % 96
    else:
        return ord_num % 64 + 26
    
def find_common_three(sack1, sack2, sack3):
    common = list(set(sack1).intersection(sack2).intersection(sack3))
    if "\n" in common:
        common.remove("\n")
    print(common)
    return common[0] 

with open("rucksack.txt") as f: 
    sack_content = [line for line in f]
    chall_num = 2
    total_pts = 0
    if(chall_num == 1):
        for sack in sack_content:
            div_line = len(sack) // 2
            common = find_common_item(sack[:div_line], sack[div_line:])#
            total_pts += calculate_pts(common)
    else:
        for i in range(0, len(sack_content), 3):
            common = find_common_three(sack_content[i],sack_content[i+1],sack_content[i+2])
            total_pts += calculate_pts(common)
    print(total_pts)
        
        
    