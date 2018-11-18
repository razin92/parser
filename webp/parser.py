from .secret import auth_data_istv, auth_data_check_ip
import requests
import re

#file = open('site.html', 'r')
#r = requests.post(url, auth_data_istv)
#r = requests.get(url2)
#data = r.content.decode('windows-1251', 'ignore')
#data = ''.join([x for x in file])
#print(r.json())
#print(data)
data = ''
result = re.findall(r'<dt>.+</dt>', data)
result2 = re.findall(r'<dd>\n*.+\n*</dd>', data)

res_dict = {}
for x,y in zip(result, result2):
    res_dict.update({re.findall(r'[А-Яа-я.A-Z-\s]+', x)[0]: re.findall(r'[^</>\n]+', y)[1]})
#file.close()
