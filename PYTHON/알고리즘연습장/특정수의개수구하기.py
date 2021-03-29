from bisect import bisect_left, bisect_right

def count(array, x):
    left_index = bisect_left(array, x) 
    right_index = bisect_right(array, x)
    return right_index - left_index


array = list(map(int, input().split()))
x = int(input())
print(count(array, x))

