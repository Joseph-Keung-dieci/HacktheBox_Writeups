```bash
dig AXFR -p 53 @10.10.11.166
```

[/home/kali/Desktop/HTB/HacktheBox/Machines/10.10.11.166-trick/results/10.10.11.166/scans/tcp53/tcp_53_dns_zone-transfer.txt](file:///home/kali/Desktop/HTB/HacktheBox/Machines/10.10.11.166-trick/results/10.10.11.166/scans/tcp53/tcp_53_dns_zone-transfer.txt):

```

; <<>> DiG 9.18.4-2-Debian <<>> AXFR -p 53 @10.10.11.166
; (1 server found)
;; global options: +cmd
;; Query time: 36 msec
;; SERVER: 10.10.11.166#53(10.10.11.166) (UDP)
;; WHEN: Sat Aug 13 07:23:26 EDT 2022
;; MSG SIZE  rcvd: 56


```