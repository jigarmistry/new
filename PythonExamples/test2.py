import re
text = '_his is some text -- with punctuation.'
print text
print
patterns = [
(r'^(\_|w+)', 'word at start of string'),
(r'(\w+)\S*$', 'word at end, with optional punctuation'),
(r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
(r'(\w+t)\b', 'word ending with t'),
]
for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)  
    print 'Pattern %r (%s)\n' % (pattern, desc)
    print ' ', match.groups()
    print