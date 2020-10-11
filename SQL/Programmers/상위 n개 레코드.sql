/*
https://programmers.co.kr/learn/courses/30/lessons/59405

1. SELECT NAME FROM 으로 테이블의 이름 정보를 가져옴 
2. ORDER BY 로 오름차순 정렬함
3. 최상위 1개의 정보만 가지고 옴
*/

SELECT NAME FROM ANIMAL_INS 
ORDER BY DATETIME
LIMIT 1