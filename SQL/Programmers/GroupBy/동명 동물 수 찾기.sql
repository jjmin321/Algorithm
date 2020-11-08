/*
https://programmers.co.kr/learn/courses/30/lessons/59041

1. SELECT ANIMAL_TYPE, Count(NAME) as count로 동물의 종류, 동물의 수를 count변수로 가져옴 
2. GROUP BY NANE으로 동물의 이름 별로 동물의 수를 COUNT함
3. HAVING으로 count가 2이상인 값들만 가져옴
4. ORDER BY NAME으로 동물 이름에 따라 오름차순으로 정렬함
*/

SELECT NAME, COUNT(NAME) as COUNT 
FROM ANIMAL_INS 
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME