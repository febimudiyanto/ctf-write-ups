## Python Wrangling

### Deskripsi

Intruksinya adalah melakukan decrypt pada file *flag.txt.en* menggunakan password di file *pw.txt* dan menggunakan Decryptor yaitu file python *ende.py*

### Steps
1. Satukan semua file dalam folder yang sama
2. Buka file *pw.txt* kemudian copy isi passwordnya

```
pw.txt > ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
```
3. Decrypt menggunakan file *ende.py*

```
python3 ende.py -d flag.txt.en
```
masukkan password yang ada pada langkah 2.

flag:
```
picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}
```
