def binary_search(array, target, start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in array:
            if i > mid:
                total += i - mid
        if total > target: # 요청한 떡의 길이보다 많이 잘랐을 때 (오른쪽 탐색)
            answer = mid 
            start = mid+1
        elif total < target: # 요청한 떡의 길이보다 적게 잘랐을 때 (왼쪽 탐색)
            end = mid-1
        else: # 요청한 떡의 길이만큼 잘랐을 때
            return mid
    return answer 

n, m = map(int, input().split())
array = list(map(int, input().split()))
print(binary_search(array, m, 0, max(array)))
