database = [
    ['A',  '1234'],
    ['B',  '4242'],
    ['C',  '7524'],
    ['D',  '9843']
]

username = raw_input('User name: ')
pin = raw_input('PIN code: ')

if [username, pin] in database:
    print 'Access granted'
else:
    print 'Access Denied'