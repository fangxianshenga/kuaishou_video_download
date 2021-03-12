# -*- encoding=utf8 -*-
'''
time:2021.3.8
抓取的url是 'https://video.kuaishou.com/profile/3xh53y6gh8iumy9
采用的是打开的浏览器采集的
采集数量超过了就会报错。
'''


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


    translate = 1  #搜索排名,视频的命名

    def run(self):
        ##设置接管理管Chrome浏览器
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # chromedriver = r'D:\Python\Python38\Scripts\chromedriver.exe'
        self.driver = webdriver.Chrome(options=chrome_options)
        print(self.driver.title)
        ##作品数量
        num = self.driver.find_element_by_xpath('//div[@class="user-detail-info"]//h3').text
        print(num)


        for a in range(int(self.translate),int(num)+1):
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/div/div[1]/div[2]/div/div/div/div[%s]' % a).click()
            WebDriverWait(self.driver,1000).until(EC.presence_of_element_located((By.CLASS_NAME,'player-video')))
            url_video = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/div/div[1]/div[2]/div[1]/div[2]/video').get_attribute('src')
            # video.append(url_video)
            try:
                self.video_download(url_video)
            except:
                print('已全部下载')
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
            os.mkdir(os.path.dirname(os.path.abspath(__file__)) + './' + 'ran')
        except:
            print('文件夹存在，自动生成失败。')

        with open('.\\ran\\%s.mp4' % self.translate, 'ab') as tp:

            tp.write(res)

        print('第%s个视频下载已下载' % self.translate)


def start():
    start = KuaiShou()
    start.run()

if __name__ == '__main__':
    start()