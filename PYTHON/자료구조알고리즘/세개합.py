
def solution(arr):
    min = sum(arr)
    for i in range(len(arr)-2):
        if min > sum(arr[i:i+3]): min = sum(arr[i:i+3])
    return min

arr = [4, 5, 1, 2, 3, 7, 3, 2, 1, 8]
print(solution(arr))