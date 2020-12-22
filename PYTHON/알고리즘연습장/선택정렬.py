'''
가장 작은 요소를 선택해, 앞자리부터 위치를 결정
'''
def selection_sort(arr):
    min_position = 0
    for i in range(len(arr)): # 0, 1, 2, 3, 4, 5, 6
        for j in range(i, len(arr)):
            if arr[min_position] > arr[j] : min_position = j
        arr[i-1], arr[min_position] = arr[min_position], arr[i-1]
    return arr 

arr = [2, 4, 1, 3, 7, 6, 5]
print(selection_sort(arr))