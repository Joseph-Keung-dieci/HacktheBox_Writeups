```bash
nmap -vv --reason -Pn -T4 --min-rate=1000 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/parallels/HacktheBox/OSCP-like/Linux-Admirer/results/10.10.10.187/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/parallels/HacktheBox/OSCP-like/Linux-Admirer/results/10.10.10.187/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.187
```

[/home/parallels/HacktheBox/OSCP-like/Linux-Admirer/results/10.10.10.187/scans/tcp80/tcp_80_http_nmap.txt](file:///home/parallels/HacktheBox/OSCP-like/Linux-Admirer/results/10.10.10.187/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.93 scan initiated Sun Nov 13 14:14:00 2022 as: nmap -vv --reason -Pn -T4 --min-rate=1000 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/parallels/HacktheBox/OSCP-like/Linux-Admirer/results/10.10.10.187/scans/tcp80/tcp_80_http_nmap.txt -oX /home/parallels/HacktheBox/OSCP-like/Linux-Admirer/results/10.10.10.187/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.10.187
Nmap scan report for 10.10.10.187
Host is up, received user-set (0.026s latency).
Scanned at 2022-11-13 14:14:00 AEDT for 18s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.25 ((Debian))
|_http-chrono: Request times for /; avg: 197.27ms; min: 153.68ms; max: 274.42ms
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-malware-host: Host appears to be clean
|_http-feed: Couldn't find any feeds.
|_http-date: Sun, 13 Nov 2022 03:14:11 GMT; 0s from local time.
| http-headers: 
|   Date: Sun, 13 Nov 2022 03:14:10 GMT
|   Server: Apache/2.4.25 (Debian)
|   Connection: close
|   Content-Type: text/html; charset=UTF-8
|   
|_  (Request type: HEAD)
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
| http-robots.txt: 1 disallowed entry 
|_/admin-dir
| http-vhosts: 
|_128 names had status 200
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-mobileversion-checker: No mobile version detected.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-title: Admirer
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=10.10.10.187
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://10.10.10.187:80/index.html
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.10.187
|     
|     Path: http://10.10.10.187:80/
|     Line number: 20
|     Comment: 
|         <!-- Header -->
|     
|     Path: http://10.10.10.187:80/
|     Line number: 17
|     Comment: 
|         <!-- Wrapper -->
|     
|     Path: http://10.10.10.187:80/
|     Line number: 94
|     Comment: 
|         <!-- Footer -->
|     
|     Path: http://10.10.10.187:80/
|     Line number: 120
|     Comment: 
|         <!-- Still under development... This does not send anything yet, but it looks nice! -->
|     
|     Path: http://10.10.10.187:80/
|     Line number: 30
|     Comment: 
|         <!-- Main -->
|     
|     Path: http://10.10.10.187:80/
|     Line number: 144
|     Comment: 
|         <!-- Scripts -->
|     
|     Path: http://10.10.10.187:80/
|     Line number: 2
|     Comment: 
|         <!--
|         	Multiverse by HTML5 UP
|         	html5up.net | @ajlkn
|         	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
|_        -->
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
| http-enum: 
|_  /robots.txt: Robots file
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
|_http-exif-spider: ERROR: Script execution failed (use -d to debug)
|_http-server-header: Apache/2.4.25 (Debian)
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-useragent-tester: 
|   Status for browser useragent: 200
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
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|     /assets/css/
|       css: 1
|     /assets/js/
|       js: 2
|     /images/fulls/
|       jpg: 4
|     /images/thumbs/
|       jpg: 4
|   Longest directory structure:
|     Depth: 2
|     Dir: /images/thumbs/
|   Total files found (by extension):
|_    Other: 1; css: 1; jpg: 8; js: 2
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.10.187
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://10.10.10.187:80/
|     Form id: name
|_    Form action: #
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
| http-php-version: Logo query returned unknown hash 123371a226c5565255e93ac3b0dc0f5a
|_Credits query returned unknown hash 123371a226c5565255e93ac3b0dc0f5a
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Nov 13 14:14:18 2022 -- 1 IP address (1 host up) scanned in 18.74 seconds

```
