from API_baidu.config.account import account
import json
import requests


# 调用接口分析文本
def get_token(API_KEY, SECRET_KEY):
    '''
    针对HTTP API调用者
    百度AIP开放平台使用OAuth2.0授权调用开放API
    调用API时必须在URL中带上accesss_token参数
    :param API_KEY: 应用信息
    :param SECRET_KEY: 应用信息
    :return: access_token
    '''
    # 获取access_token:<http://ai.baidu.com/docs#/Auth/top>
    url = account['access_token_url']
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    r = requests.post(url, params=params)
    token = json.loads(r.text)['access_token']
    r.close()

    return token


if __name__ == '__main__':
    API_KEY = 'MOzTi8637GaWn2RZuZDYGamR'
    SECRET_KEY = 'VLIzOvOLLhSQF8DNUtqDEr2Ly04lURxg'
    token = get_token(API_KEY=API_KEY,
                      SECRET_KEY=SECRET_KEY)
    print(token)
