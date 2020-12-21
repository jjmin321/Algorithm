'''
두 개의 요소를 비교하며 큰 요소를 뒤에 위치하도록 교환
'''

def bubble_sort(arr):
    for i in range(len(arr)-1):
        arr[i:i+2] = sorted(arr[i:i+2])
    return arr

arr = [2, 4, 1, 7, 3, 5, 6]
print(bubble_sort(arr))
