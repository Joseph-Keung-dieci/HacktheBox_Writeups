```bash
nmap -vv --reason -Pn -T4 --min-rate=1000 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/parallels/HacktheBox/Machines/10.10.11.183-Ambassador/results/10.10.11.183/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/parallels/HacktheBox/Machines/10.10.11.183-Ambassador/results/10.10.11.183/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.11.183
```

[/home/parallels/HacktheBox/Machines/10.10.11.183-Ambassador/results/10.10.11.183/scans/tcp80/tcp_80_http_nmap.txt](file:///home/parallels/HacktheBox/Machines/10.10.11.183-Ambassador/results/10.10.11.183/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.93 scan initiated Tue Dec  6 14:22:03 2022 as: nmap -vv --reason -Pn -T4 --min-rate=1000 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/parallels/HacktheBox/Machines/10.10.11.183-Ambassador/results/10.10.11.183/scans/tcp80/tcp_80_http_nmap.txt -oX /home/parallels/HacktheBox/Machines/10.10.11.183-Ambassador/results/10.10.11.183/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.11.183
Nmap scan report for 10.10.11.183
Host is up, received user-set (0.029s latency).
Scanned at 2022-12-06 14:22:09 AEDT for 17s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-feed: 
| Spidering limited to: maxpagecount=40; withinhost=10.10.11.183
|   Found the following feeds: 
|_    RSS (version 2.0): http://10.10.11.183:80/index.xml
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-errors: Couldn't find any error pages.
| http-internal-ip-disclosure: 
|_  Internal IP Leaked: 127.0.1.1
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.11.183
|     
|     Path: http://10.10.11.183:80/ananke/css/main.min.css
|     Line number: 1
|     Comment: 
|         /*!TACHYONS v4.9.1 | http://tachyons.io*/
|     
|     Path: http://10.10.11.183:80/ananke/css/main.min.css
|     Line number: 1
|     Comment: 
|         /*!normalize.css v8.0.0 | MIT License | github.com/necolas/normalize.css*/
|     
|     Path: http://10.10.11.183:80/ananke/css/main.min.css
|     Line number: 1
|     Comment: 
|_        /*!TACHYONS v4.12.0 | http://tachyons.io*/
| http-php-version: Logo query returned unknown hash 4e8656a1e2c09ff4135b58519f82a327
|_Credits query returned unknown hash 4e8656a1e2c09ff4135b58519f82a327
|_http-chrono: Request times for /; avg: 160.11ms; min: 152.56ms; max: 175.35ms
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; xml: 1
|     /ananke/css/
|       css: 1
|     /posts/welcome-to-the-ambassador-development-server/
|       Other: 1
|   Longest directory structure:
|     Depth: 2
|     Dir: /posts/welcome-to-the-ambassador-development-server/
|   Total files found (by extension):
|_    Other: 2; css: 1; xml: 1
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
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-headers: 
|   Date: Tue, 06 Dec 2022 03:22:18 GMT
|   Server: Apache/2.4.41 (Ubuntu)
|   Last-Modified: Fri, 02 Sep 2022 01:37:04 GMT
|   ETag: "e46-5e7a7c4652f79"
|   Accept-Ranges: bytes
|   Content-Length: 3654
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-enum: 
|_  /images/: Potentially interesting directory w/ listing on 'apache/2.4.41 (ubuntu)'
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-mobileversion-checker: No mobile version detected.
| http-vhosts: 
|_128 names had status 200
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-title: Ambassador Development Server
|_http-date: Tue, 06 Dec 2022 03:22:14 GMT; -2s from local time.
|_http-malware-host: Host appears to be clean
|_http-generator: Hugo 0.94.2

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Dec  6 14:22:26 2022 -- 1 IP address (1 host up) scanned in 23.01 seconds

```
