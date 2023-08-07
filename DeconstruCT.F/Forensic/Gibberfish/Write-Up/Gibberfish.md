# Gibberfish (Forensics, Easy)

<p> Pada challenge kali ini, diberikan file attachment berupa file flag.txt yang ketika dibuka berisikan encoding base64. Setelah didecode ternyata hasil encoding merupakan header file elf 64 bit. </p>

<p> Extract hasil encoding base64 tersebut menjadi sebuah elf 64 bit, dan buka menggunakan debugger tools seperti Ghidra, IDA, Cutter dan tools lainnya. </p>

<p> Setelah itu cek bagian main pada file elf tersebut, <i> Simsalabim </i> Flag berhasil ditemukan </p>

<p> Sedikit tambahan, sebenarnya anda cukup menggunakan strings command jika menggunakan Linux untuk mendapatkan flag </p>

<p> Flag : <strong> dsc{h0wdy_c7f_h4ack3r5} </strong></p>
