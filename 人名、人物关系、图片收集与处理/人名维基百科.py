import urllib.request

url='https://zh.wikipedia.org/wiki/%E5%93%88%E5%88%A9%E6%B3%A2%E7%89%B9%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'cookie':'WMF-Last-Access=09-Jan-2023; WMF-Last-Access-Global=09-Jan-2023; GeoIP=SG::Singapore:1.29:103.85:v4; zhwikimwuser-sessionId=a1889d10da9163f902e5; zhwikiBlockID=420306!5d23ffc2ccc215f79ddd1ac0703ebda201155912f8ac5b17ac732157e22b60ac46dfe8f4f8332e7f2b299293360acaaba3b43d051b7b96f9cc599324bc24344a; zhwikiwmE-sessionTickLastTickTime=1673245491531; zhwikiwmE-sessionTickTickCount=8'
    ,'accept-language': 'zh-CN,zh;q=0.9'
}
#request对象，因为参数顺序问题，不能直接写url，headers，中间还有一个data，所以要关键字传参
request=urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)
# 获取源码数据
content=response.read().decode('utf-8')
# print(content)

#解析
from lxml import etree

#解析服务器响应文件
tree=etree.HTML(content)

# 表格外的
#获取数据 返回是列表类型，可以用【0】来拿第一个
# result=tree.xpath('//input[@id="su"]/@value')
# result=tree.xpath('/html/body/div[3]/div[3]/div[1]/text()')
result4=tree.xpath('//*[@id="mw-content-text"]/div[1]/ul/li/b/text()')
result5=tree.xpath('//*[@id="mw-content-text"]/div[1]/ul/li/b/a/text()')

# print(result1)
# print(result2)
# result1.extend(result2)
# print(result1)

# 表格里的没有超链接的
# result=tree.xpath('//*[@id="NavFrame1"]/div[2]/table/tbody/tr[5]/td[1]/text()')
# result=tree.xpath('//*[@id="NavFrame1"]/div[2]/table/tbody/tr[13]/td[1]/text()')
# result=tree.xpath('//*[@id="mw-content-text"]/div[1]/div[3]/div[2]/table/tbody/tr[2]/td[1]/text()')
result=tree.xpath('//*[@id="mw-content-text"]/div[1]/div[3]/div[2]/table/tbody/tr/td[1]/text()')
# print(result)

# result3 = list(filter(lambda x : x != '\n', result))
result3=[x.strip() for x in result if x.strip()!='']
print(result3)

# # 有超链接的
result2=tree.xpath('//*[@id="mw-content-text"]/div[1]/div[3]/div[2]/table/tbody/tr/td[1]/a/text()')
print(result2)
#
# # 主角 现各学院学生
result1=tree.xpath('//*[@id="mw-content-text"]/div[1]/div[3]/div[2]/table/tbody/tr/td[1]/b/a/text()')
print(result1)

total_result=result1+result2+result3+result4+result5
# total_result=result4+result5
# # 转成简体字
# L1 = []
# import opencc
# cc = opencc.OpenCC('t2s')
# for x in total_result:#这块类型转换挺麻烦的str对象加入到list
#     s = cc.convert(x)
#     L1 += [s]
# print(L1)
#
#   # L1 = ['This']


import pandas as pd
name=['name']
test=pd.DataFrame(columns=name,data=total_result)
test.to_csv('e:/testcsv.csv',index=False,encoding='utf-8-sig')
