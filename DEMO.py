from API_baidu import NLP_SDK, entity_annotation, face_detect
import os

text = '委托他人申请的，还须提交委托书、委托代理人或指定代表身份证明（如身份证、外籍人员护照等）原件、复印件'
results = entity_annotation(text=text)
print(results)

text = '本区办理的营业执照且登记档案中的场地使用证明仍在有效期内，可使用《关于经营场所合法使用证明材料的情况说明》'
result = NLP_SDK(text=text, method='depParser')
print(result)

base_path = os.path.dirname(__file__)
results = face_detect(image_path=base_path + '/API_baidu/picture/e1.jpg',
                      show=True,
                      savepath=None)
print(results)
