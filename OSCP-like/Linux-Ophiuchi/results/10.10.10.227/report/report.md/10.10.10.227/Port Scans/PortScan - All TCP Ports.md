```bash
nmap -vv --reason -Pn -T4 --min-rate=1000 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/_full_tcp_nmap.txt" -oX "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/xml/_full_tcp_nmap.xml" 10.10.10.227
```

[/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/_full_tcp_nmap.txt](file:///home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/_full_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Fri Sep 23 13:51:29 2022 as: nmap -vv --reason -Pn -T4 --min-rate=1000 -sV -sC --version-all -A --osscan-guess -p- -oN /home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/_full_tcp_nmap.txt -oX /home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/xml/_full_tcp_nmap.xml 10.10.10.227
Nmap scan report for 10.10.10.227
Host is up, received user-set (0.033s latency).
Scanned at 2022-09-23 13:51:29 AEST for 18s
Not shown: 65533 closed tcp ports (conn-refused)
PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 6d:fc:68:e2:da:5e:80:df:bc:d0:45:f5:29:db:04:ee (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpzM/GEYunOwIMB+FyQCnOaYRK1DYv8e0+VI3Zy7LnY157q+3SITcgm98JGS/gXgdHQ4JnkCcXjUb9LaNRxRWO+l43E9v2b2U9roG8QetbBUl5CjJ0KHXeIwNgOcsqfwju8i8GA8sqQCELpJ3zKtKtxeoBo+/o3OnKGzT/Ou8lqPK7ESeh6OWCo15Rx9iOBS40i6zk77QTc4h2jGLOgyTfOuSGTWhUxkhqBLqSaHz80G7HsPSs1BA9zAV8BOx9WmtpMsgDcNG14JAQQd904RCzgw0OaQ0J6szs78Us8Piec0rF/T4b1H3sbUedOdA0QKgGbNojObVrz5VwOw6rqxbs1gZLePXB5ZNjm0cp+Sen8TkRkdUf7Sgw92B//RhSoIakp1u5eOPs/uJ6hyCholUnerl3WK8NPB9f9ICPYq8PbvVMu6zcytV/cCjwxFloWB989iyuqG/lYcdMhGJlAacOFy5TRcTB8c5Qlmtl44J/4dyuCJAhj5SY6TRdcSxhmz0=
|   256 7a:c9:83:7e:13:cb:c3:f9:59:1e:53:21:ab:19:76:ab (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM79V2Ts2us0NxZA7nnN9jor98XRj0hw7QCb+A9U8aEhoYBcrtUqegExaj/yrxjbZ/l0DWw2EkqH4uly451JuMs=
|   256 17:6b:c3:a8:fc:5d:36:08:a1:40:89:d2:f4:0a:c6:46 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIO31s/C33kbuzZl9ohJWVEmLsW9aqObU6ZjlpbOQJt0C
8080/tcp open  http    syn-ack Apache Tomcat 9.0.38
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Parse YAML
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Sep 23 13:51:47 2022 -- 1 IP address (1 host up) scanned in 17.81 seconds

```
