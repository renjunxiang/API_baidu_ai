from API_baidu.config.account import account
from API_baidu.get_token import get_token
import json
import requests
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

_API_KEY = account['api']['face_detect']['account']['API_KEY']
_SECRET_KEY = account['api']['face_detect']['account']['SECRET_KEY']


# 调用接口分析文本
def face_detect(API_KEY=_API_KEY,
                SECRET_KEY=_SECRET_KEY,
                image_path=None,
                max_face_num=10,
                show=True,
                savepath=None):
    '''
    :param API_KEY: 项目账号信息
    :param SECRET_KEY: 项目账号信息
    :param image_path: 图片路径
    :param max_face_num: 监测人脸数,不超过10
    :param show: 是否显示结果,默认Ture
    :param savepath: 监测后图片保存路径,默认None
    :return: 百度API分析结果,dict
    '''
    # 获取access_token:<http://ai.baidu.com/docs#/Auth/top>
    access_token = get_token(API_KEY, SECRET_KEY)

    f = open(image_path, 'rb')  # 二进制方式打开图文件
    f_base64 = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()

    # 调百度实体识别接口:<http://ai.baidu.com/docs#/EntityAnnotation-API/top>
    url = account['api']['face_detect']['url']
    params = {'access_token': access_token}
    headers = {'Content-Type': account['api']['face_detect']['Content-Type']}
    face_field = 'age,beauty,expression,faceshape,gender,glasses,landmark,race,quality,facetype'
    # face_field = 'landmark'
    data = json.dumps({'image': f_base64.decode(),
                       'image_type': 'BASE64',
                       'max_face_num': max_face_num,
                       'face_field': face_field})
    r = requests.post(url=url,
                      params=params,
                      headers=headers,
                      data=data)
    result = json.loads(r.text)

    if result['error_msg'] == 'pic not has face':
        print('picture dose not have face')
    else:
        if show or savepath:
            lena = mpimg.imread(image_path)
            n = max(lena.shape[0] / 25, lena.shape[0] / 16)
            plt.figure(figsize=[lena.shape[1] / n, lena.shape[0] / n])
            plt.axis('off')
            plt.imshow(lena)
            line_width = 1
            line_color = 'blue'
            scatter_size = 10
            scatter_color = 'yellow'
            for i in result['result']['face_list']:
                landmark72 = i['landmark72']
                x = [i['x'] for i in landmark72]
                y = [i['y'] for i in landmark72]

                plt.scatter(x=x, y=y, s=scatter_size, c=scatter_color)
                # 脸
                plt.plot(x[0:13],
                         y[0:13],
                         linewidth=line_width,
                         color=line_color)
                # 左眼
                plt.plot(x[13:22],
                         y[13:22],
                         linewidth=line_width,
                         color=line_color)
                # 左睫毛
                plt.plot(x[22:29] + x[22:23],
                         y[22:29] + y[22:23],
                         linewidth=line_width,
                         color=line_color)
                # 右眼
                plt.plot(x[30:39],
                         y[30:39],
                         linewidth=line_width,
                         color=line_color)
                # 右睫毛
                plt.plot(x[39:47] + x[39:40],
                         y[39:47] + y[39:40],
                         linewidth=line_width,
                         color=line_color)
                # 鼻子
                plt.plot(x[47:57] + x[47:48],
                         y[47:57] + y[47:48],
                         linewidth=line_width,
                         color=line_color)
                plt.plot([x[51], x[57], x[52], x[51]],
                         [y[51], y[57], y[52], y[51]],
                         linewidth=0.5,
                         color=line_color)
                # 嘴巴
                plt.plot([x[58], x[59], x[60], x[61], x[62]],
                         [y[58], y[59], y[60], y[61], y[62]],
                         linewidth=line_width,
                         color=line_color)
                plt.plot([x[58], x[66], x[67], x[68], x[62]],
                         [y[58], y[66], y[67], y[68], y[62]],
                         linewidth=line_width,
                         color=line_color)
                plt.plot([x[58], x[71], x[70], x[69], x[62]],
                         [y[58], y[71], y[70], y[69], y[62]],
                         linewidth=line_width,
                         color=line_color)
                plt.plot([x[58], x[65], x[64], x[63], x[62]],
                         [y[58], y[65], y[64], y[63], y[62]],
                         linewidth=line_width,
                         color=line_color)
                plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
            if savepath:
                plt.savefig(savepath)
            if show:
                plt.show()

    return result


if __name__ == '__main__':
    import os

    base_path = os.path.dirname(__file__)
    results = face_detect(API_KEY=_API_KEY,
                          SECRET_KEY=_SECRET_KEY,
                          image_path=base_path+'/picture/e1.jpg',
                          show=True,
                          savepath=base_path+'/picture/r1.jpg')
    print(results)
