
import http.client
import hashlib
import urllib
import random
import json
import sys
def translation(q, fromLang='wyw', toLang='en'):

    appid = '20190510000296192'
    secretKey = 'Cacyhw1OlP116JWZgGG7'

    httpClient = None
    myurl = '/api/trans/vip/translate'
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
    
        # response is an HTTPResponse object
        response = httpClient.getresponse()
        content = response.read().decode('utf-8')
        data = json.loads(content)
        result = str(data['trans_result'][0]['dst'])
        return result
    except Exception as e:
        print("报错了")
    finally:
        if httpClient:
            httpClient.close()
