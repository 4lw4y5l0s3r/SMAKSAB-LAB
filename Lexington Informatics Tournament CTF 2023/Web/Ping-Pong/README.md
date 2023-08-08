# Ping Pong ( Web, Solved )

<p> Diberikan file attachment berupa ZIP yang berisikan file python flask tentang website tersebut serta URL website yang ketika dibuka berisikan terminal pinging IP addresss atau domain. </p>

<p> Saya curiga kalau soal ini berkaitan dengan command injection, jadi saya coba masukkan payload <strong> 8.8.8.8;ls </strong> dan ternyata keluar isi dari machine website tersebut. </p>

<img src=ping.png>

<p> karena ada flag.txt dalam listing directory machine tersebut, saya gunakan command <strong> 8.8.8.8; cat flag.txt </strong> dan flag berhasil didapatkan </p>

<h3>Flag : <strong> LITCTF{I_sh0uld_b3_m0r3_c4r3ful} </strong></h3>
