def find_distinct(datastream, x):
    tmp_set = set()
    for i in range(0, len(datastream)):
        for y in range(x):
            tmp_set.add(datastream[i+y])
        if len(tmp_set) == x:
            print(tmp_set)
            return i+x
        tmp_set = set()
    return 0

with open('in1.txt') as f1:
    datastream = f1.read()
    
    # result 1
    print(find_distinct(datastream, 4))

    # result 2
    print(find_distinct(datastream, 14))

