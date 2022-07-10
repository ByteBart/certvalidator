#!/usr/bin/python
from urllib.request import  ssl, socket
import sys
from datetime import datetime


#some site without http/https in the path
base_url = sys.argv[1]
port = '443'

hostname = base_url
context = ssl.create_default_context()

now = now = datetime.now()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        certificate = ssock.getpeercert()
        print ("Issuer is:  "+(certificate['issuer'][1][0][1]))
        certExpires = datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
        daysToExpiration = (certExpires - datetime.now()).days
        print ("Expires on: "+certificate['notAfter'])
        print ("Expires in "+str(daysToExpiration)+" days")
        print ("Valid for: "+str(certificate['subject']))
        