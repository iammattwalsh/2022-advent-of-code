class Monkey:
    def __init__(self, id, items, operation, test, monkey_list) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.num_inspected = 0
        self.list = monkey_list

    def inspect(self) -> None:
        for item in self.items:
            match self.operation.val:
                case 'old':
                    val = item.worry
                case _:
                    val = int(self.operation.val)
            match self.operation.mode:
                case '+':
                    item.worry += val
                case '-':
                    item.worry -= val
                case '*':
                    item.worry *= val
                case '/':
                    item.worry /= val
            item.worry //= 3
            self.num_inspected += 1

    def throw(self) -> None:
        while len(self.items) > 0:
            item = self.items[0]
            if item.worry % self.test.val == 0:
                self.list[self.test.true].items.append(self.items.pop(0))
            else:
                self.list[self.test.false].items.append(self.items.pop(0))
    
    def take_turn(self) -> None:
        self.inspect()
        self.throw()

class Item:
    def __init__(self, worry) -> None:
        self.worry = int(worry)

class Operation:
    def __init__(self, mode, val) -> None:
        self.mode = mode
        self.val = val

class Test:
    def __init__(self, val, true, false) -> None:
        self.val = int(val)
        self.true = int(true)
        self.false = int(false)



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]

    monkeys = []
    monkey = {
        'id': 0,
        'items': [],
        'op_mode': '',
        'op_val': '',
        'test_mode': '',
        'test_val': '',
        'test_true': '',
        'test_false': '',
    }

    for line in lines:
        build = False
        loc = line.find(':')
        split_line = line.split()
        if 'Monkey' in line:
            monkey['id'] = int(line[-2])
        elif 'Starting items:' in line:
            monkey['items'] = line[loc + 2:].split(', ')
        elif 'Operation: ' in line:
            monkey['op_mode'] = split_line[-2]
            monkey['op_val'] = split_line[-1]
        elif 'Test: ' in line:
            monkey['test_val'] = split_line[-1]
        elif 'If true: ' in line:
            monkey['test_true'] = split_line[-1]
        elif 'If false: ' in line:
            monkey['test_false'] = split_line[-1]
            build = True

        if build == True:
            new_monkey = Monkey(
                id=monkey['id'],
                items=[Item(item) for item in monkey['items']],
                operation=Operation(
                    monkey['op_mode'],
                    monkey['op_val']
                ),
                test=Test(
                    monkey['test_val'],
                    monkey['test_true'],
                    monkey['test_false']
                ),
                monkey_list=monkeys
            )
            monkeys.append(new_monkey)

    num_loops = 20

    for _ in range(num_loops):
        for monkey in monkeys:
            monkey.take_turn()
    
    def sort_key(monkey):
        return monkey.num_inspected
    
    monkeys.sort(reverse=True, key=sort_key)
    print(monkeys[0].num_inspected * monkeys[1].num_inspected)