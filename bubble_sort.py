#bubble sort algorithm
#steps through a list, compares adjacent elements
#and swaps them if the first is bigger than the 
#latter
#example: unsorted list: [5, 1, 3, 4, 2]
#bubble sorted list: [1, 2, 3, 4, 5]

def bubble_sort(list: list):
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            list[i], list[i-1] = list[i-1], list[i]
        for a in range(len(list) - 1):
            pass
    return list

print(bubble_sort([5, 3, 2, 4, 1]))