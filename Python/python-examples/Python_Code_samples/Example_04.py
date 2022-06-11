f = open('data.txt', 'w') # Make a new file in output mode ('w' is write)
f.write('Hello\n') # Write strings of characters to it
f.write('world\n') # Return number of items written in Python 3.X
f.close()
f = open('data.txt') # 'r' (read) is the default processing mode
text = f.read() # Read entire file into a string
print(text)
for line in open('data.txt'): print(line)

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8) # Create packed binary data
print(packed) # 10 bytes, not objects or text
file = open('data.bin', 'wb') # Open binary output file
file.write(packed) # Write packed binary data
file.close()

data = open('data.bin', 'rb').read() # Open/read binary data file
print(data) # 10 bytes, unaltered
data[4:8] # Slice bytes in the middle
list(data) # A sequence of 8-bit bytes
[0, 0, 0, 7, 115, 112, 97, 109, 0, 8]
print(struct.unpack('>i4sh', data)) # Unpack into objects again

x = 1 # 1 decimal is 0001 in bits
print(x << 2) # Shift left 2 bits: 0100
print(x | 2) # Bitwise OR (either bit=1): 0011
print(x & 1) # Bitwise AND (both bits=1): 0001

L = [1, 2, 1, 3, 2, 4, 5]
print(L)
print(set(L)
)
print(list(set(L)))


print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))# Find list differences
print(set('abcdefg') - set('abdghij')) # Find string differences
print(set('spam') - set(['h', 'a', 'm'])) # Find differences, mixed
print(set(dir(bytes)) - set(dir(bytearray))) # In bytes but not bytearray
print(set(dir(bytearray)) - set(dir(bytes)))

      
