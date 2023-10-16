# Bluffer Overflow (PWN, 100 Point)

# Description

Maybe it's your first time pwning? Can you overwrite the variable?

nc ctf.tcp1p.com 17027

Author: rennfurukawa

# How To Solve

Given a zip file which when extracted contains the c file which is the source code for running netcat. In the description it is explained that this problem is a buffer overflow type with overwrite variables. I opened the netcat server's c file and found the buffer overflow size, which was 20. Apart from that, the variable value for getting the flag on the netcat server was 5134160.

<img src=pwn.png>

After that, i search in google about challenge buffer overflow and overwrite variable. Find it in challenge PWN 101 TryHackMe, PWN102. I used script with a little change and run in linux, after run i find the flag.

<img src=flag.png>

<h3> FLAG : TCP1P{ez_buff3r_0verflow_l0c4l_v4r1abl3_38763f0c86da16fe14e062cd054d71ca} </h3>
