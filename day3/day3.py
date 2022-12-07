def intersection_lst_item(lst):
    return list(set(lst[0:len(lst)//2]).intersection(lst[len(lst)//2:]))[0]

def intersection_lsts_rucksacks(rucksack1, rucksack2, rucksack3):
    return list(set(rucksack1).intersection(rucksack2).intersection(rucksack3))[0]

def calc_item_value(item):
    if ord(item) > 97:
        return ord(item) - 96
    else: 
        return ord(item) - 38


with open('in1.txt') as f1:
    rucksacks1 = f1.read().split('\n')
    shared_items = [intersection_lst_item(i) for i in rucksacks1]

with open('in2.txt') as f2:
    rucksacks2 = f2.read().split('\n')
    result = 0
    for i in range(0, len(rucksacks2), 3):
        result += calc_item_value(intersection_lsts_rucksacks(rucksacks2[i], rucksacks2[i+1], rucksacks2[i+2]))


    
#result 1
print(sum(map(calc_item_value, shared_items)))

#result 2
print(result)