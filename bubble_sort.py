#bubble sort algorithm
#steps through a list, compares adjacent elements
#and swaps them if the first is bigger than the 
#latter
#example: unsorted list: [5, 1, 3, 4, 2]
#bubble sorted list: [1, 2, 3, 4, 5]

def bubble_sort(list: list):
    for i, v in enumerate(list):
        if list[i] > list[i+1]:
            list[i+1].append(v)
            list[i].append(v[i+1])
    return list

print(bubble_sort([5, 1, 3, 4, 2]))