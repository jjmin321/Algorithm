/*
https://programmers.co.kr/learn/courses/30/lessons/59036

1. SELECT ANIMAL_ID, NAME FROM으로 테이블에서 아이디 값, 이름 값을 가지고 옴 
2. WHERE으로 아픈 동물들만 찾음 
3. ORDER BY로 오름차순 정렬함
*/

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID