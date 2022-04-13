def mixed_keyword(key: str = "college", pt: str = "UNIVERSITY") -> str:
    
    key = key.upper()
    pt = pt.upper()
    temp = []
    for i in key:
        if i not in temp:
            temp.append(i)
    len_temp = len(temp)
    
    alpha = []
    modalpha = []
    for j in range(65, 91):
        t = chr(j)
        alpha.append(t)
        if t not in temp:
            temp.append(t)
    
    r = int(26 / 4)
    
    k = 0
    for _ in range(r):
        s = []
        for j in range(len_temp):
            s.append(temp[k])
            if not (k < 25):
                break
            k += 1
        modalpha.append(s)
    
    d = {}
    j = 0
    k = 0
    for j in range(len_temp):
        for m in modalpha:
            if not (len(m) - 1 >= j):
                break
            d[alpha[k]] = m[j]
            if not k < 25:
                break
            k += 1
    print(d)
    cypher = ""
    for i in pt:
        cypher += d[i]
    return cypher


print(mixed_keyword("college", "UNIVERSITY"))
