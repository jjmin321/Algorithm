'''
https://programmers.co.kr/learn/courses/30/lessons/12948

풀이 : 

'''

def solution(phone_number):
    return ''.join(['*' for i in range(len(phone_number)-4)]+list(phone_number)[-4:])
phone_number = "01033334444"
print(solution(phone_number))
