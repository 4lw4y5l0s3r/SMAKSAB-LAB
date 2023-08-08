# My boss left ( Web, Solved)

<p> Diberikan file attachment zip yang berisikan login.php serta URL website yang ketika dibuka berisikan login page, saat saya baca file login.php ternyata ada credential password dalam bentuk encoding base64. Langsung saya decode dan menghasilkan string <i> this is some gibberish text password </i></p>

<p> Awalnya saya pikir string hasil decode tersebut adalah passwordnya dan usernya adalah admin (setau saya, user default di login adalah admin), namun ternyata salah. Saat saya coba masukkan username admin dan password encoding base64 ternyata berhasil mendapatkan flag </p>

<img src=web.png>

<h3> <strong> LITCTF{oOps_sh0uld_h4v3_us3d_str1ct_c0mp4r1sons} </strong></h3>
