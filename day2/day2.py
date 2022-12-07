def calc_points1(pair):
    if pair[0] == 'A':
        if pair[2] == 'X':
            return 4
        elif pair[2] == 'Y':
            return 8
        else:
            return 3
    elif pair[0] == 'B':
        if pair[2] == 'X':
            return 1
        elif pair[2] == 'Y':
            return 5
        else:
            return 9
    else:
        if pair[2] == 'X':
            return 7
        elif pair[2] == 'Y':
            return 2
        else:
            return 6

def calc_points2(pair):
    if pair[0] == 'A':
        if pair[2] == 'X':
            return 3
        elif pair[2] == 'Y':
            return 4
        else:
            return 8
    elif pair[0] == 'B':
        if pair[2] == 'X':
            return 1
        elif pair[2] == 'Y':
            return 5
        else:
            return 9
    else:
        if pair[2] == 'X':
            return 2
        elif pair[2] == 'Y':
            return 6
        else:
            return 7


with open('in1.txt') as f:
    games = f.read().split('\n')

# result 1
print(sum(map(calc_points1, games)))

# result 2
print(sum(map(calc_points2, games)))