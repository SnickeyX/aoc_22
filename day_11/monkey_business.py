CHALL_NUM = 2

class Monkey:
    def __init__(self, id, starting_items,  modulo, monkey1, monkey2, fun_info) -> None:
        self.id = id
        self.items_held = starting_items
        if(fun_info.count("+") > 0):
            self.is_multiply = False
            self.fun = lambda x : x + int(fun_info[-1])
        elif(fun_info.count("*") > 0):
            self.is_multiply = True
            if(fun_info[-1] == "old"):
               self.fun = lambda x : x * x
            else:
                self.fun = lambda x : x * int(fun_info[-1])
        self.modulo = modulo
        self.monkey1 = monkey1
        self.monkey2 = monkey2
        self.items_inspected = 0
    def inspect(self):
        self.items_inspected += len(self.items_held)
        print("Monkey: ", self.id, "items inspected: ", self.items_inspected, "items held: ", self.items_held)
        self.items_held = list(map(self.fun, self.items_held))
        print(self.items_held)
        if(CHALL_NUM == 1):
            self.items_held = list(map(lambda x: x  // 3, self.items_held))
    def test(self):
        result_if_true = []
        result_if_false = []
        for item in self.items_held:
            if(item % self.modulo == 0):
                result_if_true.append(item)
            else:
                result_if_false.append(item)
        self.items_held.clear()
        return result_if_true, result_if_false

def parse_input():
    with open("main_input.txt") as file:
        input = [line.strip() for line in file.readlines() if line.strip() != ""]
        monkey_content  = [input[i:i+6] for i in range(0,len(input), 6)]
        monkey_list = []
        monkey_big_mod = 1
        for monkey_info in monkey_content:
            monkey_id = int(monkey_info[0].split(" ")[1][0:-1])
            starting_items = [int(item.replace(",","")) for item in monkey_info[1].split(" ")[2:]]
            monkey_fun_info = monkey_info[2].split(" ")
            monkey_modulo = int(monkey_info[3].split(" ")[-1])
            monkey_pass_1 = int(monkey_info[4].split(" ")[-1])
            monkey_pass_2 = int(monkey_info[5].split(" ")[-1])
            monkey_big_mod *= monkey_modulo
            monkey_list.append(Monkey(monkey_id, starting_items, monkey_modulo, monkey_pass_1, monkey_pass_2, monkey_fun_info))
        return monkey_list, monkey_big_mod
        
if __name__ == "__main__":
    monkeys, monkey_mod = parse_input()
    if(CHALL_NUM == 1):
        round_num = 20
    else:
        round_num = 10000
    for round in range(round_num):
        for monkey in monkeys:
            monkey.inspect()
            result1, result2 = monkey.test()
            monkeys[monkey.monkey1].items_held += list([r % monkey_mod for r in result1])
            monkeys[monkey.monkey2].items_held += list([r % monkey_mod for r in result2])
               
    items_held_total = sorted([monkey.items_inspected for monkey in monkeys])
    print(items_held_total)
    print("solution to part: ", CHALL_NUM, " is: ", items_held_total[-1]*items_held_total[-2])