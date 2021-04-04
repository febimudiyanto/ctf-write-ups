## Wave a flag

### Deskripsi

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm) has extraordinarily helpful information...

### Steps
1. Step ini khusus untuk linux
2. Download file nya

```
wget https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm
```

3. tambahkan mode *executable*

```
chmod +x warm
```
4. jalankan file nya

```
./warm -h
```

Flag:
```
picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}
```
