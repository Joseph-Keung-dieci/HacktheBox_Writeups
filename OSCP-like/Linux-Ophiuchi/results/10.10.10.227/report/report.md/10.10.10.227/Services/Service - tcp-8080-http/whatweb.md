```bash
whatweb --color=never --no-errors -a 3 -v http://10.10.10.227:8080 2>&1
```

[/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_whatweb.txt](file:///home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_whatweb.txt):

```
WhatWeb report for http://10.10.10.227:8080
Status    : 200 OK
Title     : Parse YAML
IP        : 10.10.10.227
Country   : RESERVED, ZZ

Summary   : Cookies[JSESSIONID], HttpOnly[JSESSIONID], Java

Detected Plugins:
[ Cookies ]
	Display the names of cookies in the HTTP headers. The
	values are not returned to save on space.

	String       : JSESSIONID

[ HttpOnly ]
	If the HttpOnly flag is included in the HTTP set-cookie
	response header and the browser supports it then the cookie
	cannot be accessed through client side script - More Info:
	http://en.wikipedia.org/wiki/HTTP_cookie

	String       : JSESSIONID

[ Java ]
	Java allows you to play online games, chat with people
	around the world, calculate your mortgage interest, and
	view images in 3D, just to name a few. It's also integral
	to the intranet applications and other e-business solutions
	that are the foundation of corporate computing.

	Website     : http://www.java.com/

HTTP Headers:
	HTTP/1.1 200
	Set-Cookie: JSESSIONID=D119A66256869D003DBC50B2D12DADA2; Path=/; HttpOnly
	Content-Type: text/html;charset=UTF-8
	Content-Length: 8042
	Date: Fri, 23 Sep 2022 03:51:38 GMT
	Connection: close



```
