'''
https://programmers.co.kr/learn/courses/30/lessons/42579

풀이 : all_kind에 set을 통해 장르의 종류를 도출합니다. 그리고 장르의 종류를 순회하며 genre_songs 에 장르의 종류를 Key로, 총 플레이 횟수와 모든 [노래 번호, 플레이 횟수]를 Value로 저장합니다.
    그 후 ranking_songs에 총 플레이 횟수가 높은 순서대로 저장하고 all_songs에 모든 [노래 번호, 플레이 횟수]를 랭킹이 높은 장르 순으로 리스트로 구분하여 저장합니다.
    그리고 장르 별 모든 노래를 노래의 플레이 횟수 순서로 정렬한 뒤 album에 추가합니다. 만약 장르 별 노래 수가 2개 이상이라면 2개를 추가합니다.
'''

from collections import deque

def songs_by_genre_ranking(genres, plays):
    all_kind = list(set(genres))
    genre_songs = {}
    while all_kind:
        kind = all_kind.pop()
        genre_songs[kind] = [0]
        for idx, (genre, play) in enumerate(zip(genres, plays)):
            if genre == kind:
                genre_songs[kind][0] += play
                genre_songs[kind].append([idx, play])
    ranking_songs = sorted(genre_songs.values(), key=lambda x:x[0], reverse=True)
    all_songs = []
    for i in ranking_songs:
        all_songs.append(i[1:])
    return all_songs

def pick_best_song(album, songs):
    songs_ranking = sorted(songs, key=lambda x:x[1], reverse=True)
    album.append(songs_ranking[0][0])
    if len(songs_ranking) >= 2:
        album.append(songs_ranking[1][0]) 
    
def solution(genres, plays):
    album = []
    all_songs = songs_by_genre_ranking(genres,plays)
    for songs in all_songs:
        pick_best_song(album, songs)
    return album