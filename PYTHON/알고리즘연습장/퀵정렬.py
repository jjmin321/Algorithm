def quickSort(arr, start, end):
  if start >= end:
    return
  pivot = partition(arr, start, end)
  quickSort(arr, start, pivot-1)
  quickSort(arr, pivot+1, end)

def partition(arr, start, end):
  L, R = start, end
  while L < R:
    while arr[start] < arr[R]:
      R -= 1
    while L < R and arr[L] <= arr[start]:
      L += 1
    arr[L], arr[R] = arr[R], arr[L]
  arr[start], arr[L] = arr[L], arr[start]
  return L


arr = [7, 13, 2, 9, 25, 0, 44]
quickSort(arr, 0, len(arr)-1)
print(arr)