from collections import defaultdict

with open('in1.txt') as f1:
    commands = f1.read().split('\n')

    current_path = []
    dirs_size = defaultdict(lambda: 0)

    for i in commands:
        command_parts = i.split(' ')
        if command_parts[0] == '$':
            if command_parts[1] == 'cd':
                if command_parts[2] == '..':
                    current_path.pop()
                else:
                    if len(current_path) == 0:
                        current_path.append(command_parts[2])
                    else:
                        current_path.append(command_parts[2]+'/')
        else:
            dirs_size[''.join(current_path)] += 0
            try:
                value = int(command_parts[0])
                for x in range(len(current_path)+1):
                    dirs_size[''.join(current_path[:x])] += value
            except:
                pass

    result1 = 0
    for i, x in dirs_size.items():
        if x <= 100000:
            result1 += x

    #result 1
    print(result1)

    #result 2
    for i in sorted(dirs_size.values()):
        if i >= (30000000 - (70000000 - dirs_size['/'])):
            print(i)
            break


