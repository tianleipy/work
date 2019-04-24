import urllib.request
import urllib.parse
import json
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
i = input("请输入需要翻译的内容：")
data = {}
data['i'] = i
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15547243462692'
data['sign'] = 'c7deffc620db0c13898767172807fcb3'
data['ts'] = '1554724346269'
data['bv'] = '7aa7fb563107e590a52b125bb19c7b5a'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'
data = urllib.parse.urlencode(data).encode('utf-8')
respons = urllib.request.urlopen(url,data)
html = respons.read().decode('utf-8')
#print(html)
html = json.loads(html)
print("翻译后的结果为：%s" %(html['translateResult'][0][0]['tgt']))