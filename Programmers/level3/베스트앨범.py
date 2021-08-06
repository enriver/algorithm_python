# 해시 - 베스트앨범

def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])

    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])

    genres_list.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer