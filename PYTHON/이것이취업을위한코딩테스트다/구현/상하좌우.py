'''
N x N 크기의 정사각형 공간 위에 서 있다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상하좌우 방향으로 이동할 수 있으며,
시작 좌표는 항상 (1, 1)이다. N과 A가 이동할 계획서가 제공되면 N이 도착할 지점의 좌표를 출력하라. (단, 정사각형 공간을 벗어나는 움직임은 무시한다)
'''

N = int(input())
plans = input().split()
x, y = 1, 1

for plan in plans:
    if plan == 'L' and y > 1:
        y -= 1
    elif plan == 'R' and y < N:
        y += 1
    elif plan == 'U' and x > 1:
        x -= 1
    elif plan == 'D' and x < N:
        x += 1
print(x, y)