```bash
dig -p 53 -x 10.10.10.182 @10.10.10.182
```

[/home/parallels/HacktheBox/OSCP-like/AD-Cascade/results/10.10.10.182/scans/tcp53/tcp_53_dns_reverse-lookup.txt](file:///home/parallels/HacktheBox/OSCP-like/AD-Cascade/results/10.10.10.182/scans/tcp53/tcp_53_dns_reverse-lookup.txt):

```

; <<>> DiG 9.18.8-1-Debian <<>> -p 53 -x 10.10.10.182 @10.10.10.182
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: FORMERR, id: 28342
;; flags: qr rd; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 978b51d9f39a263d (echoed)
;; QUESTION SECTION:
;182.10.10.10.in-addr.arpa.	IN	PTR

;; Query time: 27 msec
;; SERVER: 10.10.10.182#53(10.10.10.182) (UDP)
;; WHEN: Fri Nov 18 15:56:55 AEDT 2022
;; MSG SIZE  rcvd: 66


```
