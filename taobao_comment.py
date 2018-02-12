
# coding: utf-8

# In[ ]:


import requests
import re
#从第一个列表页获取评论数和商品id（构造网址的）
shangpinurl = 'https://s.taobao.com/search?q=xiaomi&imgfile=&commend=all&ssid=s5-e&search_type=item' \
              '&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
res = requests.get(shangpinurl)
res.encoding = res.apparent_encoding
txt = res.text
nid = re.findall('"nid":"(\d+)"', txt)
comments_count = re.findall('"comment_count":"(\d+)"', txt)

# 请求单个商品的所有评论detail文件并保存
for id, num in zip(nid, comments_count):
    comments_page_num = int(num)//10 + 1
    filename = id + '.txt'
    
    with open(filename, 'a') as f:
        for i in range(comments_page_num):
            page = i + 1
            url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + str(id) + '&sellerId=1776456424&order=3&currentPage=' + str(page) + '&pageSize=10&&callback=_DLP_2510_der_3_currentPage_' + str(page) + '_pageSize_10_'
            res3 = requests.get(url)
            print(id + '-' + str(page))
            f.write(res3.text)
        

