# Ez PDF (Forensic, 100 Point)

<h3> Description Of Challenge </h3>
I just downloaded this PDF file from a strange site on the internet....

Author : daffainfo

<h3> How To Solve </h3>

<p> Given a pdf file which when opened only contains the words TCP1P CTF 2023, logo, and good luck. First, i use exiftool to find metadata about pdf file. Find interesting metadata in creator name but the strings is encoding with base64. So i use base64 decoder tools to decode that </p>
<img src=1st-flag.png>

<p> To find the second flag. I use tools online named PDF Extractor Online. Because i search in google about pdf steganography, the output is PDF Extractor so i think this pdf file maybe have a hidden image or text but not working if using binwalk or foremost command.</p>

<img src=2nd-flag.png>

<p> After that, i use strings command to find interesting strings in pdf file and find obfuscated javascript code. I deobfuscated the javascript code with jsnice and cyberchef. Then i find var pdf function in javascript code with last flag. In this moment, i use 2 solution.  </p>

<p> The first solution is manually find the last flag format like strings} in pdf function javascript code and using logical thinking to align the text with the flags so it can be read </p>

<p> The second solution is running the javascript code using node emulator. Before that, you must input javascript code in file and change integer of variable var from 1 to zero. Use node file.js in linux to run the javascript code and find the last flag </p>

<img src=3rd-flag.png>

<h3> FLAG : TCP1P{D01n9_F023n51C5_0N_pdf_f1L35_15_345y_15N7_17_l3jaf9ci293m1d} </h3>
