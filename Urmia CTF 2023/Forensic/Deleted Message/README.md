# Deleted Message (Forensic, Solved)

<h3> Description </h3>

<p> Cyber Police have seized a computer containing illegal content, but the data stored is secured with a password. </p>

<p> A member of the criminal organization owning the computer was arrested. Police suspect that the password was sent to the criminal via SMS, but the message was deleted right before the arrest. </p>

<p> You’re given a dump of the data partition of the phone (running Android 6.0). Your job as the forensic specialist is to recover the deleted password.</p>

<h3> How To Solved </h3>

<p> Diberikan sebuah file gz (zip) yang ketika diextract menghasilkan tar dan ketika diextract lagi menghasilkan folder data dump dari Android 6.0, saya coba gunakan grep command yaitu <strong> grep -R uctf </strong> untuk mendapatkan flag dan ternyata saya mendapatkan path menuju flag yaitu user/0/com.android.messaging/databases/bugle_db-journal. Sisanya tinggal buka file tersebut dan flag berhasil didapat </p>

<img src=grep.png>

<p> Terima kasih atas sepuh TCP1P yang sudah memberikan pencerahan untuk solved soal ini </p>

<img src=ilmu.png>

<h3> Flag : uctf{l057_1n_urm14} </h3>
