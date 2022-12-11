with open('in1.txt') as f1:
    tree_rows = f1.read().split('\n')
    grid = []
    
    for i in tree_rows:
        grid.append([int(x) for x in i])

    result = (len(grid) * 2) + (len(grid[0]) * 2 - 4)
    for i in range(1, len(grid)- 1):
        for x in range(1, len(grid[0])-1):
            row = grid[i]
            column = [grid[y][x] for y in range(len(grid))]
            if grid[i][x] > max(row[x+1:]):
                result += 1
            elif grid[i][x] > max(row[:x]):
                result += 1
            elif grid[i][x] > max(column[:i]):
                result += 1
            elif grid[i][x] > max(column[i+1:]):
                result += 1

    scenic_score = 0
    counts = []
    for i in range(1, len(grid)- 1):
        for x in range(1, len(grid[0])-1):
            current_score = []
            row = grid[i]
            column = [grid[y][x] for y in range(len(grid))]
            current_adder = 0
            for y in row[x+1:]:
                if grid[i][x] > y:
                    current_adder += 1
                else:
                    current_adder += 1
                    break
            current_score.append(current_adder)
            current_adder = 0
            for y in row[:x][::-1]:
                if grid[i][x] > y:
                    current_adder += 1
                else:
                    current_adder += 1
                    break
            current_score.append(current_adder)
            current_adder = 0
            for y in column[:i][::-1]:
                if grid[i][x] > y:
                    current_adder += 1
                else:
                    current_adder += 1
                    break
            current_score.append(current_adder)
            current_adder = 0
            for y in column[i+1:]:
                if grid[i][x] > y:
                    current_adder += 1
                else:
                    current_adder += 1
                    break
            current_score.append(current_adder)
            current_adder = 0
            counts.append(current_score)
            current_score = []
    results = []
    for i in counts:
        tmp_res = 1
        for x in i:
            tmp_res *= x
        results.append(tmp_res)

    print(result)
    
    print(max(results))    
