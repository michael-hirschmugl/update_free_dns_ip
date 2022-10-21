#!/usr/bin/python

# This script is an adaption of Jeremy Blythe's script (http://jeremyblythe.blogspot.co.uk/2012/05/python-freedns-client-on-raspberry-pi.html)
# It will update FreeDNS using multiple keys if you have "Link updates of the same IP together" Disabled.

import urllib2
import os.path

FREEDNS_URL = 'http://freedns.afraid.org/dynamic/update.php?'
OLDIP_FILE = '/var/lib/misc/oldip'
USER_KEYS = ["", "", ""]

def updatedns(ip):
    for key in USER_KEYS:
        print urllib2.urlopen(FREEDNS_URL+key).read().strip()

    f = open(OLDIP_FILE, 'w')
    f.write(ip)
    f.close()

newip = urllib2.urlopen("http://ip.dnsexit.com/").read().strip()

if not os.path.exists(OLDIP_FILE):
    updatedns(newip)
else:
    f = open(OLDIP_FILE, 'r')
    oldip = f.read()
    f.close()
    if oldip != newip:
        updatedns(newip)