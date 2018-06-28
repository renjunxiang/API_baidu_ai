from aip import AipNlp
from API_baidu.config.account import account

_APP_ID = account['api']['entity_annotation']['account']['APP_ID']
_API_KEY = account['api']['entity_annotation']['account']['API_KEY']
_SECRET_KEY = account['api']['entity_annotation']['account']['SECRET_KEY']


# 调用接口分析文本
def NLP_SDK(text,
            method='depParser',
            APP_ID=_APP_ID,
            API_KEY=_API_KEY,
            SECRET_KEY=_SECRET_KEY,
            **options):
    '''
    依据百度SDK官方文档的参数名称不做任何修改:<https://ai.baidu.com/docs#/NLP-Python-SDK/top>
    :param texts: 需要打标签的文档,部分方法需要以列表形式给出配对
    :param method: 功能名称
    :param APP_ID: 项目账号信息
    :param API_KEY: 项目账号信息
    :param SECRET_KEY: 项目账号信息
    :param options: 其他可选参数
    :return: 返回百度SDK返回结果
    method 功能名称全体：
    词法分析 lexer,词法分析（定制版）lexerCustom,依存句法分析 depParser,
    词向量表示 wordEmbedding,DNN语言模型 dnnlm,词义相似度 wordSimEmbedding,短文本相似度 wordSimEmbedding,
    评论观点抽取 commentTag,情感倾向分析 sentimentClassify,文章标签 keyword,文章分类 topic
    '''
    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    # 词法分析
    if method == 'lexer':
        result = client.lexer(text, **options)
    # 词法分析（定制版）
    elif method == 'lexerCustom':
        result = client.lexerCustom(text, **options)
    # 依存句法分析
    elif method == 'depParser':
        result = client.depParser(text, **options)
    # 词向量表示
    elif method == 'wordEmbedding':
        result = client.wordEmbedding(text, **options)
    # DNN语言模型
    elif method == 'dnnlm':
        result = client.dnnlm(text, **options)
    # 词义相似度
    elif method == 'wordSimEmbedding':
        word1, word2 = text[0], text[1]
        result = client.wordSimEmbedding(word1, word2, **options)
    # 短文本相似度
    elif method == 'simnet':
        text1, text2 = text[0], text[1]
        result = client.simnet(text1, text2, **options)
    # 评论观点抽取
    elif method == 'commentTag':
        result = client.commentTag(text, **options)
    # 情感倾向分析
    elif method == 'sentimentClassify':
        result = client.sentimentClassify(text, **options)
    # 文章标签
    elif method == 'keyword':
        title, content = text[0], text[1]
        result = client.keyword(title, content, **options)
    # 文章分类
    elif method == 'topic':
        title, content = text[0], text[1]
        result = client.topic(title, content, **options)
    return result


if __name__ == '__main__':
    _text = '本区办理的营业执照且登记档案中的场地使用证明仍在有效期内，可使用《关于经营场所合法使用证明材料的情况说明》'
    result = NLP_SDK(text=_text, method='depParser')
    print(result)
