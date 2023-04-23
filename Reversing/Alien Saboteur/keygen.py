#!/usr/bin/python

permut_byte_array = b'\x13\x19\x0f\x0a\x07\x00\x1d\x0e\x16\x10\x0c\x01\x0b\x1f\x18\x14\x08\x09\x1c\x1a\x21\x04\x22\x12\x05\x1b\x11\x20\x06\x02\x15\x17\x0d\x1e\x23\x03'
Xor_Key_byte_array = b'\x16\xb0\x47\xb2\x01\xfb\xde\xeb\x82\x5d\x5b\x5d\x10\x7c\x6e\x21\x5f\xe7\x45\x2a\x36\x23\xd4\xd7\x26\xd5\xa3\x11\xed\xe7\x5e\xcb\xdb\x9f\xdd\xe2'
Solution_Compare_String = b'\x65\x5d\x77\x4a\x33\x40\x56\x6c\x75\x37\x5d\x35\x6e\x6e\x66\x36\x6c\x36\x70\x65\x77\x6a\x31\x79\x5d\x31\x70\x7f\x6c\x6e\x33\x32\x36\x36\x31\x5d'

PermutDict = {}
for i in range(len(permut_byte_array)) :
    PermutDict[permut_byte_array[i]] = i


def Xor(bytes_array_a,value) :
    return bytes(a^value for a in bytes_array_a)

def swapbytes(byte_array,i,j) :
    res = b''
    for c in range(len(byte_array)) :
        if c == i :
            res += bytearray( [byte_array[j]] )
        elif c == j :
            res += bytearray( [byte_array[i]] )
        else :
            res += bytearray( [byte_array[c]] )
    return res

def PermutByteArray(bytes_array) :
    byte_res = bytes_array
    for i in range(36)[::-1] :
        byte_res = swapbytes(byte_res,i,permut_byte_array[i])
    return byte_res

for i in range(36) :
    Solution_Compare_String = PermutByteArray(Xor(Solution_Compare_String,Xor_Key_byte_array[35-i]))
    print(Solution_Compare_String)
