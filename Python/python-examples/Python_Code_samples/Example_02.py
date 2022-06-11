#Object type Example literals/creation
#Numbers 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
#Strings 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
#Lists [1, [2, 'three'], 4.5], list(range(10))
#Dictionaries {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
#Tuples (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
#Files open('eggs.txt'), open(r'C:\ham.bin', 'wb')
#Sets set('abc'), {'a', 'b', 'c'}
#Other core types Booleans, types, None
#Program unit types Functions, modules, classes (Part IV, Part V, Part VI)
#Implementation-related types Compiled code, stack tracebacks (Part IV, Part VII)
L1 = [1,2]
L1= L1.append(L1)
print(L1)
#List Operations
S = 'shrubbery'
L = list(S) # Expand to a list: [...]
print( L)
L[1] = 'c' # Change it in place
print(''.join(L))

B = bytearray(b'spam') # A bytes/list hybrid (ahead)
B.extend(b'eggs') # 'b' needed in 3.X, not 2.X
print(B) # B[i] = ord(c) works here too

print(B.decode()) # Translate to normal string

S = 'Spam'
S.find('pa') # Find the offset of a substring in S
print(S)
print(S.isalpha())
print(S.upper())
s2=S.replace('pa', 'XYZ') # Replace occurrences of a string in S with another
print(s2)
line = 'aaa,bbb,ccccc,dd'
print(line.split(','))
line = 'aaa,bbb,ccccc,dd\n'
print(line.split(','))
print(line.rstrip().split(','))
print('{:,.2f}'.format(296999.2567) )# Separators, decimal digits

#print('{.2f | 05d}'.format(3.14159) )# Digits, padding, signs
print(dir(S))
print(S[1:])

