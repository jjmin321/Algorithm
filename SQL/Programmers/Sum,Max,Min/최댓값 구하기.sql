/*
https://programmers.co.kr/learn/courses/30/lessons/59415

풀이 : 가장 최근에 들어온 동물을 구하기 위해서는 DATETIME중 최댓값을 가져오면 된다. 즉, SELECT MAX(DATETIME) FROM ANIMAL_INS 를 하면 DATETIME중 가장 큰 값을 가져온다.
*/

SELECT MAX(DATETIME) FROM ANIMAL_INS