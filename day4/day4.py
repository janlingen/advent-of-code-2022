def contains_eachother1(pair1, pair2):
    if int(pair1[0]) in range(int(pair2[0]),int(pair2[1]) +1) and int(pair1[1]) in range(int(pair2[0]),int(pair2[1]) +1):
        return True
    if int(pair2[0]) in range(int(pair1[0]),int(pair1[1]) +1) and int(pair2[1]) in range(int(pair1[0]),int(pair1[1]) +1):
        return True
    return False

def contains_eachother2(pair1, pair2):
    if int(pair1[0]) in range(int(pair2[0]),int(pair2[1]) +1):
        return True
    if int(pair1[1]) in range(int(pair2[0]),int(pair2[1]) +1):
        return True
    if int(pair2[0]) in range(int(pair1[0]),int(pair1[1]) +1):
        return True
    if int(pair2[1]) in range(int(pair1[0]),int(pair1[1]) +1):
        return True
    return False
    

with open('in1.txt') as f1:
    ids = [i.split('n') for i in f1.read().split('\n')]
    result1 = 0
    result2 = 0
    for i in ids:
        range1 = i[0].split(',')[0].split('-')
        range2 = i[0].split(',')[1].split('-')
        if contains_eachother1(range1, range2):
            result1 +=1
        if contains_eachother2(range1, range2):
            result2 +=1
    print(result1)
    print(result2)