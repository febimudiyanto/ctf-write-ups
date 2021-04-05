## Nice netcat

```
nc mercury.picoctf.net 21135

```
hint: ascii

### steps
1. install netcat
2. simpan output dari nc ke file flag.txt
```
nc mercury.picoctf.net 21135 > flag.txt
```
3. decode angka ke ascii menggunakan program python.
silahkan gunakan yang sudah saya buat [python ascii decode](https://github.com/febimudiyanto/ctf-write-ups/blob/cde885a257872821818bb8edfb68ba91fb8a89ab/picoctf-2021/Nice_netcat/decode_ascii.py)

note: *decode_ascii.py* dan *flag.txt* harus satu folder

flag:
```
picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}
```
