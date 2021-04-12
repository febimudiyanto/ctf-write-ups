## Matryoshka doll

### Deskripsi

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/b6205dd933ec01c022c4e6acbdf11116/dolls.jpg)


### Steps

1. Download the image
2. coba buka dengan eog, dan ternyata tidak bisa terbuka
3. cek kateogri file nya

```
file dolls.jpg

>> dolls.jpg: PNG image data, 594 x 1104, 8-bit/color RGBA, non-interlaced
```
rubah extensinya dengan png
4. cek strings nya, dan ternyata terdapat file lagi didalamnya
```
strings dolls.png |tail
```
outputnya:
```
f8<y
nTJ	U
tqe#^
:E2dT
4E6:
Fir1
C=%b
 	flL^9]
base_images/2_c.jpgUT
O`ux

```
ket: artinya tedapat file lain di file tersebut.
kita gunakan foremost
5. command foremost
```
foremost dolls.png -o output/
```
6. lakukan unzip
```
unzip output/zip/[tab]
```
7. remove folder output

```
rm -rf output
```
8. foremost file *2_c.jpg*
9. lakukan kembali langkah 6, sampai foremost file *4_c.jpg*
10. unzip kembali dan muncul file *flag.txt*

note:
langkah-langkah ini runut dan sistematis, sehingga bisa kita buat otomatis. Hhehe



flag:
```
picoCTF{4f11048e83ffc7d342a15bd2309b47de}
```
