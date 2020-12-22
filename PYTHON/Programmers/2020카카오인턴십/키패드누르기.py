'''
https://programmers.co.kr/learn/courses/30/lessons/67256

풀이 : 2차원 배열에 번호를 등록시킨 뒤, 왼쪽 손의 현재 좌표, 오른쪽 손의 현재 좌표를 변수로 등록하여 숫자, 숫자의 좌표와 손의 좌표의 거리, 주로 사용하는 손을 기반으로 풀었습니다.

'''

def solution(numbers, hand):
    answer = ''
    phone = [[j for j in range(i, i+3)] for i in range(1, 10, 3)]
    phone.append(['*', 0, '#'])
    left_hand = [3, 0]
    right_hand = [3, 2]
    break_point = False
    for i in numbers:
        break_point = False
        for r_idx, r_val in enumerate(phone):
            for c_idx, c_val in enumerate(r_val):
                if i == c_val:
                    break_point = True
                    if i % 3 == 0 and i != 0: answer += 'R'; right_hand = [r_idx, c_idx]
                    elif i % 3 == 1: answer += 'L'; left_hand = [r_idx, c_idx]
                    else: 
                        left_distance = ((left_hand[0] - r_idx if left_hand[0] >= r_idx else r_idx - left_hand[0])
                                        +(left_hand[1] - c_idx if left_hand[1] >= c_idx else c_idx - left_hand[1]))
                        right_distance = ((right_hand[0] - r_idx if right_hand[0] >= r_idx else r_idx - right_hand[0]) 
                                        +(right_hand[1] - c_idx if right_hand[1] >= c_idx else c_idx - right_hand[1]))
                        if left_distance < right_distance: answer += 'L'; left_hand = [r_idx, c_idx]
                        elif right_distance < left_distance: answer += 'R'; right_hand = [r_idx, c_idx]
                        else: 
                            answer += hand[0].upper()
                            if hand == 'left': left_hand = [r_idx, c_idx]
                            else: right_hand = [r_idx, c_idx]
                    break
            if (break_point): break
    return answer

numbers, hand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"
print(solution(numbers, hand))
