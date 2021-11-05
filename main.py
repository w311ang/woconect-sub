import requests
import os

s=requests.Session()
s.headers.update({'accessToken':os.getenv('token')})
with s.post('https://woapp.10155.com/trafficBus/userAppList/checkUserflow') as resp:
  json=resp.json()
  result=json['result']
  host=result['host']
  port=result['port']
  username=result['username']
  password=result['password']
  socksurl='socks5://%s:%s@%s:%s/s'%(username,password,host,port)
  #socks5://3000007591&13135361530&1636100380:BB36EC5B9459D563DB172F9284632648@n89.gzproxy.10155.com:8089/
  with open('docs/sub.txt','w') as f:
    f.write(socksurl)
