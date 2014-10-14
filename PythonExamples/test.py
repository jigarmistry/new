import re

text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print 'Found "%s" at %d:%d' % (text[s:e], s, e)
### 
for i in 'jigar':
    print i;
###    
list=['first',['jigar,mistry'],'second'];
###
for i in list:
    print i
###
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
    else:
        d[c] += 1
    return d
def print_hist(h):
    for c in h:
        print c, h[c]
h=histogram('pprrttabc');
print_hist(h);
###
#a=input("Enter key");
dict={'0':{'a','b'},'1':{'c','d'}};
print dict
###
import os
print os
###
d=tuple('j');
print d.count('j');
print d;
###







