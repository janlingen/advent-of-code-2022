from collections import defaultdict

with open('in1.txt') as f1:
    moves = f1.read().split('\n')
    result = 1
    move_count = 0
    value_time = [20, 60, 100, 140, 180, 220]
    sum_of_times = 0

    for i in moves:
        if i.split()[0] == "addx":
            result += int(i.split()[1])
            move_count += 1
            if move_count in value_time:
                sum_of_times += move_count * (result - int(i.split()[1]))
            move_count += 1
            if move_count in value_time:
                sum_of_times += move_count * (result - int(i.split()[1]))
        else:
            move_count += 1
            if move_count in value_time:
                sum_of_times += move_count * result

    print(sum_of_times)