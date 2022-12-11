# Day 11
import math

class Monkey():
    name = 0
    items = []
    operation = []
    test = 0
    test_true = 0
    test_false = 0
    inspections = 0

def main():

    count = 0
    monkeys = []
    file = open("Data.txt", "r")
    
    # Monkey setup
    while True:
        line = file.readline()
        line = line.replace("\n","")
        if not line:
            break
        # Name
        monkey = Monkey()
        monkey.name = count

        # Items
        these_items = []
        line = file.readline()
        line = line.replace("\n","")
        sec = line.split(":")
        items = sec[1].split(",")
        for item in items:
            these_items.append(int(item))
        monkey.items = these_items
        # Operation
        line = file.readline()
        line = line.replace("\n","")
        sec = line.split(": ")
        monkey.operation = sec[1].split(" ")

        # Test
        line = file.readline()
        line = line.replace("\n","")
        sec = line.split(":")
        test = sec[1].split(" ")
        monkey.test = int(test[3])

        # True
        line = file.readline()
        line = line.replace("\n","")
        sec = line.split(": ")
        test = sec[1].split(" ")
        monkey.test_true = int(test[3])

        # False
        line = file.readline()
        line = line.replace("\n","")
        sec = line.split(": ")
        test = sec[1].split(" ")
        monkey.test_false = int(test[3])

        line = file.readline()
        line = line.replace("\n","")
        monkeys.append(monkey)
        count = count + 1
    modifier = 1

    for monkey in monkeys:
        modifier *= monkey.test

    for i in range(10000):
        for i in range(0, len(monkeys)):

            monkey = monkeys[i]
            
            for item in monkey.items:
                monkey.inspections = monkey.inspections + 1

                new_item = calculate(item, monkey.operation)
                new_item = new_item % modifier;
                new_item = math.floor(new_item)

                if new_item%monkey.test == 0:
                    monkeys[monkey.test_true].items.append(new_item)
                else:
                    monkeys[monkey.test_false].items.append(new_item)

            monkey.items = []
            monkeys[i] = monkey
    
    for i in range(0, len(monkeys)):
            monkey = monkeys[i]
            print("Monkey ", monkeys[i].name, " inspected items ", monkeys[i].inspections, " times.")
    print("Kiitos ohjelman käytöstä!")
    
def calculate(item, operation):
    if operation[3] == "+":
        if operation[2] == "old" and operation[4] == "old":
            new_item = item + item
        elif operation[2] == "old":
            new_item = item + int(operation[4])
        elif operation[4] == "old":
            new_item = item + int(operation[2])
        else:
            new_item = int(operation[2]) + int(operation[4])
    else:
        if operation[2] == "old" and operation[4] == "old":
            new_item = item * item
        elif operation[2] == "old":
            new_item = item * int(operation[4])
        elif operation[4] == "old":
            new_item = item * int(operation[2])
        else:
            new_item = int(operation[2]) * int(operation[4])
    return new_item
main()
