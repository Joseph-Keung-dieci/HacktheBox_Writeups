```bash
[*] ssh on tcp/22

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp22/tcp_22_ssh_hydra.txt" ssh://10.10.10.227

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 22 -O "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp22/tcp_22_ssh_medusa.txt" -M ssh -h 10.10.10.227

[*] http on tcp/8080

	[-] (gobuster v3) Multi-threaded directory/file enumeration for web servers using various wordlists:

		gobuster dir -u http://10.10.10.227:8080/ -t 50 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -x "txt,html,php,asp,aspx,jsp" -o "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_gobuster_dirbuster.txt"

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 8080 -o "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_auth_hydra.txt" http-get://10.10.10.227/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 8080 -O "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_auth_medusa.txt" -M http -h 10.10.10.227 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 8080 -o "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_form_hydra.txt" http-post-form://10.10.10.227/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 8080 -O "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_form_medusa.txt" -M web-form -h 10.10.10.227 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (nikto) old but generally reliable web server enumeration tool:

		nikto -ask=no -h http://10.10.10.227:8080 2>&1 | tee "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_nikto.txt"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://10.10.10.227:8080/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/parallels/HacktheBox/OSCP-like/Linux-Ophiuchi/results/10.10.10.227/scans/tcp8080/tcp_8080_http_wpscan.txt"


```