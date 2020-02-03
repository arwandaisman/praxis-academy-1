# Pengantar

## Instalasi Miniconda Ubuntu (opsional)
1. Download instalasi pada web resmi [conda.io](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
dan pilih platform Linux

2. Tersedia 2 installer yaitu Miniconda dan Anaconda, pilih miniconda

3. Lakukan verifikasi terhadap file bash yang sudah kita download, dengan mengetikkan
`sha256sum <filename>` / 
`sha256sum Miniconda3-latest-Linux-x86_64.sh` 
ikuti langkah langkah instalasi pada layar, jika tahapan instalasi membingungkan ada baiknya pilih mode _default_ (bisa dikonfigurasi dikemudian hari)

4. Untuk menguji miniconda yang anda install re-open terminal yang anda gunakan, lalu ketikkan 
`conda list` 
package yang sudah terinstall akan otomatis terlihat

## Instalasi Code Editor Ubuntu (Visual Studio Code)
### A 
1. Buka ubuntu software dan ketik, Visual Studio Code maka akan muncul software code editor yang akan kita install
![](https://github.com/dummytarget/praxis-academy/blob/master/img/msatu/hsatu/01.png)
2. Pilih, lalu install, tunggu hingga selesai

### B 
![](https://github.com/dummytarget/praxis-academy/blob/master/img/msatu/hsatu/02.png)
1. Atau masuk ke web resminya [VSC](https://code.visualstudio.com/) dan download .deb installation
2. Jalankan instalasi .deb, dan tunggu hingga selesai

## Instalasi PIP Ubuntu
1. Buka terminal lalu ketikkan `wget https://bootstrap.pypa.io/get-pip.py -o get-pip.py` dan tunggu proses hingga selesai
  - wget adalah command line ubuntu yang digunakan untuk mendownload langsung tanpa browser, dengan catatan url yang diinputkan harus benar

2. Karena ubuntu sudah terintsal pyhton maka ketikan `pyhton get-pip.py` untuk melakukan instalasi pip, lalu tunggu proses hingga selesai.

3. Ketik `pip` pada terminal, jika instalasi berhasil maka _manual book_ dari pip akan muncul pada terminal
![](https://github.com/dummytarget/praxis-academy/blob/master/img/msatu/hsatu/03.png)
