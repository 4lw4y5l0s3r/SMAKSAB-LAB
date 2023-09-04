# Hidden Streams (Steganography, Solved)

<h3> Description </h3>

<p> Explore the available streams and consider the different types of data that can be associated with a single filename. Good luck! </p>

<h3> How To Solved </h3>

<p> Diberikan file zip yang ketika diextract berisikan file disk image virtual server atau virtual pc, karena merupakan disk image saya kepikiran tentang tools bernama Autopsy. Langsung saya coba cek file disk image tersebut menggunakan Autopsy dan ketemu file zip bernama flag.zip namun dikasih password </p>

<img src=autopsy.png>

<p> Untuk mencari passwordnya saya cek file disk image tersebut menggunakan command <strong> strings -n 10 stream-ctf.vhd </strong>. Sisanya hanya perlu buka file zip tersebut menggunakan password yang ditemukan dan ketemu flagnya </p>

<img src=pw.png>

<h3> Flag : uctf{St. Mary Church} </h3>
