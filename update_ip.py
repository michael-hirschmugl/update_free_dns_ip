#!/usr/bin/python

# This script is an adaption of Paul Castle's script, which is the adaption of Jeremy Blythe's script (http://jeremyblythe.blogspot.co.uk/2012/05/python-freedns-client-on-raspberry-pi.html)
# It will update FreeDNS using multiple keys if you have "Link updates of the same IP together" Disabled.

import urllib.request as urllib2
import requests
import os.path

#SUBDOMAIN = ""
#USER = ""
#PASS = ""
FREEDNS_URL = 'http://freedns.afraid.org/dynamic/update.php?'
USER_KEY = ""

print(urllib2.urlopen(FREEDNS_URL+USER_KEY).read().strip())

#newip = str(urllib2.urlopen("http://ip.dnsexit.com/").read().strip(), "UTF-8")
#print(newip)

#URL = "http://" + USER + ":" + PASS + "@freedns.afraid.org/nic/update?hostname=" + SUBDOMAIN + "&myip=" + newip

#print(URL)

#urllib2.urlopen(URL)
#f = requests.get(URL)
#print(f.text)