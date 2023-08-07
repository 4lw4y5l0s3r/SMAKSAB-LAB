# misc, Kevin (Solved)

<p> Pada Challenge kali ini, diberikan link URL sebuah website yang ketika dibuka berisikan background game among us dan sebuah foto seorang dengan nama file kevin.jpg. </p>
<p> Karena deskripsi soal menyebutkan steganography, saya download file kevin.jpg tersebut di Kali Linux. Saat di cek metadata serta strings yang terdapat pada file kevin.jpg hasilnya adalah file tersebut merupakan file PNG dan bukan file JPG. </p>
<img src=exiftool.png>
<p> Karena file kevin.jpg merupakan file PNG, saya gunakan tools zsteg untuk mendapatkan flag dalam file tersebut dan <i> Voilaaa... </i> Saya berhasil mendapatkan flagnya. </p>

<p> Flag : <strong> LITCTF{3d_printing_is_cool} </strong></p>
