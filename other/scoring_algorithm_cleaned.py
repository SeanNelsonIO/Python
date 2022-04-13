


def procentual_proximity(
    source_data: list[list[float]], weights: list[int]
) -> list[list[float]]:

    

    
    data_lists: list[list[float]] = []
    for data in source_data:
        for i, el in enumerate(data):
            if len(data_lists) < i + 1:
                data_lists.append([])
            data_lists[i].append(float(el))

    score_lists: list[list[float]] = []
    
    for dlist, weight in zip(data_lists, weights):
        mind = min(dlist)
        maxd = max(dlist)

        score: list[float] = []
        
        if weight == 0:
            for item in dlist:
                try:
                    score.append(1 - ((item - mind) / (maxd - mind)))
                except ZeroDivisionError:
                    score.append(1)

        elif weight == 1:
            for item in dlist:
                try:
                    score.append((item - mind) / (maxd - mind))
                except ZeroDivisionError:
                    score.append(0)

        
        else:
            raise ValueError("Invalid weight of %f provided" % (weight))

        score_lists.append(score)

    
    final_scores: list[float] = [0 for i in range(len(score_lists[0]))]

    
    for i, slist in enumerate(score_lists):
        for j, ele in enumerate(slist):
            final_scores[j] = final_scores[j] + ele

    
    for i, ele in enumerate(final_scores):
        source_data[i].append(ele)

    return source_data
