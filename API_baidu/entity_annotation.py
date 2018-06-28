from API_baidu.config.account import account
from API_baidu.get_token import get_token
import json
import requests

APP_ID = account['api']['entity_annotation']['account']['APP_ID']
API_KEY = account['api']['entity_annotation']['account']['API_KEY']
SECRET_KEY = account['api']['entity_annotation']['account']['SECRET_KEY']


# 调用接口分析文本
def entity_annotation(text,
                      API_KEY=API_KEY,
                      SECRET_KEY=SECRET_KEY):
    '''
    :param texts: 需要打标签的文档列表
    :param API_KEY: 项目账号信息
    :param SECRET_KEY: 项目账号信息
    :return: 百度API返回结果
    '''
    # 获取access_token
    access_token = get_token(API_KEY, SECRET_KEY)

    # 调百度实体识别接口文档:<http://ai.baidu.com/docs#/EntityAnnotation-API/top>
    url = account['api']['entity_annotation']['url']
    params = {'access_token': access_token}
    headers = {'Content-Type': account['api']['entity_annotation']['Content-Type']}
    data = json.dumps({'data': text})
    r = requests.post(url=url,
                      params=params,
                      headers=headers,
                      data=data)
    result = json.loads(r.text)
    return result


if __name__ == '__main__':
    _text = '委托他人申请的，还须提交委托书、委托代理人或指定代表身份证明（如身份证、外籍人员护照等）原件、复印件'
    results = entity_annotation(text=_text)
    print(results)
