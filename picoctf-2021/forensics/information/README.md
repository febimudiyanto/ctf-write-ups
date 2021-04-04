## information

### Deskripsi

kita diminta untuk menemukan suatu flag dari file [cat.jpg](https://mercury.picoctf.net/static/e5825f58ef798fdd1af3f6013592a971/cat.jpg)


## Steps
1. Download dulu seperti biasa dengan wget
2. buka dulu gambarnya apakah ada informasi yang bisa kita dapat.
3. ada dugaan flag disembunyikan, jadi saya gunakan strings

```
strings cat.jpg |grep picoCTF
```
4. karena tidak membuahkan hasil, saya gunakan *exiftool*

```
exiftool cat.jpg
```
5. saya melihat ada yang mencurigakan yaitu bagian informasi 

```
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```
6. decode dengan base64 https://www.base64decode.org/

flag:
```
picoCTF{the_m3tadata_1s_modified}
```
