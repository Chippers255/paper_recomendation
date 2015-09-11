
def intersect(paper_1, paper_2, top):
    p1 = paper_1[:top]
    p2 = paper_2[:top]

    count = 0
    for x in p1:
        for y in p2:
            if x[0] == y[0]:
                print x[0]
                count +=1

    return float(count)
# end def intersect

def union(paper_1, paper_2, top):
    p1 = paper_1[:top]
    p2 = paper_2[:top]

    total = []
    for x in p1:
        if x[0] not in total:
            total.append(x[0])

    for y in p2:
        if y[0] not in total:
            total.append(y[0])

    return float(len(total))
# end def union

def jaccard_similarity(paper_1, paper_2, top=20):
    return float(intersect(paper_1, paper_2, top) / union(paper_1, paper_2, top))
# end def jaccard_similarity

def jaccard_distance(paper_1, paper_2, top=20):
    return float(1 - jaccard_similarity(paper_1, paper_2, top))
# end def jaccard_distance