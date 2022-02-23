import time
from random import randint as ri

def how_long_sort(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        x = func(*args, **kwargs)
        finish = time.time()
        time_sec = finish - start
        print(f'Sortowanie trwało {time_sec} sekund.')

        return x
    return wrapper

@how_long_sort
def bubble_sort(arr : list) -> list:
    N = len(arr)
    for j in range(1,N):
        for i in range(N-1):
            if arr[i] > arr[i+1]:
                pom = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = pom
    return  arr

@how_long_sort
def sort_function(arr : list) -> list:
    arr.sort()
    return arr

@how_long_sort
def sorted_function(arr : list) -> list:
    return sorted(arr)

def check_sorted_lists(l1, l2, l3):
    if l1 == l2 == l3:
        print('Lista1 == Lista2 == Lista3')

list_to_sort = [ri(1,10000) for i in range(10000)]

list_to_sort_2 = list_to_sort.copy()
list_to_sort_3 = list_to_sort.copy()

sorted_list = bubble_sort(list_to_sort)
print(sorted_list)

sorted_list_2 = sort_function(list_to_sort_2)
print(sorted_list_2)

sorted_list_3 = sorted_function(list_to_sort_3)
print(sorted_list_3)

check_sorted_lists(sorted_list, sorted_list_2, sorted_list_3)

