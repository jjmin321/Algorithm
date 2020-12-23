/*
https://programmers.co.kr/learn/courses/30/lessons/59039

풀이 : WHERE을 사용하여 NAME이 null인 ANIMAL_ID를 가져왔고 ORDER BY를 사용해 오름차순으로 정렬하였습니다.
*/

SELECT ANIMAL_ID FROM ANIMAL_INS
WHERE NAME is null
ORDER BY ANIMAL_ID