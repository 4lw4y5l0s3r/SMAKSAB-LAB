# Snowy Rock (Forensics, Easy)

<p> Pada Challenge kali ini, diberikan file attachment berupa file snowy_rock_fi.jpg yang ketika dicek metadata serta string pada file tersebut ternyata ada file zip dan snowyrock.txt yang tersimpan dalam file JPG tersebut. </p>

<p> Setelah itu, saya extract menggunakan Binwalk Tools untuk extract file snowyrock.txt tersebut. Setelah itu, saya coba cek hasil extract file JPG tersebut dan menemukan bahwa, file snowyrock.txt masih tersimpan di file Zip yang terkunci </p>

<p> Karena masih terkunci saya coba gunakan john untuk bruteforce password file zip tersebut serta menggunakan wordlists rockyou dan didapatkan lah passwordnya yaitu 11snowbird, extract saja dan file snowyrock.txt terbuka </p>

<img src=john.jpg>

<p> Saat file tersebut dibuka ternyata isinya kosong lalu saya cek hint challenge tersebut, saya putuskan untuk menggunakan tools Stegsnow dengan command sebagai berikut <i>stegsnow -C snowyrock.txt</i> </p>

<p>Flag sudah berhasil didapatkan ? Jawabannya tidak hasil dari stegsnow command adalah encoding base32 dan ROT13, decode terlebih dahulu untuk mendapatkan flag </p>

<p> Flag <strong> dsc{SnOw_rOcKs_fOr_r34l} </strong></p>
