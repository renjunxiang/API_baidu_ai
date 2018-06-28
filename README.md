# API_baidu_ai
[![](https://img.shields.io/badge/Python-3.5-blue.svg)](https://www.python.org/)
[![](https://img.shields.io/badge/baidu--aip-2.1.0.0-brightgreen.svg)](https://pypi.python.org/pypi/baidu-aip/2.1.0.0)
[![](https://img.shields.io/badge/requests-2.18.4-brightgreen.svg)](https://pypi.python.org/pypi/requests/2.18.4)
**百度人工智能平台API封装**

## 功能说明
### 获取平台的access_token
get_token.py：需要API_KEY和SECRET_KEY，在config/account.py中请自行修改账号信息，开通账号完全免费<br>
**提供的个人项目账号信息仅为了方便使用者进行测试，账号有每日调用上限，禁止传播和任何商业化使用，学术研究需经本人许可！**

### 调用平台的SDK做自然语言处理
NLP_SDK.py：公测以后百度推荐使用SDK方式，因此对其做了简单的封装，需要APP_ID、API_KEY和SECRET_KEY，返回字典<br>
![](https://github.com/renjunxiang/API_baidu_ai/blob/master/picture/entity_annotation.jpg)<br>

### 调用平台的API做实体识别
entity_annotation.py：需要API_KEY和SECRET_KEY，返回字典
![](https://github.com/renjunxiang/API_baidu_ai/blob/master/picture/depParser.jpg)<br>

### 调用平台的API做人脸检测
face_detect.py：需要API_KEY和SECRET_KEY，返回字典，选择是否返回图片
![](https://github.com/renjunxiang/API_baidu_ai/blob/master/picture/e2.jpg)<br>
![](https://github.com/renjunxiang/API_baidu_ai/blob/master/picture/r2.jpg)<br>




