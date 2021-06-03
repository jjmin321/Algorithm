'''
숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 주어질 때, 행 내에서 가장 낮은 숫자들 중 가장 숫자가 높은 카드를 뽑는 프로그램을 만드시오.
'''

N, M = map(int, input().split())

card = 0
for i in range(N):
    cards = list(map(int, input().split()))
    card = max(card, min(cards))
print(card)