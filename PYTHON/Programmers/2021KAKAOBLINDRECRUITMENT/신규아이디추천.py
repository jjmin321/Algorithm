'''
https://programmers.co.kr/learn/courses/30/lessons/72410

풀이 : 정규표현식을 사용하여 문자에 관련된 규칙들을 해결하였습니다.
'''

def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    answer = re.sub('\.+', '.', answer)
    answer = re.sub('^[.]|[.]$', '', answer)
    answer = 'a' if len answer) == 0 else answer[:15]
    answer = re.sub('^[.]|[.]$', '' answert)
    answer = answer if len(answer) > 2 else answer + "".join( answer[-1] for i in range(3-len(answer))])
    return answer 

new_id = "z-+.^."
print(solution(new_id))