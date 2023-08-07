# misc, kevin (Solved)

<p> Pada challenge kali ini, diberikan sebuah URL link website yang ketika dibuka berisikan background game Among Us beserta gambar seseorang dengan nama file <i> kevin.jpeg </i></p>

<img src=kevin.jpeg>

<p> Karena deskripsi challenge bilang soal Steganography, saya coba untuk download terlebih dahulu file kevin.jpeg tersebut ke kali linux. Lalu saat di cek metadata serta strings dalam file tersebut, ternyata menghasilkan fakta bahwa file tersebut merupakan file PNG dan bukan JPG</p>

<img src=exiftool.png>

<p> Seteleh mengetahui fakta tersebut, saya gunakan tools zsteg (Steganography for PNG file) dan <i> Voilaaa... </i> Flag berhasil didapatkan </p>

<p>Flag : <strong> LITCTF{3d_printing_is_cool} </strong></p>
