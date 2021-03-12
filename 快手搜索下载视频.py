'**coding:utf-8'
'''
抓取的url是 'https://video.kuaishou.com/search/video?searchKey=%E8%B7%B3%E8%88%9E
采用的是打开的浏览器采集的
采集数量超过了就会报错。
'''

import re
import os
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class KuaiShou(object):
    '''
    # def __int__(self):
        self.translate = 1  #搜索排名,视频的命名

        self.file = input('请命名一个文件夹名称用于保存下载后的视频:')
        try:
            self.new_file = os.mkdir(os.path.dirname(os.path.abspath(__file__)) + './' + self.file)
        except:
            ...
        # 当前的路径
        self.now_path = os.path.dirname(os.path.abspath(__file__))
        self.now_file_path = os.path.join(now_path, file)
    '''

    translate = 1  # 搜索排名,视频的命名

    def run(self):
        ##设置接管理管Chrome浏览器
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chromedriver = r'D:\Python\Python38\Scripts\chromedriver.exe'
        # self.driver = webdriver.Chrome(chromedriver, options=chrome_options)
        self.driver = webdriver.Chrome(options=chrome_options)

        # video = []
        for a in range(1,1000):
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/div/div/div[2]/div[1]/div/div[1]/div[%s]/div[1]/div/div[1]/img' % a).click()
            WebDriverWait(self.driver,1000).until(EC.presence_of_element_located((By.CLASS_NAME,'player-video')))
            url_video = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/div/div[1]/div[2]/div[1]/div[2]/video').get_attribute('src')
            # video.append(url_video)
            self.video_download(url_video)
            self.driver.back()
            sleep(2)
            self.translate += 1

    ##下载视频
    def video_download(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        }

        res = requests.get(url, headers=headers).content

        try:
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + './' + 'kuaishou')
        except:
            ...

        with open('.\\kuaishou\\%s.mp4' % self.translate, 'ab') as tp:

            tp.write(res)

        print('第%s个视频下载已下载....' % self.translate)


def start():
    start = KuaiShou()
    start.run()

if __name__ == '__main__':
    start()