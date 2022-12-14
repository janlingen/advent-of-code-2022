def move_tail1(h_x, h_y, t_x, t_y):
    #. . . H
    #. T . .
    #s . . .
    if not has_collision(h_x, h_y, t_x, t_y):
        diff_x = 0 if h_x == t_x else (h_x - t_x) / abs(h_x - t_x)
        diff_y = 0 if h_y == t_y else (h_y - t_y) / abs(h_y - t_y)
        return (t_x + diff_x, t_y + diff_y)
    return (t_x, t_y)

def has_collision(h_x, h_y, t_x, t_y):
    if abs(h_x - t_x) <= 1 and abs(h_y - t_y) <= 1:
        return True
    else:
        return False

with open('in1.txt') as f1:
    moves = f1.read().split('\n')
    visited1 = set()
    h_x , h_y = 0, 0
    t_x, t_y = 0, 0
    visited1.add((t_x, t_y))

    for i in moves:
        for step in range(int(i[2:])):
            if i[0] == 'R':
                h_x += 1
                t_x, t_y = move_tail1(h_x, h_y, t_x, t_y)
            elif i[0] == 'L':
                h_x -= 1
                t_x, t_y = move_tail1(h_x, h_y, t_x, t_y)
            elif i[0] == 'U':
                h_y += 1
                t_x, t_y = move_tail1(h_x , h_y, t_x, t_y)
            elif i[0] == 'D':
                h_y -= 1
                t_x, t_y = move_tail1(h_x , h_y, t_x, t_y)
            visited1.add((t_x, t_y))

    visited2 = set()
    knots = [[0, 0] for _ in range(10)]
    visited1.add((0, 0))

    for i in moves:
        for step in range(int(i[2:])):
            knots[0][0] += 1 if i[0] == "R" else -1 if i[0] == "L" else 0
            knots[0][1] += 1 if i[0] == "U" else -1 if i[0] == "D" else 0
            for x in range(9):
                head = knots[x]
                tail = knots[x + 1]
                diff_x = head[0] - tail[0]
                diff_y  = head[1] - tail[1]
                if not has_collision(head[0], head[1], tail[0], tail[1]):
                    if diff_x == 0:
                        tail[1] += diff_y  // 2
                    elif diff_y  == 0:
                        tail[0] += diff_x // 2
                    else:
                        tail[0] += 1 if diff_x > 0 else -1
                        tail[1] += 1 if diff_y > 0 else -1

            visited2.add(tuple(knots[-1]))

    # result 1
    print(len(visited1))

    # result 2
    print(len(visited2))
