/*
https://programmers.co.kr/learn/courses/30/lessons/59404

1. SELECT ANIMAL_ID, NAME, DATETIME FROM 으로 테이블의 아이디, 이름, 보호 시작일 정보를 가져옴 
2. ORDER BY NAME, DATETIME DESC로 이름으로 오름차순 정렬 후, 이름이 같을 경우 보호 시작일을 내림차순으로 정렬함
*/

SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC