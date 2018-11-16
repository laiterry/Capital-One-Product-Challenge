# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
import urllib.request
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

# !/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser
import os

cf = configparser.ConfigParser()
# cf.read("test.ini")
cf.read("config")

print ("Program Start!!!")


#read by type
base_url = cf.get("url", "base_url")

#read int
start = cf.getint("page", "start")
end = cf.getint("page", "end")

print ("base_url:", base_url)
print ("start_page:", start)
print ("end_page:", end)




#profile_dir =r"~/Library/Application Support/Google/Chrome/Default/Cookies"

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]


def init_web_driver():
    user_agent = random.choice(my_headers) # "Mozilla/5.0"
    global driver
    #chrome_options = Options()
    chrome_options = webdriver.ChromeOptions()
    #
    #chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
    chrome_options.add_argument(user_agent)
    chrome_options.add_argument('--disable-gpu')
    driver_path = './chromedriver'  # 这里放的就是下载的driver本地路径
    #driver_path = './geckodriver'  # 这里放的就是下载的driver本地路径
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)

# 关掉driver
def close_web_driver():
    driver.quit()



def get_req(target_url):
    user_agent = "Mozilla/5.0"
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url=target_url, headers=headers)
    req = urllib.request.urlopen(request)
    return req


def category(cate_ulr):
    req = get_req(cate_ulr)
    soup = BeautifulSoup(req.read(), 'html.parser')
    sections = soup.find_all('section', 'air-card-hover air-card-hover-escape air-card-hover_tile')  # 查找所有a标签中class='title'的语句

    l=[]
    for section in sections:
        attrs = section.attrs
        if "data-ng-click" in attrs:
            s = attrs["data-ng-click"]
            s = s.split("\"")
            s = "https://www.upwork.com/o/profiles/users/_"+s[1]
            l.append(s)

    return l

cate_name = base_url.split('/')[-2]

base = base_url + "?user_pref=2&page="
url_list = []

date = time.strftime('%b %Y', time.localtime())
filetime = time.strftime('_%Y_%m_%d_%H_%I_%S', time.localtime())

urlpath = "./hourlyrate_"+cate_name+filetime+"_urls.txt"
filepath = "./hourlyrate_"+cate_name+filetime+".txt"

# with open(urlpath, "w") as file:  # 在磁盘以只写的方式打开/创建一个名为 articles 的txt文件
#     for i in range(start,end+1):
#         cate_url = base+str(i)
#         tmp_list =category(cate_url)
#         url_list.extend(tmp_list)
#         print(str(i)+": "+cate_url+" size:"+str(len(tmp_list)))
#         for url in tmp_list:
#             file.write(url+'\n')
#         file.flush()
#         time.sleep(3)
#
# print("!!!Important: Successfully get urls for users")
#
#url_list = ['https://www.upwork.com/o/profiles/users/_~016d530cd56570bfbc', 'https://www.upwork.com/o/profiles/users/_~0196bcc795c047c856', 'https://www.upwork.com/o/profiles/users/_~010e24bf71a6f4d8d2', 'https://www.upwork.com/o/profiles/users/_~01ec97334b39e7a99f', 'https://www.upwork.com/o/profiles/users/_~0128c772e6afb31933', 'https://www.upwork.com/o/profiles/users/_~01d25b90382bee4077', 'https://www.upwork.com/o/profiles/users/_~01d9c764f554779b28', 'https://www.upwork.com/o/profiles/users/_~0133b53e9c3593ef5e', 'https://www.upwork.com/o/profiles/users/_~0181b3eb2c7318081b', 'https://www.upwork.com/o/profiles/users/_~0105796c29dc26dfb5', 'https://www.upwork.com/o/profiles/users/_~01a5b18f860e7c495d', 'https://www.upwork.com/o/profiles/users/_~016e10fa5dbadcb411', 'https://www.upwork.com/o/profiles/users/_~0180f72de0fb06b175', 'https://www.upwork.com/o/profiles/users/_~01b022fbc80591e103', 'https://www.upwork.com/o/profiles/users/_~018640141f5af99a67', 'https://www.upwork.com/o/profiles/users/_~017a32f72a2239494d', 'https://www.upwork.com/o/profiles/users/_~01ec20b514fd86278a', 'https://www.upwork.com/o/profiles/users/_~010408994c1ea4feae', 'https://www.upwork.com/o/profiles/users/_~0191273e32a21186a3', 'https://www.upwork.com/o/profiles/users/_~01eb6d2b9ee53ec5bc', 'https://www.upwork.com/o/profiles/users/_~01252021cee761e0df', 'https://www.upwork.com/o/profiles/users/_~01973f3fd649e6104e', 'https://www.upwork.com/o/profiles/users/_~01ec9a012a2d7753b2', 'https://www.upwork.com/o/profiles/users/_~01d266983112823a66', 'https://www.upwork.com/o/profiles/users/_~01c8b810594347647a', 'https://www.upwork.com/o/profiles/users/_~01d3b1ac0594d17737', 'https://www.upwork.com/o/profiles/users/_~015691ddf7d6d040cf', 'https://www.upwork.com/o/profiles/users/_~01cbb6797192d2aaa1', 'https://www.upwork.com/o/profiles/users/_~013351483ee0c86748', 'https://www.upwork.com/o/profiles/users/_~017e58d3d4182ae117', 'https://www.upwork.com/o/profiles/users/_~018ca2018aee228b2f', 'https://www.upwork.com/o/profiles/users/_~01d2ddbecaa317fe66', 'https://www.upwork.com/o/profiles/users/_~0199277c77b21aeb68', 'https://www.upwork.com/o/profiles/users/_~014905c02c35e859e2', 'https://www.upwork.com/o/profiles/users/_~01e0354f61a7fbfdce', 'https://www.upwork.com/o/profiles/users/_~01cda38233c40a17d7', 'https://www.upwork.com/o/profiles/users/_~01fcb8875f2837cc4a', 'https://www.upwork.com/o/profiles/users/_~0172c6665df67001da', 'https://www.upwork.com/o/profiles/users/_~01b625339a9c2e1360', 'https://www.upwork.com/o/profiles/users/_~01a5543e4831773616', 'https://www.upwork.com/o/profiles/users/_~01a17f469d3279a4ed', 'https://www.upwork.com/o/profiles/users/_~01a7dcc06c8abde073', 'https://www.upwork.com/o/profiles/users/_~011510d776c06eedcf', 'https://www.upwork.com/o/profiles/users/_~0198142c1919375beb', 'https://www.upwork.com/o/profiles/users/_~0196db128b008df2da', 'https://www.upwork.com/o/profiles/users/_~015b53b5698e6cc864', 'https://www.upwork.com/o/profiles/users/_~0159afcb4c7ed51fe3', 'https://www.upwork.com/o/profiles/users/_~0178406fd0dc861ab4', 'https://www.upwork.com/o/profiles/users/_~01653b68c5253ec924', 'https://www.upwork.com/o/profiles/users/_~0137f3e9d035d9b04d', 'https://www.upwork.com/o/profiles/users/_~01669f73cdeb43b640', 'https://www.upwork.com/o/profiles/users/_~012e76bbd43e944732', 'https://www.upwork.com/o/profiles/users/_~01b653d45b8cbd7618', 'https://www.upwork.com/o/profiles/users/_~01d7d8b28160773a01', 'https://www.upwork.com/o/profiles/users/_~013c09d766824f5f76', 'https://www.upwork.com/o/profiles/users/_~01df307a8776209ce6', 'https://www.upwork.com/o/profiles/users/_~01ebd3ce65f77c34ef', 'https://www.upwork.com/o/profiles/users/_~0159d678d067246e26', 'https://www.upwork.com/o/profiles/users/_~010fb328ca7a63eb44', 'https://www.upwork.com/o/profiles/users/_~01bc53d88b1c329db5', 'https://www.upwork.com/o/profiles/users/_~0135b1875589f16a8a', 'https://www.upwork.com/o/profiles/users/_~01ba78e02ac325102a', 'https://www.upwork.com/o/profiles/users/_~014b7782d7610ae835', 'https://www.upwork.com/o/profiles/users/_~01e1436aba34360147', 'https://www.upwork.com/o/profiles/users/_~01a8ff98e27717d69c', 'https://www.upwork.com/o/profiles/users/_~01f7ef02792e473791', 'https://www.upwork.com/o/profiles/users/_~01903e9bd4b5c67055', 'https://www.upwork.com/o/profiles/users/_~019aa50565f25ab131', 'https://www.upwork.com/o/profiles/users/_~011b52617128455169', 'https://www.upwork.com/o/profiles/users/_~019c31c32614554ef8', 'https://www.upwork.com/o/profiles/users/_~01a8ff98e27717d69c', 'https://www.upwork.com/o/profiles/users/_~01669f73cdeb43b640', 'https://www.upwork.com/o/profiles/users/_~012e76bbd43e944732', 'https://www.upwork.com/o/profiles/users/_~01b653d45b8cbd7618', 'https://www.upwork.com/o/profiles/users/_~01d7d8b28160773a01', 'https://www.upwork.com/o/profiles/users/_~013c09d766824f5f76', 'https://www.upwork.com/o/profiles/users/_~01df307a8776209ce6', 'https://www.upwork.com/o/profiles/users/_~01ebd3ce65f77c34ef', 'https://www.upwork.com/o/profiles/users/_~0105bbf24f4b032054', 'https://www.upwork.com/o/profiles/users/_~01c1154d2eef12ac5f', 'https://www.upwork.com/o/profiles/users/_~0189e3b438b3e5a9a9', 'https://www.upwork.com/o/profiles/users/_~0143c50cb75ecc9bd4', 'https://www.upwork.com/o/profiles/users/_~017dfea6f75578d9e1', 'https://www.upwork.com/o/profiles/users/_~016f8f3ea9b6c54fea', 'https://www.upwork.com/o/profiles/users/_~0194764456ddaffa03', 'https://www.upwork.com/o/profiles/users/_~01780a966b8309ef2a', 'https://www.upwork.com/o/profiles/users/_~01a17f469d3279a4ed', 'https://www.upwork.com/o/profiles/users/_~0160db99a0b2d796cd', 'https://www.upwork.com/o/profiles/users/_~0177f6f4fa366accfe', 'https://www.upwork.com/o/profiles/users/_~01a7dcc06c8abde073', 'https://www.upwork.com/o/profiles/users/_~011510d776c06eedcf', 'https://www.upwork.com/o/profiles/users/_~0198142c1919375beb', 'https://www.upwork.com/o/profiles/users/_~0137d2bd2e6953425f', 'https://www.upwork.com/o/profiles/users/_~01439cd695a38ccf35', 'https://www.upwork.com/o/profiles/users/_~0137a38ba04e11eabc', 'https://www.upwork.com/o/profiles/users/_~01c04b9dfe2c0dffca', 'https://www.upwork.com/o/profiles/users/_~012c65d452410d39cf', 'https://www.upwork.com/o/profiles/users/_~017405b1a8a664cbdf', 'https://www.upwork.com/o/profiles/users/_~01642272ea7ca54776', 'https://www.upwork.com/o/profiles/users/_~01d8081a80e7d6fae5', 'https://www.upwork.com/o/profiles/users/_~0163cafae3182b4e6c', 'https://www.upwork.com/o/profiles/users/_~01632cf44f74358944', 'https://www.upwork.com/o/profiles/users/_~01864feb55d181054a', 'https://www.upwork.com/o/profiles/users/_~01559e299f5184f368', 'https://www.upwork.com/o/profiles/users/_~01d685b4145ea2fbac', 'https://www.upwork.com/o/profiles/users/_~017f4ac4e89327285b', 'https://www.upwork.com/o/profiles/users/_~01e7f06bc38ae7b2b2', 'https://www.upwork.com/o/profiles/users/_~01c959196dffe16d44', 'https://www.upwork.com/o/profiles/users/_~0155050ad6dd3f1758', 'https://www.upwork.com/o/profiles/users/_~015e5b32ec3c7c0344', 'https://www.upwork.com/o/profiles/users/_~01b26a12aa9616d016', 'https://www.upwork.com/o/profiles/users/_~01f81649fd5a02bbfe', 'https://www.upwork.com/o/profiles/users/_~01197f8451baadb5c7', 'https://www.upwork.com/o/profiles/users/_~016a065b7dff6c5ad6', 'https://www.upwork.com/o/profiles/users/_~011c5a10f7ae9cb2aa', 'https://www.upwork.com/o/profiles/users/_~01bd282bc1c58525f4', 'https://www.upwork.com/o/profiles/users/_~01c001017e1fc01e20', 'https://www.upwork.com/o/profiles/users/_~01e0670e8627f070bc', 'https://www.upwork.com/o/profiles/users/_~01cd0dec557f37bad9', 'https://www.upwork.com/o/profiles/users/_~01d62fd4beb180a6d1', 'https://www.upwork.com/o/profiles/users/_~01b0c277aa6f2f2954', 'https://www.upwork.com/o/profiles/users/_~0143ab7575de2bd697', 'https://www.upwork.com/o/profiles/users/_~013738c6d90cba70c9', 'https://www.upwork.com/o/profiles/users/_~01e8a343265aaa290d', 'https://www.upwork.com/o/profiles/users/_~019186db2c0456bfc0', 'https://www.upwork.com/o/profiles/users/_~01a308116469d617dc', 'https://www.upwork.com/o/profiles/users/_~015931deaa72c0b2e1', 'https://www.upwork.com/o/profiles/users/_~01c836b66074a3da3d', 'https://www.upwork.com/o/profiles/users/_~01fd74e52a837696bb', 'https://www.upwork.com/o/profiles/users/_~016a1dcb6972730cc9', 'https://www.upwork.com/o/profiles/users/_~01ec722715d191d20f', 'https://www.upwork.com/o/profiles/users/_~013785e9318a21c619', 'https://www.upwork.com/o/profiles/users/_~01eb5436591526bb2f', 'https://www.upwork.com/o/profiles/users/_~01a03cca2ac1c78e72', 'https://www.upwork.com/o/profiles/users/_~011eeda3be396c0ccb', 'https://www.upwork.com/o/profiles/users/_~01cd0b5537077f74d6', 'https://www.upwork.com/o/profiles/users/_~010e6b21d5efbf7fc9', 'https://www.upwork.com/o/profiles/users/_~01ee1d5ba1ec12fb59', 'https://www.upwork.com/o/profiles/users/_~01ae9e78631d9d822f', 'https://www.upwork.com/o/profiles/users/_~01474e9d2b2d6ae7e8', 'https://www.upwork.com/o/profiles/users/_~01694214d016d07e40', 'https://www.upwork.com/o/profiles/users/_~01148a792f76639554', 'https://www.upwork.com/o/profiles/users/_~010ccf07b505368a98', 'https://www.upwork.com/o/profiles/users/_~01e9238de2afc67885', 'https://www.upwork.com/o/profiles/users/_~015cd4fe8b43c75457', 'https://www.upwork.com/o/profiles/users/_~01072db6d4d633d8f0', 'https://www.upwork.com/o/profiles/users/_~018ca5a98184dfa193', 'https://www.upwork.com/o/profiles/users/_~019891bd7e6459be3c', 'https://www.upwork.com/o/profiles/users/_~01f3c2bcc972b8349a', 'https://www.upwork.com/o/profiles/users/_~019c867316cc98164a', 'https://www.upwork.com/o/profiles/users/_~01129294418f2be1e7', 'https://www.upwork.com/o/profiles/users/_~01f37f4bfec5071d5c', 'https://www.upwork.com/o/profiles/users/_~01b3956b1301b4192d', 'https://www.upwork.com/o/profiles/users/_~012c8b23f43e44b5ee', 'https://www.upwork.com/o/profiles/users/_~019aad63b03639b527', 'https://www.upwork.com/o/profiles/users/_~019c71caafcdbbc114', 'https://www.upwork.com/o/profiles/users/_~01327865797c79c7c9', 'https://www.upwork.com/o/profiles/users/_~0192db63c03d1f8c17', 'https://www.upwork.com/o/profiles/users/_~0178897f0040987249', 'https://www.upwork.com/o/profiles/users/_~01252021cee761e0df', 'https://www.upwork.com/o/profiles/users/_~016a32f44e742fcf2c', 'https://www.upwork.com/o/profiles/users/_~01822f685ecb55a4c2', 'https://www.upwork.com/o/profiles/users/_~01cf74ff40ff6ecad9', 'https://www.upwork.com/o/profiles/users/_~01e3c0b75873e9e2c5', 'https://www.upwork.com/o/profiles/users/_~015375d0b5ed2a91ff', 'https://www.upwork.com/o/profiles/users/_~01722ff16d2f207058', 'https://www.upwork.com/o/profiles/users/_~01f648055bf629214f', 'https://www.upwork.com/o/profiles/users/_~0105e5a59a1d44f017', 'https://www.upwork.com/o/profiles/users/_~016fd6c2cc50fda802', 'https://www.upwork.com/o/profiles/users/_~01afdf678d8b3161f3', 'https://www.upwork.com/o/profiles/users/_~01df1c61183bfc227d', 'https://www.upwork.com/o/profiles/users/_~012962fe68579ee2c4', 'https://www.upwork.com/o/profiles/users/_~0112fc10bb60c5e1e8', 'https://www.upwork.com/o/profiles/users/_~019ab9e130636a855b', 'https://www.upwork.com/o/profiles/users/_~012712ec8c065dcaa6', 'https://www.upwork.com/o/profiles/users/_~01f5c042cc538d97a0', 'https://www.upwork.com/o/profiles/users/_~011c7e46d96cbadb7c', 'https://www.upwork.com/o/profiles/users/_~01b3956b1301b4192d', 'https://www.upwork.com/o/profiles/users/_~01c6d19d9d3256adfa', 'https://www.upwork.com/o/profiles/users/_~01f7ef02792e473791', 'https://www.upwork.com/o/profiles/users/_~0196f1eab8a462a8ad', 'https://www.upwork.com/o/profiles/users/_~013738c6d90cba70c9', 'https://www.upwork.com/o/profiles/users/_~013785e9318a21c619', 'https://www.upwork.com/o/profiles/users/_~01b00267bdebb96505', 'https://www.upwork.com/o/profiles/users/_~018ff97f24bd1af7fe', 'https://www.upwork.com/o/profiles/users/_~012e1184f4a14c6592', 'https://www.upwork.com/o/profiles/users/_~0142cee9400f4fde42', 'https://www.upwork.com/o/profiles/users/_~0197b08644ccba2f00', 'https://www.upwork.com/o/profiles/users/_~01e6181192fef3699b', 'https://www.upwork.com/o/profiles/users/_~0105bbf24f4b032054']
url_list = ['https://www.upwork.com/o/profiles/users/_~01ae35ee31fa7b42f7','https://www.upwork.com/o/profiles/users/_~01afdf678d8b3161f3','https://www.upwork.com/o/profiles/users/_~013e86fe55f8504baf','https://www.upwork.com/o/profiles/users/_~014ff2f6dab34a07d8','https://www.upwork.com/o/profiles/users/_~0137f3e9d035d9b04d','https://www.upwork.com/o/profiles/users/_~0126efe05e50a1609a','https://www.upwork.com/o/profiles/users/_~01d112b14282b50470','https://www.upwork.com/o/profiles/users/_~015a799b09b9635233','https://www.upwork.com/o/profiles/users/_~013e3c764fccf17f08','https://www.upwork.com/o/profiles/users/_~014450b93bf4895df1','https://www.upwork.com/o/profiles/users/_~01d8f067fa75d830de','https://www.upwork.com/o/profiles/users/_~011ab11c540bba7bfe','https://www.upwork.com/o/profiles/users/_~01402d7c862810a63c','https://www.upwork.com/o/profiles/users/_~01c91bc5292d652bdc','https://www.upwork.com/o/profiles/users/_~012bf74ac927e02f38','https://www.upwork.com/o/profiles/users/_~019a3ddf0f81049ed4','https://www.upwork.com/o/profiles/users/_~01903e9bd4b5c67055','https://www.upwork.com/o/profiles/users/_~01878352b5802cd34c','https://www.upwork.com/o/profiles/users/_~01d5195472b9536f61','https://www.upwork.com/o/profiles/users/_~010f3edce56c955909','https://www.upwork.com/o/profiles/users/_~019816bd474f2ae511','https://www.upwork.com/o/profiles/users/_~011ced33ee45d0c4fb','https://www.upwork.com/o/profiles/users/_~01250cdaad842eced7','https://www.upwork.com/o/profiles/users/_~010169ae6c4fa107fa','https://www.upwork.com/o/profiles/users/_~0114600f80ea10ef15','https://www.upwork.com/o/profiles/users/_~019ab969da788ee18e','https://www.upwork.com/o/profiles/users/_~01712a166073edd2b6','https://www.upwork.com/o/profiles/users/_~013b06b500240474a3','https://www.upwork.com/o/profiles/users/_~0196c49e3592b2dde0','https://www.upwork.com/o/profiles/users/_~01f2ea500ada208f61','https://www.upwork.com/o/profiles/users/_~01d6d8a513eb985edc','https://www.upwork.com/o/profiles/users/_~01aba22ce392462a9f','https://www.upwork.com/o/profiles/users/_~01e06edc22120bdc6b','https://www.upwork.com/o/profiles/users/_~01c8b810594347647a','https://www.upwork.com/o/profiles/users/_~01306f071e676bb7fe','https://www.upwork.com/o/profiles/users/_~01e5008888d2a2aebc','https://www.upwork.com/o/profiles/users/_~0149a3d462ad71ae72','https://www.upwork.com/o/profiles/users/_~01aeb5a8ba5e1d2e5e','https://www.upwork.com/o/profiles/users/_~017904f681fe28e2c1','https://www.upwork.com/o/profiles/users/_~016f47c829fe8e6fcf','https://www.upwork.com/o/profiles/users/_~0149a3d462ad71ae72','https://www.upwork.com/o/profiles/users/_~01aeb5a8ba5e1d2e5e','https://www.upwork.com/o/profiles/users/_~01f2d778b9555e23ce','https://www.upwork.com/o/profiles/users/_~0195bca293add4bdec','https://www.upwork.com/o/profiles/users/_~01ab413f62da6c0497','https://www.upwork.com/o/profiles/users/_~01551f9282233437ec','https://www.upwork.com/o/profiles/users/_~01e8579306f41a503b','https://www.upwork.com/o/profiles/users/_~016afce6e21601f54a','https://www.upwork.com/o/profiles/users/_~014f08d2ee46d32164','https://www.upwork.com/o/profiles/users/_~0132e95d537c457424','https://www.upwork.com/o/profiles/users/_~01fb00d9267afc4395','https://www.upwork.com/o/profiles/users/_~01eec5b92e4d165ee6','https://www.upwork.com/o/profiles/users/_~01eb6d2b9ee53ec5bc','https://www.upwork.com/o/profiles/users/_~01d2ddbecaa317fe66','https://www.upwork.com/o/profiles/users/_~01e9811f43aa8834c2','https://www.upwork.com/o/profiles/users/_~01044c237be3848ef4','https://www.upwork.com/o/profiles/users/_~01f2385135834ef12d','https://www.upwork.com/o/profiles/users/_~012340b1ccf6b36ffc','https://www.upwork.com/o/profiles/users/_~014b5dc9450794684a','https://www.upwork.com/o/profiles/users/_~01061b0ec6b5356f23','https://www.upwork.com/o/profiles/users/_~01b4c1c4ab936fda8d','https://www.upwork.com/o/profiles/users/_~01b596ae377de66528','https://www.upwork.com/o/profiles/users/_~019e8d3d2a5f671049','https://www.upwork.com/o/profiles/users/_~0137be8026fbf9241d','https://www.upwork.com/o/profiles/users/_~0184aea1de968f46c5','https://www.upwork.com/o/profiles/users/_~015b714621ebf0c666','https://www.upwork.com/o/profiles/users/_~01420620fdc7158c75','https://www.upwork.com/o/profiles/users/_~017f722af51291bd5b','https://www.upwork.com/o/profiles/users/_~01fd5a7913dbc7a87a','https://www.upwork.com/o/profiles/users/_~016ec112600134bd09','https://www.upwork.com/o/profiles/users/_~011f9f2e1b7d05b2e0','https://www.upwork.com/o/profiles/users/_~018c4c5c670419ad71','https://www.upwork.com/o/profiles/users/_~010cc1394261fd0428','https://www.upwork.com/o/profiles/users/_~01a1a389d10ee2a8a8','https://www.upwork.com/o/profiles/users/_~01dff551ef9b489fa9','https://www.upwork.com/o/profiles/users/_~01aa2818426fec5227','https://www.upwork.com/o/profiles/users/_~01ebf1c2e0b39b58c8','https://www.upwork.com/o/profiles/users/_~01ba7a0e1667523c5e','https://www.upwork.com/o/profiles/users/_~017e58d3d4182ae117','https://www.upwork.com/o/profiles/users/_~0144c712297f32967f','https://www.upwork.com/o/profiles/users/_~019ab9e130636a855b','https://www.upwork.com/o/profiles/users/_~0125a6674a4becf862','https://www.upwork.com/o/profiles/users/_~011831e0c358614042','https://www.upwork.com/o/profiles/users/_~0114f916f8b743cc68','https://www.upwork.com/o/profiles/users/_~019d41b5f642e23f20','https://www.upwork.com/o/profiles/users/_~0177decff0ec4a3e69','https://www.upwork.com/o/profiles/users/_~01db7bdb99e83b3f46','https://www.upwork.com/o/profiles/users/_~0172c6665df67001da','https://www.upwork.com/o/profiles/users/_~0163414a4565245261','https://www.upwork.com/o/profiles/users/_~01a7820571aa253bcd','https://www.upwork.com/o/profiles/users/_~012063950baa07b066','https://www.upwork.com/o/profiles/users/_~017cff120a21b290ba','https://www.upwork.com/o/profiles/users/_~0195d64598b6865b73','https://www.upwork.com/o/profiles/users/_~017896d361f321eab8','https://www.upwork.com/o/profiles/users/_~01327865797c79c7c9','https://www.upwork.com/o/profiles/users/_~01a2b698951fa0944a','https://www.upwork.com/o/profiles/users/_~01cf30fc284f2c05e1','https://www.upwork.com/o/profiles/users/_~01ee6c7ba1078298e8','https://www.upwork.com/o/profiles/users/_~0146d695245ed38c6a','https://www.upwork.com/o/profiles/users/_~015a185a99ed3ceca7','https://www.upwork.com/o/profiles/users/_~0114fa02902e5fb426','https://www.upwork.com/o/profiles/users/_~0172480835212ab344','https://www.upwork.com/o/profiles/users/_~01dbe2ac03cb8fe0b0','https://www.upwork.com/o/profiles/users/_~01abc79ec14ce5e353','https://www.upwork.com/o/profiles/users/_~01aa5550779dc9de18','https://www.upwork.com/o/profiles/users/_~01b7e6b8969bc24982','https://www.upwork.com/o/profiles/users/_~014c050501bbe6f9f4','https://www.upwork.com/o/profiles/users/_~01873179d3fb47fdbf','https://www.upwork.com/o/profiles/users/_~01df38464d646f2c7a','https://www.upwork.com/o/profiles/users/_~014be17126f3ac4a9e','https://www.upwork.com/o/profiles/users/_~01095dcf4d56a6d548','https://www.upwork.com/o/profiles/users/_~01712210b842b5083c','https://www.upwork.com/o/profiles/users/_~01fb7203c8f923785b','https://www.upwork.com/o/profiles/users/_~0109cb304e3aa9eebf','https://www.upwork.com/o/profiles/users/_~019a1d160511d69522','https://www.upwork.com/o/profiles/users/_~0198a1b4433d6a8e4a','https://www.upwork.com/o/profiles/users/_~015b56a2f663b2008c','https://www.upwork.com/o/profiles/users/_~01fc9dfc9eed0323c3','https://www.upwork.com/o/profiles/users/_~014a4a4c9955619b1e','https://www.upwork.com/o/profiles/users/_~01e9f9d09f9010f6cd','https://www.upwork.com/o/profiles/users/_~0168b98a01ef8ffa13','https://www.upwork.com/o/profiles/users/_~01a6db14dda8dd9424','https://www.upwork.com/o/profiles/users/_~01608e60ad09f7cad3','https://www.upwork.com/o/profiles/users/_~0192032781301316c2','https://www.upwork.com/o/profiles/users/_~013f145c849c59673e','https://www.upwork.com/o/profiles/users/_~01d52787f5d7e4e37f','https://www.upwork.com/o/profiles/users/_~01ed1f48409a6b400a','https://www.upwork.com/o/profiles/users/_~015a20727939db6e6f','https://www.upwork.com/o/profiles/users/_~014eaca6242b15bb73','https://www.upwork.com/o/profiles/users/_~016a79c54178dd1829','https://www.upwork.com/o/profiles/users/_~01a1e3de94ea60731c','https://www.upwork.com/o/profiles/users/_~015d5efbf6bb02ff03','https://www.upwork.com/o/profiles/users/_~011809902177699089','https://www.upwork.com/o/profiles/users/_~0181727e26e0b11732','https://www.upwork.com/o/profiles/users/_~015f5eeeffbb22f0c7','https://www.upwork.com/o/profiles/users/_~01b68ac6ff2a769f19','https://www.upwork.com/o/profiles/users/_~010ace102573237bfe','https://www.upwork.com/o/profiles/users/_~014fb464912e299e48','https://www.upwork.com/o/profiles/users/_~0149f94b09aaaea31a','https://www.upwork.com/o/profiles/users/_~01ac184b63bc469ea2','https://www.upwork.com/o/profiles/users/_~015b1032d2938319a8','https://www.upwork.com/o/profiles/users/_~014fb464912e299e48','https://www.upwork.com/o/profiles/users/_~01f41bc3283cf5ae90','https://www.upwork.com/o/profiles/users/_~01710fabc5ab147d41','https://www.upwork.com/o/profiles/users/_~01c959196dffe16d44','https://www.upwork.com/o/profiles/users/_~01746cf1b469d863e5','https://www.upwork.com/o/profiles/users/_~0154423b1ccda9e785','https://www.upwork.com/o/profiles/users/_~0128ae464e34993888','https://www.upwork.com/o/profiles/users/_~01c41f165aae068d68','https://www.upwork.com/o/profiles/users/_~0136aae49a2941c17a','https://www.upwork.com/o/profiles/users/_~0149025008cd321523','https://www.upwork.com/o/profiles/users/_~01257e8d443ceafead','https://www.upwork.com/o/profiles/users/_~010a7249c89d9263e2','https://www.upwork.com/o/profiles/users/_~01d7a6df848eaa52c6','https://www.upwork.com/o/profiles/users/_~019db3a5be0bdc7211','https://www.upwork.com/o/profiles/users/_~01bc6ab7d08fc3f858','https://www.upwork.com/o/profiles/users/_~0159fa6d77e41e1c8c','https://www.upwork.com/o/profiles/users/_~01178fc08a7d265e99','https://www.upwork.com/o/profiles/users/_~014c520f4d2970e641','https://www.upwork.com/o/profiles/users/_~01bf41246a3f5d439b','https://www.upwork.com/o/profiles/users/_~01d2bcd186a750cd4e','https://www.upwork.com/o/profiles/users/_~014a4f6d43b7e0f563','https://www.upwork.com/o/profiles/users/_~01adbd81f24f85c987','https://www.upwork.com/o/profiles/users/_~018fde6e259a9bdbec','https://www.upwork.com/o/profiles/users/_~012253a0fe284441d8','https://www.upwork.com/o/profiles/users/_~01658daa4f1f7127a5','https://www.upwork.com/o/profiles/users/_~011a800321bcbb197d','https://www.upwork.com/o/profiles/users/_~01a9354243d4c8f18a','https://www.upwork.com/o/profiles/users/_~0130b5a3f48c6f4a2c','https://www.upwork.com/o/profiles/users/_~0131681a311f3e3785','https://www.upwork.com/o/profiles/users/_~0131681a311f3e3785','https://www.upwork.com/o/profiles/users/_~01e9c49119213a8b3a','https://www.upwork.com/o/profiles/users/_~01afefc96eaac2a534','https://www.upwork.com/o/profiles/users/_~0162dc8de6938c267b','https://www.upwork.com/o/profiles/users/_~01577069b4bf5d5952','https://www.upwork.com/o/profiles/users/_~013351483ee0c86748','https://www.upwork.com/o/profiles/users/_~0177f6f4fa366accfe','https://www.upwork.com/o/profiles/users/_~01532f64e769b5a8bb','https://www.upwork.com/o/profiles/users/_~01281a9e47c87c140a','https://www.upwork.com/o/profiles/users/_~01ba8e941fd30e14a0','https://www.upwork.com/o/profiles/users/_~0180701802dd0eed10','https://www.upwork.com/o/profiles/users/_~01608b13f94cb4e3ed','https://www.upwork.com/o/profiles/users/_~01e71dde8f41f3ce0b','https://www.upwork.com/o/profiles/users/_~0194e7d7be49267be5','https://www.upwork.com/o/profiles/users/_~01e3b2064628c88c61','https://www.upwork.com/o/profiles/users/_~01f4d26e1369e149dc','https://www.upwork.com/o/profiles/users/_~01997a95debfff0eae','https://www.upwork.com/o/profiles/users/_~01cc1f03f6b048624f','https://www.upwork.com/o/profiles/users/_~017ae8dc1859e1ff06','https://www.upwork.com/o/profiles/users/_~0129f4acebe08b96d2','https://www.upwork.com/o/profiles/users/_~01b0f722c783c7a8d8','https://www.upwork.com/o/profiles/users/_~01bf0fe7b637c1cb33','https://www.upwork.com/o/profiles/users/_~01669f73cdeb43b640','https://www.upwork.com/o/profiles/users/_~01a572700e7f88ff41','https://www.upwork.com/o/profiles/users/_~01678661f791c138cf','https://www.upwork.com/o/profiles/users/_~01ec20b514fd86278a','https://www.upwork.com/o/profiles/users/_~01518828ead02559aa','https://www.upwork.com/o/profiles/users/_~0121393c8a99dba48e','https://www.upwork.com/o/profiles/users/_~0128d8938152fa53f7','https://www.upwork.com/o/profiles/users/_~01f4f3ab9d459abd3c']
time.sleep(3)


hourly_salaries = []

pattern = re.compile(r'([a-zA-Z]{3})(\s{1})([0-9]{4})')
init_web_driver()
reg = r'(\d+)'
with open(filepath, "w") as file:  # 在磁盘以只写的方式打开/创建一个名为 articles 的txt文件
    for url in url_list:
        driver.get(url)
        driver.implicitly_wait(3)  # wait up to 10 seconds for the elements to become available
        html = driver.page_source    # 获取网页html
        html_soup = BeautifulSoup(html,"lxml")

        if "Upwork Access Denied" in html_soup.text:
            name = input("Please verify that you are not a robot")
            print('Continue' + name)

        hr = html_soup.find_all('div', 'pull-right lead m-0-top-bottom')  # 查找所有a标签中class='title'的语句
        hist = html_soup.find_all('small', 'text-muted nowrap ng-binding')

        skills = html_soup.find_all('a', "o-tag-skill ng-binding ng-scope")

        skills_str = ","
        for skill in skills:
            s = skill.text
            s= s.strip()
            skills_str+=(s+"_")
        skills_str = skills_str[0:len(skills_str)-1]
        print(skills_str)
        uid = url.split("~")[1]
        if len(hr)>=1:
            money = hr[0].contents[2].contents[1].contents[0].split("$")[1]
            hourly_salaries.append(money)
            file.write(uid+','+date + ',' + cate_name + ',' + money + skills_str+'\n')
            file.flush()

        for h in hist:
            p = h.parent.parent.parent.parent.parent
            s = p.text
            m = pattern.search(s)
            month = m.group()
            money = h.contents[0].split(" ")[0].split("$")[1]
            file.write(uid+','+month + ',' + cate_name + ',' + money + skills_str+'\n')
            file.flush()

        time.sleep(5)

close_web_driver()









