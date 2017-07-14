import pythonwhois
import pdb

f = open('url_sample.txt', 'r')
line = f.readlines()

for i in line:
        print i
        print pythonwhois.get_whois(i)


