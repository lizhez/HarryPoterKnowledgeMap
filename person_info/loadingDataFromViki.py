import csv
import urllib.request
import urllib.parse
from lxml import etree
import re

result = {'姓名': '', '别名': '', '饰演': '', '生日': '', '性别': '', '简介': '', '性格特点': '', '外貌': '',
          '魔杖': ''}
person_list = []


# 获取人名
def get_name():
    # 打开人物关系表
    with open("data/relation.csv", "r", encoding="utf-8") as csvfile:
        readers = csv.reader(csvfile)
        for line in readers:
            # 人物关系表中，一个人会对应很多种关系，所以会有很多行数据，而我们只要一行
            if line[0] not in person_list:
                # 第一列对应人物名字
                person_list.append(line[0])
        # 第一行是表头，删去
        del person_list[0]
        csvfile.close()


# 打开网页，获取网页内容
def url_open(url, datafrom):
    if datafrom == "baidu":
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
            # 'Accept': '*/*',
            'Cookie': 'BAIDUID=F05F2D250326B8F64E124A2E5F98890F:FG=1; BAIDUID_BFESS=F05F2D250326B8F64E124A2E5F98890F:FG=1; __bid_n=184f4e32b67586162f4207; PSTM=1673112256; delPer=0; BD_CK_SAM=1; PSINO=7; BIDUPSID=1BF9B2E811474D0A204167C3AFCACF96; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BD_UPN=12314753; BA_HECTOR=0g0hah0585010g2k0500alhe1hrjakg1l; ZFY=Zryyc6Mcd6tlhhbTIZ8yLqn2ocsN5odLjnE:AeNusVTg:C; B64_BOT=1; BDUSS=FXM3c0a3R-NUpPM3FIeFc2YkpZWGprMTgyT2NhS3MtVXVMSG1rdjlOTDZOLUZqRUFBQUFBJCQAAAAAAAAAAAEAAAAy8h1~3rLD18-3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPqquWP6qrljYW; BDUSS_BFESS=FXM3c0a3R-NUpPM3FIeFc2YkpZWGprMTgyT2NhS3MtVXVMSG1rdjlOTDZOLUZqRUFBQUFBJCQAAAAAAAAAAAEAAAAy8h1~3rLD18-3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPqquWP6qrljYW; sugstore=1; ab_sr=1.0.1_NWE5MTM2NmJlMzc2NDE3NWNmMDVlYTBiMDYwYmEzZTQxODc4ZmEyZGIzZDM1MjRmZDg2ZDNmMmU5MmFiNDMwNThhZmYwYjE1OTQ3YTlhMjVjMWZkMmUwMGY1ZmVmNjRhNTY0ZmNjMDA0MWNjM2U0MjM2ZTY1OGUxZmE4MGNkZGMyMzNjZjE3ZGQzZWQxYWFjNjVkOTY2YzQxNjJmN2ZlMmUzMzMzNzgwNzcwYzg4NTYwYTYyNThkNTA2YjQ2Y2Uy; RT="sl=15&ss=lcm7c543&tt=1rdl&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=4lmlv0yqjdx&ld=lm9k"; H_PS_PSSID=; channel=so.lenovo.com.cn; H_PS_645EC=8993UxLK3NZ6iWFAEmI5HrT%2BP5reExBRJTs0QZspaM%2BBtXnWZMS5414GzXmG%2BjckJVE1Dw; baikeVisitId=0d52afeb-e9bc-4162-a4ab-17f6bbda4407; BDSVRTM=176'
        }
    else:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'cookie': 'WMF-Last-Access=09-Jan-2023; WMF-Last-Access-Global=09-Jan-2023; GeoIP=JP:13:Tokyo:35.69:139.69:v4; zhwikimwuser-sessionId=10df95fe94fa73c63945; zhwikiBlockID=415029%21c9d64fba99bc1b619ebebe1dcee39175d715bd68c5269a6723f6efaf4bb1ed4fa3295c0c1a7305a3ae483ba87ad70e8aa6b64dcecfedccf9a58e99c30ee1f45b; zhwikiwmE-sessionTickLastTickTime=1673242107982; zhwikiwmE-sessionTickTickCount=11',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
    request = urllib.request.Request(url=url, headers=headers)
    try:
        response = urllib.request.urlopen(request)
    except Exception:
        return None
    content = response.read().decode('utf-8')
    if "https://baike.baidu.com/error.html" in content:
        return None
    if response.status != 200:
        print("internet error")
    return content


# 获取魔杖信息
def magic_wand():
    magic_keywords = urllib.parse.quote('魔杖')
    magic_url = 'https://baike.baidu.com/item/' + magic_keywords
    magic_data = url_open(magic_url, "baidu")
    magic_tree = etree.HTML(magic_data)
    # 创建魔杖和角色对应的字典
    owner_magic_wand = {}
    # 获取魔杖拥有者信息
    owner_data = magic_tree.xpath('//div[starts-with(@class,"para")][position()>125][position()<147]/a/text()')
    # 获取魔杖信息
    magic_wand_data = magic_tree.xpath('//div[starts-with(@class,"para")][position()>125][position()<147]/text()')
    for m in range(len(owner_data)):
        # 分割魔杖信息，只要最重要的一部分信息
        magic_temp = magic_wand_data[m].replace('——', '').split("。")
        owner_magic_wand[owner_data[m]] = magic_temp[0]
    return owner_magic_wand


# 从百度百科获取人物信息
def info_from_baidu(name, keywords):
    url = 'https://baike.baidu.com/item/' + keywords
    if name == "哈利·波特":
        url = 'https://baike.baidu.com/item/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9/799457?fromModule=lemma_sense-layer#viewPageContent'
    data = url_open(url, "baidu")
    if data is None:
        return None
    tree = etree.HTML(data)
    name_data = []
    value_data = []
    # 获取属性名
    name_node = tree.xpath('//div/dl/dt[@class="basicInfo-item name"]')
    # 因为得到的数据中有\xa0，将其用‘’replace掉
    for i in range(len(name_node)):
        name_data.append(name_node[i].xpath("string(.)").replace('\xa0', ''))
    # 获取属性信息
    value_node = tree.xpath('//div/dl/dd[@class="basicInfo-item value"]')
    for i in range(len(name_node)):
        value_data.append(value_node[i].xpath("string(.)").replace('\n', ''))
    # 根据属性名和属性信息获取存储在list中的位置一一对应
    for i in range(len(name_data)):
        if name_data[i] == '别名':
            result['别名'] = value_data[i]
        if name_data[i] == '饰演':
            result['饰演'] = value_data[i]
        if name_data[i] == '生日':
            result['生日'] = value_data[i]
        if name_data[i] == '性别':
            result['性别'] = value_data[i]
    # 获取简介
    describe = tree.xpath('//div[starts-with(@class,"para")]')
    # 人物的简介比较长的，我们只关心它的最主要的简介，也就是第一段简介
    result['简介'] = describe[0].xpath("string(.)")
    return "success"


# 从viki百科获取信息
def info_from_viki(keywords):
    url = 'https://zh.wikipedia.org/wiki/' + keywords
    if name == "哈利·波特":
        url = 'https://zh.wikipedia.org/wiki/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9_(%E8%A7%92%E8%89%B2)'
    data = url_open(url, "viki")
    if data is None:
        return None
    tree = etree.HTML(data)
    # 获得所有h2和h3标签
    tag = tree.xpath('//div[@class="mw-parser-output"]/h2 | //div[@class="mw-parser-output"]/h3')
    # 获得所有h2，h3和p标签
    pdata = tree.xpath(
        '//div[@class="mw-parser-output"]/p | //div[@class="mw-parser-output"]/h2 | //div[@class="mw-parser-output"]/h3')
    # 维基百科上人物的外观和性格都有对应的h2标签，标签中的内容如下：
    toComplex1 = "外观上"
    toComplex2 = "性格上"
    count = ''
    charCount = 0
    character = ''
    # 找到h2标签中内容为“性格下”的下一个h2或者h3标签中内容，记录在count中
    for j in range(len(tag)):
        trs = tag[j].xpath("string(.)")
        if trs == toComplex2:
            j = j + 1
            count = tag[j].xpath("string(.)")
            break
    # 找到对应性格和外貌的p标签，并将它们的内容分别保存在character和appearance中
    for i in range(len(pdata)):
        trs = pdata[i].xpath("string(.)")
        if trs == toComplex1:
            i = i + 1
            appearance = pdata[i].xpath("string(.)")
            temp = re.sub('[\d]', '', appearance).replace('[]', '').replace('\n', '')
            result['外貌'] = temp
        if charCount == 1 and trs != count:
            pdata_list = trs.replace('\n', '').split("。")
            toSimple = pdata_list[0] + "。"
            character = character + toSimple
        if trs == toComplex2:
            charCount = 1
        if trs == count:
            break
    result['性格特点'] = character
    return "success"


# json to csv
def json_to_csv(result):
    print(result)
    csv_file = open('data/data.csv', 'a', newline='', encoding='utf8')
    writer = csv.writer(csv_file)
    for i in range(len(result)):
        keys = result[i].keys()
        writer.writerow(keys)
        break

    for data in result:
        for key in keys:
            if key not in data:
                data[key] = ''
        writer.writerow(data.values())
    csv_file.close()


if __name__ == '__main__':
    # 获取人名
    get_name()
    # 获取魔杖信息
    owner_magic_wand = magic_wand()

    result_data = []
    for i in range(len(person_list)):
        name = person_list[i]
        if owner_magic_wand.get(name) is not None:
            result['魔杖'] = owner_magic_wand.get(name)
        keywords = urllib.parse.quote(name)
        status = info_from_baidu(name, keywords)
        if status is None:
            for j in result.keys():
                result[j] = ''
        else:
            info_from_viki(keywords)
        result['姓名'] = name
        result_data.append(
            {'姓名': result['姓名'], '别名': result['别名'], '饰演': result['饰演'], '生日': result['生日'], '性别': result['性别'],
             '魔杖': result['魔杖'], '简介': result['简介'], '外貌': result['外貌'], '性格特点': result['性格特点']})
        for j in result.keys():
            result[j] = ''
    json_to_csv(result_data)