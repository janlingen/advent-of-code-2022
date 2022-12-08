# [B]                     [N]     [H]
# [V]         [P] [T]     [V]     [P]
# [W]     [C] [T] [S]     [H]     [N]
# [T]     [J] [Z] [M] [N] [F]     [L]
# [Q]     [W] [N] [J] [T] [Q] [R] [B]
# [N] [B] [Q] [R] [V] [F] [D] [F] [M]
# [H] [W] [S] [J] [P] [W] [L] [P] [S]
# [D] [D] [T] [F] [G] [B] [B] [H] [Z]
#  1   2   3   4   5   6   7   8   9 
import re

def rearrange1 (spots, moves):
    for i in moves:
        for x in range(i[0]):
            spots[i[2]-1].append(spots[i[1] - 1].pop())

def rearrange2 (spots, moves):
    for i in moves:
        spots[i[2]-1].extend(spots[i[1]- 1][-i[0]:])
        del spots[i[1]- 1][-i[0]:]
        
with open('in1.txt') as f1:
    moves = [[int(s) for s in re.findall(r'\b\d+\b', i)] for i in f1.read().split('\n')]
    spots = [['D', 'H', 'N', 'Q', 'T', 'W', 'V', 'B'],
             ['D', 'W', 'B'],
             ['T', 'S', 'Q', 'W', 'J', 'C'],
             ['F', 'J', 'R', 'N', 'Z', 'T', 'P'],
             ['G', 'P', 'V', 'J', 'M', 'S', 'T'],
             ['B', 'W', 'F', 'T', 'N'],
             ['B', 'L', 'D', 'Q', 'F', 'H', 'V', 'N'],
             ['H', 'P', 'F', 'R'],
             ['Z', 'S', 'M', 'B', 'L', 'N', 'P', 'H']]

    #result 1
    # rearrange1(spots, moves)

    #result 2
    rearrange2(spots, moves)

    result = ''
    for i in spots:
        result += i[-1:][0]
    print(result)
