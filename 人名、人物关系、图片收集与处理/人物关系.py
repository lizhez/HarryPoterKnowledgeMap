import csv
import urllib.request
import pandas as pd

clist=[]
with open ("E:testcsv.csv",'r')as p:
    reader=csv.reader(p)
    for row in reader:
        clist.append(float(row[0]))#拼接读出来的这一行第一列


def get(url):
    url = 'https://baike.baidu.com/item/%E7%BD%97%E6%81%A9%C2%B7%E9%9F%A6%E6%96%AF%E8%8E%B1/5019332'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
        'cookie': '__yjs_duid=1_bda85a6addb3bbc6a16efaeddec25efd1641642370978; BIDUPSID=3B9FAE85121EB52FECF015A4644884AA; PSTM=1650899500; BAIDU_WISE_UID=wapp_1655882624659_885; ZFY=h2L1T0NAnTmB2H5klybp79wFFpCdnJxER:BYltjGVlN8:C; BAIDUID=0143A0E8A44AF5E2EA6930B659908DF8:FG=1; BAIDUID_BFESS=0143A0E8A44AF5E2EA6930B659908DF8:FG=1; BDUSS=jN4Q1YwNW9afkJJU35mN0NFNGdNUTRyMDIyV1hUbnREcllPdn55d09KeU5vTVpqRVFBQUFBJCQAAAAAAAAAAAEAAABCYinwxL7Evs311MLIy83BzcEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI0Tn2ONE59jb; BDUSS_BFESS=jN4Q1YwNW9afkJJU35mN0NFNGdNUTRyMDIyV1hUbnREcllPdn55d09KeU5vTVpqRVFBQUFBJCQAAAAAAAAAAAEAAABCYinwxL7Evs311MLIy83BzcEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI0Tn2ONE59jb; RT="z=1&dm=baidu.com&si=0j50xz5q4fmc&ss=lcn0tcit&sl=0&tt=0&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ul=n4&hd=ns"; H_PS_PSSID=36554_37973_37647_37906_38015_36920_37989_37936_37874_26350_37957_22160_37881; BA_HECTOR=2g0l2l842h2g2h010h84a0nm1hrkuk91l; delPer=0; PSINO=2; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_ZDhlN2Y3MTdlMjFmYjg2OTkwMDI3YTM4NDNmYzY1N2I2MTIzNDUzZTE0YTE1ZjJiOTc4ZWIzNjU0MjNmYmE4NjlhMGJkNDdjYzdjODc5YTJjY2MyMTFjNjAyOGZlYzkxMmY1MWZjMWE0M2FlOTNkMmY2Njg4ZWZjZTNlMDFmZjFlZmFmOWJkOTA1NTM0YjEyN2QzYTJiNWEwMjA2NjVmYmQwNjNmODBkODUzZTQxNzdmYmY0YWYzYWIwNTVlYjQ3'

    }
    # request对象，因为参数顺序问题，不能直接写url，headers，中间还有一个data，所以要关键字传参
    request = urllib.request.Request(url=url, headers=headers)
    # 模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(request)
    # 获取源码数据
    content = response.read().decode('utf-8')
    # print(content)

    # 解析
    from lxml import etree

    # 解析服务器响应文件
    tree = etree.HTML(content)
    # print(content)


    name = []
    relation = []
    num = tree.xpath('//div/dl/dt[@class="basicInfo-item name"]/text()')
    for i in range(len(num)):
        name[i] = tree.xpath('//*[@id="J-lemma-complex-relationship-swiper"]/div/div[1]/a[i]/div[2]/text()')
        relation[i] = tree.xpath('//*[@id="J-lemma-complex-relationship-swiper"]/div/div[1]/a[i]/div[3]/text()')
        col_name = ['entity1', 'entity2', 'relation']
        test = pd.DataFrame(columns=col_name, data=[clist[i], name[i], relation[i]])
        test.to_csv('e:/testcsv.csv', index=False, encoding='utf-8-sig')


url1='https://baike.baidu.com/item/'
url2='?fromModule=lemma_search-box'



for i in range(len(clist)):
    name = urllib.parse.quote(clist[i])
    url=url1+name+url2
    get(url)


