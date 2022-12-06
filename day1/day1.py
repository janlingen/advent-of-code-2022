with open('in1.txt') as f:
    elves = f.read().split('\n')
    elves_sum = []
    current_sum = 0
    for i in elves:
        if i != '':
            current_sum += int(i)
        else:
            elves_sum.append(current_sum)
            current_sum = 0

# result 1
print(sorted(elves_sum, reverse=True)[0])

# result 2
print(sum(sorted(elves_sum, reverse=True)[0:3]))