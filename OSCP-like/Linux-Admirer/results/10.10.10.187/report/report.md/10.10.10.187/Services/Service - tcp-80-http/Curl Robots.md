```bash
curl -sSikf http://10.10.10.187:80/robots.txt
```

[/home/parallels/HacktheBox/OSCP-like/Linux-Admirer/results/10.10.10.187/scans/tcp80/tcp_80_http_curl-robots.txt](file:///home/parallels/HacktheBox/OSCP-like/Linux-Admirer/results/10.10.10.187/scans/tcp80/tcp_80_http_curl-robots.txt):

```
HTTP/1.1 200 OK
Date: Sun, 13 Nov 2022 03:14:06 GMT
Server: Apache/2.4.25 (Debian)
Last-Modified: Wed, 29 Apr 2020 09:22:10 GMT
ETag: "8a-5a46a7b96e300"
Accept-Ranges: bytes
Content-Length: 138
Vary: Accept-Encoding
Content-Type: text/plain

User-agent: *

# This folder contains personal contacts and creds, so no one -not even robots- should see it - waldo
Disallow: /admin-dir

```