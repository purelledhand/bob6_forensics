from json import dumps
from datetime import date, datetime
import pythonwhois
import pdb
import json

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type %s not serializable" % type(obj))

urlfile = open('url_sample.txt', 'r')
line = urlfile.readlines()

whoisfile = open('result.txt','w')

for i in line:
  print i
  tmp = str(pythonwhois.get_whois(i))
  whoisfile.write(tmp)
  print json.dumps(tmp, default=json_serial)

urlfile.close()
whoisfile.close()
