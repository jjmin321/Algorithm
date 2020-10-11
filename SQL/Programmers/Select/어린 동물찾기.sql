/*
https://programmers.co.kr/learn/courses/30/lessons/59037

1. SELECT ANIMAL_ID, NAME FROM 으로 테이블의 아이디, 이름 정보를 가져옴 
2. WHERE NOT으로 늙지 않은 동물 정보만 가져옴
3. ORDER BY 로 오름차순 정렬함
*/

SELECT ANIMAL_ID, NAME FROM ANIMAL_INS 
WHERE NOT INTAKE_CONDITION = 'Aged'
ORDER BY ANIMAL_ID