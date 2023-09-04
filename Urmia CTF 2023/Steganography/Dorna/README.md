# Dorna (Steganography, Solved)

<h3> Description </h3>

<p> I'm hiding somewhere. Find me if you can!! </p>

<p> if you need a password anywhere use this "urumdorn4" </p>

<img src=dorna.jpg>

<h3> How To Solved </h3>

<p> Diberikan sebuah file JPG dengan password berupa urumdorn4. Karena diberikan password untuk file gambar tersebut, saya asumsikan bahwa tipe steganography yang digunakan adalah steghide </p>

<p> Saya gunakan command <strong> steghide extract -sf dorna.jpg</strong> dengan menggunakan urumdorn4 sebagai passphrase nya, diextract lah file dorn4.txt yang berisikan flag namun isinya masih terencode base64 </p>

<p> Tinggal decode saja base64 tersebut dan anda akan mendapatkan flag </p>

<h3> Flag : uctf{dorna_lar_yovasi} </h3>
