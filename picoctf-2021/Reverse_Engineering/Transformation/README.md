## Transformation

### Deskripsi

I wonder what this really is... [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc) 
```
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

```

### Steps
1. Download file *env*
```
wget https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc
```
2. pastikan satu folder dengan file [*decode_trans.py*](https://github.com/febimudiyanto/ctf-write-ups/blob/d3ececc86f850dbec3a08de578649a435fc5cc21/picoctf-2021/Reverse_Engineering/Transformation/decode_trans.py)
note: silahkan pelajari bagaimana picoCTF di encode, dan kemudian bagaimana saya membuat decodernya.

3. run program python tersebut.

flag:
```
picoCTF{16_bits_inst34d_of_8_d52c6b93}
```
