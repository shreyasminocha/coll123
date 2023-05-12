---
marp: true
theme: leet
---

# forensics

- file formats and signatures
- metadata
- stegano
- wireshark pcaps
- disk images

---

- file extensions don't actually matter
- [magic numbers](https://en.wikipedia.org/wiki/File_format#Magic_number) (bytes) at the start of binaries

binwalk: find embedded binaries

```sh
# scan the file for embedded files
binwalk file.jpg

# extract all embedded files
binwalk --dd='.*' file.jpg
```

---

## exif: embedded metadata

```sh
exiftool file.jpg
```

---

## image steganography

steghide: popular image stegano tool

```sh
# embed secret.txt in file.jpg
steghide embed -cf file.jpg -sf secret.txt

# extract secrets, if any
steghide extract -sf file.jpg
```

optionally supports encrypting the embedded file. by default, there's no password.

---

## audio steganography

audio spectrogram: visualization of the frequencies in an audio file

can be used to hide images or messages

- [encode](https://alexadam.github.io/demos/img-encode/index.html)
- [decode](https://manual.audacityteam.org/man/spectrogram_view.html)

---

## wireshark

powerful network analysis tool

some chals require analyzing a given packet capture (`.pcapng`) to look for a flag

---

## disk imaging

```sh
# create an image of the disk at /dev/sda
dd if=/dev/sda of=test.iso

# view more info about a disk image
fdisk -l test.iso

# mount an image to /mnt/test
mount test.iso /mnt/test
```
