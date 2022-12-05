import re

def add_boxes_to_crates(line, crates): 
    for idx, char in enumerate(line):
        if char.isalnum():
            crates[idx // 4].append(char)   
    
def deal_with_move(line,crates):
    setting = re.findall(r'\d+',line)
    for i in range(int(setting[0])):
        crates[int(setting[2]) - 1].append(crates[int(setting[1]) - 1].pop())
        
def deal_with_mul_move(line, crates):
    setting = re.findall(r'\d+',line)
    # get crates to move
    payload = crates[int(setting[1]) - 1][-int(setting[0]):]
    # update crate
    crates[int(setting[1]) - 1] = crates[int(setting[1]) - 1][:-int(setting[0])]
    # add payload to new crate
    crates[int(setting[2]) - 1] += payload

with open("crate.txt") as f: 
    create_and_commands = [line for line in f]
    chall_num = 2
    # initialize the different crates
    crates = [ [] for i in range(len(create_and_commands[0].split(" ")) // 3)] 
    for line in create_and_commands:
        if(line.startswith("move")):
            if(chall_num == 1):
                deal_with_move(line, crates)
            else:
                deal_with_mul_move(line,crates)
        elif("[" in line):
            add_boxes_to_crates(line, crates)
        elif(line == "\n"):
            for crate in crates:
                crate.reverse()
    sol = "" 
    for crate in crates:
        sol = sol + crate[-1]
    print(sol)