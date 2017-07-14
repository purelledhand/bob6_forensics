import pythonwhois

data = pythonwhois.net.get_whois_raw("www.google.com",with_server_list=False)


import pdb
pdb.set_trace()

print(data['www.google.com'])
