# register starts with a value 1
reg = 1
reg_in_cycles = []

crt_ptr = 0
crt_row = []

def crt_draw(crt_ptr, crt_row, reg):
    # draw row and reset it with the pointer
    if(crt_ptr <= reg + 1 and crt_ptr >= reg - 1):
        crt_row.append("#")
    else:
        crt_row.append(".")
    return crt_ptr + 1

# can be refactored 
with open("main_input.txt") as f:
    instructions = f.read().splitlines()
    for instruction in instructions:
        instruction = instruction.split(" ")
        if(instruction[0] == "noop"):
            if(len(crt_row) == 40):
                print("".join(crt_row))
                crt_row.clear()
                crt_ptr = 0
            crt_ptr = crt_draw(crt_ptr, crt_row, reg)
            reg_in_cycles.append(reg)
        else: 
            if(len(crt_row) == 40):
                print("".join(crt_row))
                crt_row.clear()
                crt_ptr = 0
            crt_ptr = crt_draw(crt_ptr, crt_row, reg)
            if(len(crt_row) == 40):
                print("".join(crt_row))
                crt_row.clear()
                crt_ptr = 0
            crt_ptr = crt_draw(crt_ptr, crt_row, reg)
            reg_in_cycles.append(reg)
            reg_in_cycles.append(reg)
            reg += int(instruction[1])
    # very last row
    print("".join(crt_row))
            
if __name__ == "__main__":
    #part1
    signal_strength_in_cycles = [(idx+1)*reg for idx,reg in enumerate(reg_in_cycles)]
    print("output for part1: ", sum([signal_strength_in_cycles[i-1] for i in range(20,len(signal_strength_in_cycles), 40)]))
    #part2 output is just printed in the console