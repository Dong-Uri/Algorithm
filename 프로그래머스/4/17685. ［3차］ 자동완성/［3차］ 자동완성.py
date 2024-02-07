def solution(words):
    answer = 0
    i = 0
    while words:
        word_dict = {}
        for word in words:
            key = word[:i + 1]
            if key in word_dict.keys():
                word_dict[key].append(word)
            else:
                word_dict[key] = [word]
        words = []
        for key, value in word_dict.items():
            if len(value) == 1:
                answer += len(key)
                continue
            for v in value:
                if v == key:
                    answer += len(key)
                    continue
                words.append(v)
        i += 1
            
    return answer