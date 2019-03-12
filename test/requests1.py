import requests
import urllib

http_proxy = {"http":"http://hct8jnz:Sikim@ups1@153.2.227.107:8080"}
my_url = "https://www.google.com/"

s = requests.session()
s.proxies = http_proxy

r = s.get(my_url)

#res = requests.get(my_url , proxies = http_proxy)
#
# print(res)