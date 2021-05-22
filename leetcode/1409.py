def processQueries(queries, m):
    p = [i for i in range(1,m+1)]
    res = []
    for i in queries:
        a = p.index(i)
        res.append(a)
        p.pop(a)
        p.insert(0, i)
    return res

print(processQueries([3,1,2,1],5))