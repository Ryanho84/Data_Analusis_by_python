'''
目前还没有完善。
1. 如果下载的图片非常多的话，可以增加一个进度条来显示下载的进度
2. 目前使用xpath的方式爬去图片，没有模拟翻页的功能，智能爬去第一页的内容，如何改进？

'''



#coding:utf-8


import requests
import json
import os
from lxml import etree
from selenium import webdriver


query = '猫咪'
downloadPath = 'C:/Users/Ryanho/Desktop/images/'

'''download Pics'''
def download(src, id):
    dir = downloadPath + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout = 10)
    except requests.exception.ConnectionError:
        print('Can not download pictures!')
    
    if not os.path.exists(downloadPath):
        os.makedirs(downloadPath)
    if os.path.exists(dir):
        print('Pic has been existed: '+ id)
        return
    #pic_content = pic.decode('utf-8','ignore')
    fp = open(dir,'wb')
    fp.write(pic.content)
    fp.close()

def searchImages():
    #request all url
    for i in range(0, 235431,20):
        url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)
        #return results
        html = requests.get(url).text
        print('html'+html)
        #exchange JSON objs to python objs
        response = json.loads(html, encoding = 'utf-8')
        for image in response['images']:
            #download the url of image
            print(image['src'])
            #download the pic
            download(image['src'], image['id'])
    
def getImages():
    #get images by Xpath
    url = 'https://movie.douban.com/subject_search?search_text='+query+'&cat=1002'
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get(url)
    html = etree.HTML(driver.page_source)
    #using xpath helper
    src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
    title_xpath = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
        
    srcs = html.xpath(src_xpath)
    #print(srcs)
    titles = html.xpath(title_xpath)
    for src, title in zip(srcs, titles):
        #print('\t'.join([str(src),str(title.text)]))
        download(src, title.text)
    
#getImages()
searchImages()