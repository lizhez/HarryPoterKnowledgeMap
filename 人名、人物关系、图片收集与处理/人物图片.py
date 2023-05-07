
import urllib.request
from lxml import etree

def create_request(url_list):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
        'cookie': '__yjs_duid=1_bda85a6addb3bbc6a16efaeddec25efd1641642370978; BIDUPSID=3B9FAE85121EB52FECF015A4644884AA; PSTM=1650899500; BAIDU_WISE_UID=wapp_1655882624659_885; ZFY=h2L1T0NAnTmB2H5klybp79wFFpCdnJxER:BYltjGVlN8:C; BAIDUID=0143A0E8A44AF5E2EA6930B659908DF8:FG=1; BAIDUID_BFESS=0143A0E8A44AF5E2EA6930B659908DF8:FG=1; BDUSS=jN4Q1YwNW9afkJJU35mN0NFNGdNUTRyMDIyV1hUbnREcllPdn55d09KeU5vTVpqRVFBQUFBJCQAAAAAAAAAAAEAAABCYinwxL7Evs311MLIy83BzcEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI0Tn2ONE59jb; BDUSS_BFESS=jN4Q1YwNW9afkJJU35mN0NFNGdNUTRyMDIyV1hUbnREcllPdn55d09KeU5vTVpqRVFBQUFBJCQAAAAAAAAAAAEAAABCYinwxL7Evs311MLIy83BzcEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI0Tn2ONE59jb; RT="z=1&dm=baidu.com&si=0j50xz5q4fmc&ss=lcn0tcit&sl=0&tt=0&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ul=n4&hd=ns"; H_PS_PSSID=36554_37973_37647_37906_38015_36920_37989_37936_37874_26350_37957_22160_37881; BA_HECTOR=2g0l2l842h2g2h010h84a0nm1hrkuk91l; delPer=0; PSINO=2; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_ZDhlN2Y3MTdlMjFmYjg2OTkwMDI3YTM4NDNmYzY1N2I2MTIzNDUzZTE0YTE1ZjJiOTc4ZWIzNjU0MjNmYmE4NjlhMGJkNDdjYzdjODc5YTJjY2MyMTFjNjAyOGZlYzkxMmY1MWZjMWE0M2FlOTNkMmY2Njg4ZWZjZTNlMDFmZjFlZmFmOWJkOTA1NTM0YjEyN2QzYTJiNWEwMjA2NjVmYmQwNjNmODBkODUzZTQxNzdmYmY0YWYzYWIwNTVlYjQ3'

    }
    for i in range(len(url_list)):
        request = urllib.request.Request(url=url_list[i], headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        # 下载图片
        # urllib.request.urlretrieve('图片地址','文件的名字')
        tree = etree.HTML(content)  # 解析服务器文件
        name_list = tree.xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/a/img/@alt')
        # 一般设计图片的网站都会进行懒加载   所以这里的图片地址为src2
        src_list = tree.xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/a/img/@src')

        print(src_list)
        print(name_list)
        urllib.request.urlretrieve(url=src_list[0], filename='./Img/' + name_list[0] + '.jpg')

# def get_content(request):#获取网页源码
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
#     return content


# def down_load(content):#下载
#     #下载图片
#     #urllib.request.urlretrieve('图片地址','文件的名字')
#     tree = etree.HTML(content)#解析服务器文件
#     name_list = tree.xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/a/img/@alt')
#     #一般设计图片的网站都会进行懒加载   所以这里的图片地址为src2
#     src_list = tree.xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/a/img/@src')
#
#     print(src_list)
#     print(name_list)
#     urllib.request.urlretrieve(url=src_list[0],filename='./Img/' +name_list[0] + '.jpg')


if __name__ == '__main__':
    url_list=['https://baike.baidu.com/item/%E9%97%AA%E9%97%AA/19520959'
        ,'https://baike.baidu.com/item/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9/799457?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%A5%A5%E5%88%A9%E5%A7%86%C2%B7%E9%A9%AC%E5%85%8B%E8%A5%BF%E5%A7%86/6273525'
        ,'https://baike.baidu.com/item/%E8%B4%9D%E6%8B%89%E7%89%B9%E9%87%8C%E5%85%8B%E6%96%AF%C2%B7%E8%8E%B1%E6%96%AF%E7%89%B9%E5%85%B0%E5%A5%87?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%BE%B7%E6%8B%89%E7%A7%91%C2%B7%E9%A9%AC%E5%B0%94%E7%A6%8F?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E9%98%BF%E4%B8%8D%E6%80%9D%C2%B7%E7%8F%80%E8%A5%BF%E7%93%A6%E5%B0%94%C2%B7%E4%BC%8D%E5%B0%94%E5%BC%97%E9%87%8C%E5%85%8B%C2%B7%E5%B8%83%E8%B5%96%E6%81%A9%C2%B7%E9%82%93%E5%B8%83%E5%88%A9%E5%A4%9A?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%A4%9A%E6%AF%94/2115762?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%8E%84%E5%B0%BC%C2%B7%E9%BA%A6%E5%85%8B%E7%B1%B3%E5%85%B0?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E4%BC%8F%E5%9C%B0%E9%AD%94/1127381?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E8%8A%99%E8%93%89%C2%B7%E5%BE%B7%E6%8B%89%E5%BA%93%E5%B0%94?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%87%A4%E5%87%B0%E7%A6%8F%E5%85%8B%E6%96%AF?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E6%A0%BC%E9%9B%B7%E6%88%88%E9%87%8C%C2%B7%E9%AB%98%E5%B0%94?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E9%B2%81%E4%BC%AF%C2%B7%E6%B5%B7%E6%A0%BC?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E8%B5%AB%E6%95%8F%C2%B7%E6%A0%BC%E5%85%B0%E6%9D%B0?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E9%87%91%E5%A6%AE%C2%B7%E9%9F%A6%E6%96%AF%E8%8E%B1?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%BA%B7%E5%A5%88%E5%88%A9%C2%B7%E7%A6%8F%E5%90%89?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E6%96%87%E6%A3%AE%E7%89%B9%C2%B7%E5%85%8B%E6%8B%89%E5%B8%83?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%85%8B%E5%88%A9%E5%88%87?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E8%8E%B1%E5%A7%86%E6%96%AF%C2%B7%E7%BA%A6%E7%BF%B0%C2%B7%E5%8D%A2%E5%B9%B3?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%8D%A2%E5%A8%9C%C2%B7%E6%B4%9B%E5%A4%AB%E5%8F%A4%E5%BE%B7?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%8D%A2%E4%BF%AE%E6%96%AF%C2%B7%E9%A9%AC%E5%B0%94%E7%A6%8F?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E7%BD%97%E6%81%A9%C2%B7%E9%9F%A6%E6%96%AF%E8%8E%B1?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E7%B1%B3%E5%8B%92%E5%A8%83%C2%B7%E9%BA%A6%E6%A0%BC?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E7%BA%B3%E5%A8%81%C2%B7%E9%9A%86%E5%B7%B4%E9%A1%BF?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E7%8F%80%E8%A5%BF%C2%B7%E4%BC%8A%E6%A0%BC%E5%86%85%E4%BF%AE%E6%96%AF%C2%B7%E9%9F%A6%E6%96%AF%E8%8E%B1/60268554'
        ,'https://baike.baidu.com/item/%E7%A7%8B%C2%B7%E5%BC%A0?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%A1%9E%E5%BE%B7%E9%87%8C%E5%85%8B%C2%B7%E8%BF%AA%E6%88%88%E9%87%8C?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E6%91%84%E9%AD%82%E6%80%AA?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E8%A5%BF%E5%BC%97%E5%8B%92%E6%96%AF%C2%B7%E6%96%AF%E5%86%85%E6%99%AE?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%85%8B%E9%B2%81%E5%A7%86/15081619?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%A4%9A%E6%B4%9B%E9%9B%B7%E6%96%AF%C2%B7%E4%B9%8C%E5%A7%86%E9%87%8C%E5%A5%87?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%B0%8F%E7%9F%AE%E6%98%9F%E5%BD%BC%E5%BE%97?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E5%B0%8F%E5%A4%A9%E7%8B%BC%E6%98%9F%C2%B7%E5%B8%83%E8%8E%B1%E5%85%8B?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E4%BA%9A%E7%91%9F%C2%B7%E9%9F%A6%E6%96%AF%E8%8E%B1?fromModule=lemma_search-box'
        ,'https://baike.baidu.com/item/%E4%BC%8A%E6%88%88%E5%B0%94%C2%B7%E5%8D%A1%E5%8D%A1%E6%B4%9B%E5%A4%AB?fromModule=lemma_search-box'

              ]
    create_request(url_list)
