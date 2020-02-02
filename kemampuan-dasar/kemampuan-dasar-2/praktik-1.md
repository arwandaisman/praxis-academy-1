# Kemampuan Dasar 1
## Geting Sarted with Github

Pengenalan langkah awal dimulai dari 
  1. Pembuatan repositori di lokal
  2. Melakukan push
  3. Melakukan cloning repo dari github
  4. Melakukan perubahan terhadap file yang sudah di push
  5. Memperbaharui file yang sudah di push
  6. Melakukan rebase

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-a.png)
Gambar diatas menjelaskan bagaimana cara membuat sebuah repository lokal dengan nama ryhmes. menambah beberapa file diantaranya seperti README.md. Setelah itu melakukan commit terhdapa ada yang sudah dibuat pada repositori local

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-b.png)
menambahkan beberapa file dalam repository local yang seharusnya bisa dodownload melalui link pada web referensi, karena link yang dituju sudah tidak aktif, maka pembuatan file secara manual dengan comman line _touch_.

Command line _git status_ untuk melihat apa saja yang sudah dibuat, dan dilakukan commit.

Kita bisa menggunakan command line _git add_ untuk menambah pada status bahwa file tersebut akan siap di-commit

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-c.png)
Ketika semua file sudah di commit, file tersebut sudah siap di push pada repositori yang kita miliki di Github. 
Dengan command line _git log_ kita bis melihat apa saja yang sudah dika kerjakan sebelumnya

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-d.png)
Melakukan remoting terhadapa repositori yang akan kita gunakan di Github, serta membuat sebuah repositori baru pada Github.
setelah itu barulah dilakukan push repositori lokal menucu Github, dengan nama Master

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-e.png)
Membuat sebuah branch baru pada dari repo github

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-f.png)
Menambahkan beberapa member siapa saja yang mampu untuk melakukan editing terhadap repositori yang ada pada Github
Terlihat ada 2 member dalam repo tersebut (yang sedang remoting) 

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-g.png)
Membuat sebuah branch lagi, jadi dimana fungsi __branch__ digunakan ketika hendak melakukan suatu pengembangan secara terpisah

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-h.png)
_cek log status_

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-i.png)
Karena referensi ini memerlukan 2 akun untuk melakukan percobaan secara penuh, disini saya hanya melakukan perintah yang bisa dilakukan, seperti, _add, commit, push, touch,_ yang bisa berjalan dengan lancar, selain itu, terjadi error yang seharusnya diselesaikan dengan menggunakan 2 Github yang berbeda

![](https://github.com/dummytarget/praxis-academy/blob/master/img/pr1-j.png)
Melakukan perintah rebase yang digunakan untuk menyunting kembali apakah comit yang sudah kita lakukan tadi, sudah benar, jika masih ada kesalahan bisa dilakukan perubahamn disini

Jika kita melakuka rebase akan ada beberapa perintah seperti dibawah ini

__Commands:__
p, pick = use commit 
r, reword = use commit, but edit the commit message 
e, edit = use commit, but stop for amending 
s, squash = use commit, but meld into previous commit 
f, fixup = like "squash", but discard this commit's log message 
x, exec = run command (the rest of the line) using shell 
