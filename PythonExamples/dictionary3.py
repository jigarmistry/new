#------------------------------------------------------------------------------
#           Name: dictionary3.py
#         Author: Jigar Mistry
#  Last Modified: 04/08/2013
#    Description: This Python script demonstrates how to create and access a
#                 dictionary.
#------------------------------------------------------------------------------

print "";
print "";
array={0:(56,90),1:(67,89)}
print 'Available Keys:0,1'
a=int(input('Enter Key:'));
if a==0:
    print 'id:%s' % a
    print 'Height:%s\tWidth:%s' % array[a]
elif a==1:
    print 'id:%s' % a
    print 'Height:%s\tWidth:%s' % array[a]
else:
    print 'Invalid Choise';
raw_input( '\n\nPress Enter to exit...' )