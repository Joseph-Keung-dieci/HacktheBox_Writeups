```bash
nmap -vv --reason -Pn -T4 --min-rate=1000 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/parallels/HacktheBox/OSCP-like/Linux-Mirai/results/10.10.10.48/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/parallels/HacktheBox/OSCP-like/Linux-Mirai/results/10.10.10.48/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.48
```

[/home/parallels/HacktheBox/OSCP-like/Linux-Mirai/results/10.10.10.48/scans/tcp80/tcp_80_http_nmap.txt](file:///home/parallels/HacktheBox/OSCP-like/Linux-Mirai/results/10.10.10.48/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.92 scan initiated Sun Sep 18 15:13:32 2022 as: nmap -vv --reason -Pn -T4 --min-rate=1000 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/parallels/HacktheBox/OSCP-like/Linux-Mirai/results/10.10.10.48/scans/tcp80/tcp_80_http_nmap.txt -oX /home/parallels/HacktheBox/OSCP-like/Linux-Mirai/results/10.10.10.48/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.10.48
Nmap scan report for 10.10.10.48
Host is up, received user-set (0.021s latency).
Scanned at 2022-09-18 15:13:32 AEST for 30s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack lighttpd 1.4.35
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-headers: 
|   X-Pi-hole: A black hole for Internet advertisements.
|   Content-type: text/html; charset=UTF-8
|   Content-Length: 0
|   Connection: close
|   Date: Sun, 18 Sep 2022 05:13:43 GMT
|   Server: lighttpd/1.4.35
|   
|_  (Request type: GET)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-referer-checker: Couldn't find any cross-domain scripts.
| http-useragent-tester: 
|   Status for browser useragent: 404
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-server-header: lighttpd/1.4.35
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=10.10.10.48
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://10.10.10.48:80/
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-mobileversion-checker: No mobile version detected.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-chrono: Request times for /; avg: 152.77ms; min: 150.08ms; max: 156.22ms
|_http-comments-displayer: Couldn't find any comments.
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-feed: Couldn't find any feeds.
|_http-malware-host: Host appears to be clean
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-date: Sun, 18 Sep 2022 05:13:39 GMT; -1s from local time.
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| http-vhosts: 
|_128 names had status 200

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Sep 18 15:14:02 2022 -- 1 IP address (1 host up) scanned in 30.31 seconds

```
