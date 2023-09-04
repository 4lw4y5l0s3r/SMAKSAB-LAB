# Deb File | The Old Systems (Steganography, Solved)

<h3> Desciption </h3>

<p> Can you believe it? people still use linux? after the emerge of Evil E computers, nobody bothered to use linux systems. anyways, we got this file from database gaurds' pc, can you help us? </p>

<h3> How To Solve </h3>

<p> Diberikan sebuah file Debian binary package compressed data gz yang ketika dicek menggunakan command string terdapat file zip di dalamnya </p>

<img src=strings.png>

<p> Saya coba untuk extract filenya menggunakan command binwalk -M -e uctf.deb, setelah diextract saya menemukan 2 folder dan di folder kedua ternyata ada 2 file txt, namun salah satu nya merupakan bash script. Setelah dibaca ternyata ada flag di teks tersebut </p>

<img src=flag.png>

<h3> Flag : UCTF{c4n_p3n6u1n5_5urv1v3_1n_54l7_w473r} </h3>
