import re
def test_patterns(text, patterns=[]):

    for pattern, desc in patterns:
        print 'Pattern %r (%s)\n' % (pattern, desc)
        print ' %r' % text
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[:s].count('\\')
            prefix = '.' * (s + n_backslashes)
            print ' %s%r' % (prefix, substr)
    print
    return
if __name__ == '__main__':
    test_patterns('bababaaaa',[('ba', "'a' followed by 'b'"),])