'''
https://programmers.co.kr/learn/courses/30/lessons/12926

풀이 : s와 n의 값을 토대로 다른 알파벳으로 바꿉니다. 만약 알파벳의 끝에 도달하면 is_over_flow를 True로 바꾼 후, 다시 a부터 이동합니다.
'''

def solution(s, n):
    lower_s = s.lower()
    all_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    over_flow = len(all_alphabet)-n
    result = [' ' for i in range(len(s))]
    for idx, value in enumerate(lower_s):
        for alphabet_idx, alphabet in enumerate(all_alphabet):
            is_over_flow = True if alphabet_idx / over_flow >= 1 else False
            if value == alphabet:
                if is_over_flow:
                    result[idx] = all_alphabet[alphabet_idx - over_flow].upper() if s[idx].isupper() else all_alphabet[alphabet_idx - over_flow]
                    break
                else:
                    result[idx] = all_alphabet[alphabet_idx+n].upper() if s[idx].isupper() else all_alphabet[alphabet_idx+n]
                    break
    return ''.join(result)

s = 'ABC D'
n = 25
print(solution(s, n))