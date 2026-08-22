def solution(picks, minerals):
    answer = 0
    sum_picks = sum(picks)
    max_minerals = min(len(minerals), sum_picks * 5)
    arr = []

    for i in range(0, max_minerals, 5):
        dia_cnt = 0
        iron_cnt = 0
        stone_cnt = 0

        mineral = minerals[i : i + 5]
        for m in mineral :
            if m == "diamond" :
                dia_cnt += 1
            elif m == "iron" :
                iron_cnt += 1
            elif m == "stone" :
                stone_cnt += 1

        worst = dia_cnt * 25 + iron_cnt * 5 + stone_cnt
        arr.append((worst, dia_cnt, iron_cnt, stone_cnt))

    arr.sort(key=lambda x: x[0], reverse=True)

    
    for worst, dia_cnt, iron_cnt, stone_cnt in arr :
        if picks[0] > 0 :
            answer += dia_cnt + iron_cnt + stone_cnt
            picks[0] -= 1
            
        elif picks[1] > 0 :
            answer += dia_cnt * 5 + iron_cnt + stone_cnt
            picks[1] -= 1
            
        elif picks[2] > 0 :
            answer += dia_cnt * 25 + iron_cnt * 5 + stone_cnt
            picks[2] -= 1
            
        else:
            break

    return answer