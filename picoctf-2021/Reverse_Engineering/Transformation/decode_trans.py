'''
author : Febi Mudiyanto
date   : 6 - 04 - 2021

program ini dibuat dengan cara mempelajari proses encode dari picoCTF ke hasil encodenya. kemudian
dibuatlah decodenya.
'''


fp = open('enc','r')
flag = fp.readline()


def encode(flag):
    list_=[]
    for i in range(0,len(flag)-1,2):
        list_ += [chr((ord(flag[i]) << 8) + ord(flag[i+1]))]
    print(''.join(list_))

def decode(flag):
    list_=[]
    for i in range(len(flag)):
        temp = chr(ord(flag[i])-((ord(flag[i])>>8)<<8))
        list_ += chr(ord(flag[i])>>8)+temp
    print(''.join(list_))

decode(flag)
