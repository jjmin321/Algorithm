/*
https://programmers.co.kr/learn/courses/30/lessons/59412

1. SELECT HOUR(DATETIME) as hour, Count(HOUR(DATETIME)) as COUNT로 입양 시간과, count 수를 셈
2. GROUP BY hour로 시간 별로 각각 카운트함
3. HAVING으로 09:00 시부터 19:59까지만 가지고 오게 필터링함
4. ORDER BY HOUR로 시간에 따라 오름차순으로 정렬함
*/

SELECT HOUR(DATETIME) as hour, COUNT(HOUR(DATETIME)) as COUNT
FROM ANIMAL_OUTS
GROUP BY hour
HAVING hour >= 9 AND hour <= 20
ORDER BY HOUR