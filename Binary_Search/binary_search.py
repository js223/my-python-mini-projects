# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!

# naive search: scan entire list and ask if it's equal to the target
# if yes, return the index
# if no, then return -1
import math

def naive_search(mylst, target):
    for i in mylst:
        if target == i:
            return target
    return -1


def binary_search(mylst, target):
    
    while True:
        
        middle_index = math.floor(len(mylst)/2)
        middle_num = mylst[middle_index]
        new_list = []
        
        if len(mylst) == 1:
            if target != mylst[0]:
                return -1
        
        if target == middle_num:
            return target
        
        elif target > middle_num:
            for i in range(len(mylst)):
                if middle_num<mylst[i]:
                    new_list.append(mylst[i])
            mylst=new_list
            
        elif target < middle_num:
            for i in range(len(mylst)):
                if middle_num>mylst[i]:
                    new_list.append(mylst[i])
            mylst=new_list

sample_list = [1, 2, 5, 10, 21]
target_num = int(input("Type the number you want to find: "))

result = binary_search(sample_list,target_num)

if result == -1:
    print("Target number is not in the list.")
else:
    print(result)
