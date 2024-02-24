def solution(s):
    parte = []
    for i in range(0, len(s), 2):
        segmento = s[i:i + 2]
        if len(segmento) % 2 == 1:
            segmento += 'a'
        parte.append(segmento)
    return parte


s = "abcdefghijk"

print(solution(s))
