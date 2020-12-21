arr = [1, 2, 3]
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j: continue
        for k in range(len(arr)):
            if i == k or j == k: continue
            print(arr[i], arr[j], arr[k])