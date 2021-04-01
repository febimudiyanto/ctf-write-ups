'''
ROT13 Decryption
author : febi mudiyanto
date   : 1-April-2021

'''


def rot13(chiperchar):
  '''
  input: chipertext a-zA-Z0-9 and symbolic
  return: the decryption of chipertext
  
  read more about ROT13 --> https://en.wikipedia.org/wiki/ROT13
  '''
  
  list1="ABCDEFGHIJKLM"
  list2="NOPQRSTUVWXYZ"
  str_=""
  
  for i in range(len(chiperchar)):
      a= chiperchar[i]
      if a.isalpha():
          a=a.upper()

      if a in list1:
          char = list2[list1.index(a)]
      elif a in list2:
          char = list1[list2.index(a)]
      else:
          char = chiperchar[i]

      if chiperchar[i].isalpha() and chiperchar[i].islower():
          char=char.lower()

      str_+=char
  return str_



chiperchar = input("masukkan chiperchar :")
flag = rot13(chiperchar)
print(flag)
