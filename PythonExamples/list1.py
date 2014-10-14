def intersect(seq1, seq2):
    res = []             
    for x in seq1:       
        if x in seq2:    
            res.append(x)
    return res

s1 = "JIGAR"
s2 = "MISTRY"

print intersect(s1, s2)
s1 = [1,2,3,4,5]
s2 = [3,4,5,6,7]
print intersect(s1, s2)  