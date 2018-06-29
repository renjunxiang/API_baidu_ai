# API_baidu_ai
[![](https://img.shields.io/badge/Python-3.5-blue.svg)](https://www.python.org/)
[![](https://img.shields.io/badge/baidu--aip-2.1.0.0-brightgreen.svg)](https://pypi.python.org/pypi/baidu-aip/2.1.0.0)
[![](https://img.shields.io/badge/requests-2.18.4-brightgreen.svg)](https://pypi.python.org/pypi/requests/2.18.4)<br>

## 项目简介
**百度人工智能平台API封装**

## 功能说明
### 获取平台的access_token
get_token.py：需要API_KEY和SECRET_KEY，在config/account.py中请自行修改账号信息，开通账号完全免费<br>
**提供的项目账号信息仅为了方便使用者进行测试，有每日调用上限，禁止传播和任何商业化使用，学术研究需经本人许可！**
``` python
from API_baidu import get_token

API_KEY = 'xxxxxxx'
SECRET_KEY = 'xxxxxxx'
token = get_token(API_KEY=API_KEY,SECRET_KEY=SECRET_KEY)
print(token)
```

### 调用平台的SDK做自然语言处理
NLP_SDK.py：公测以后百度推荐使用SDK方式，因此对其做了简单的封装，需要APP_ID、API_KEY和SECRET_KEY，返回字典<br>
``` python
from API_baidu import NLP_SDK

text = '本区办理的营业执照且登记档案中的场地使用证明仍在有效期内，可使用《关于经营场所合法使用证明材料的情况说明》'
result = NLP_SDK(text=text, method='depParser')
print(result)
```
![](https://github.com/renjunxiang/API_baidu_ai/blob/master/picture/depParser.jpg)<br>

### 调用平台的API做实体识别
entity_annotation.py：需要API_KEY和SECRET_KEY，返回字典<br>
``` python
from API_baidu import entity_annotation

text = '委托他人申请的，还须提交委托书、委托代理人或指定代表身份证明（如身份证、外籍人员护照等）原件、复印件'
results = entity_annotation(text=text)
print(results)
```
![](https://github.com/renjunxiang/API_baidu_ai/blob/master/picture/entity_annotation.jpg)<br>

### 调用平台的API做人脸检测
face_detect.py：需要API_KEY和SECRET_KEY，返回字典，选择是否返回图片<br>
``` python
from API_baidu import face_detect

results = face_detect(image_path='xxx.jpg',
                      show=True,
                      savepath=None)
print(results)
```
![](https://github.com/renjunxiang/API_baidu_ai/blob/master/picture/e2.jpg)<br>
![](https://github.com/renjunxiang/API_baidu_ai/blob/master/picture/r2.jpg)<br>




