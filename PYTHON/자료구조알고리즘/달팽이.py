arr = [[0 for column in range(5)] for row in range(5)]
# 우하좌상으로 움직일 수 있게 변화량 배열 생성 
d_row = [0, 1, 0, -1] # 행의 변화량 
d_column = [1, 0, -1, 0] # 열의 변화량 

# 변화량의 방향이 우하좌상으로 움직일 수 있게 하는 변수 선언
direction = 0 # 방향을 표시하는 변수, 오른쪽 이동이 시작이니 0으로 초기화 
row, column = 0, 0 # 현재 좌표 0, 0에서 시작

# 행렬에 숫자를 채우는 과정을 반복문으로 작성
# 행렬에 숫자가 가득 찰 때까지 반복
cnt = 1 # 행렬에 채울 숫자 
N = 5 # 한 변의 길이 
total = N * N

while cnt <= total :
    # 현재 위치에 숫자 채워넣고 이동함. 
    arr[row][column] = cnt
    # 다음 위치 설정, 현재위치에서 이동변화량을 더하면 됨
    next_row = row + d_row[direction]
    next_column = column + d_column[direction] 

    # 이동했는데 범위를 벗어나거나, 이미 다른 숫자가 채워져있으면 방향 전환하고 이동
    if next_row < 0 or next_row >= N or next_column < 0 or next_column >= N or arr[next_row][next_column] > 0:
        # 방향 전환하고 이동 
        direction = (direction + 1) % 4
        next_row = row + d_row[direction]
        next_column = column + d_column[direction]
    
    # 다음 좌표값을 구했으니, 현재 좌표를 다음 좌표로 설정 
    row = next_row 
    column = next_column 
    cnt += 1
for i in arr:
    print(i)