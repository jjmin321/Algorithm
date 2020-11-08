/*
https://programmers.co.kr/learn/courses/30/lessons/59040

1. SELECT ANIMAL_TYPE, Count(ANIMAL_TYPE) as count로 동물의 종류, 동물의 수를 count변수로 가져옴 
2. GROUP BY ANIMAL_TYPE으로 동물의 종류 별로 동물의 수를 COUNT함
3. ORDER BY ANIMAL_TYPE으로 동물의 종류명에 따라 오름차순으로 정렬함
*/

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) as count 
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE