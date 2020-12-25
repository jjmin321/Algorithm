'''
https://programmers.co.kr/learn/courses/30/lessons/12948

풀이 : 휴대폰 뒷 4자리를 제외한 값들을 *로 바꾼 후 리스트에 넣었습니다. 그리고 뒷 4자리를 리스트에 넣어 두 리스트를 합하여 문자열로 바꿔 반환하였습니다.

'''

def solution(phone_number):
    return ''.join(['*' for i in range(len(phone_number)-4)]+list(phone_number)[-4:])
phone_number = "01033334444"
print(solution(phone_number))
