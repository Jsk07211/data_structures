from sorts.sorting_algorithm import SortingAlgorithm
import random

def rand_list():
    rand = []
    max = random.randint(3, 5)

    for i in range(max):
        rand.append(random.randint(1, 10))
    return rand

def print_sort(nums, type):
    sorter.change_type(type)
    print(nums)
    sorter.sort(nums)
    print(nums)


sorter = SortingAlgorithm("bubble")

print("### BUBBLE SORT ###")
print_sort(rand_list(), "bubble")
print("\n### SELECTION SORT ###")
print_sort(rand_list(), "select")
print("\n### INSERTION SORT ###")
print_sort(rand_list(), "insert")
print("\n### MERGE SORT ###")
print_sort(rand_list(), "merge")