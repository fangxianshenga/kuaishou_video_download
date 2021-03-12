## 简介
----
可以在[快手](https://video.kuaishou.com/?utm_source=wwwkuaishoucom&utm_medium=wwwkuaishoucom&utm_campaign=wwwkuaishoucom&location=wwwkuaishoucom)搜索下载或者下载用户全部视频。

## 主要功能
--------------------
-  快手视频下载

## 运行环境
--------------------
- windows
- python3

## 第三方库
--------------------
- 需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令
pip install -r requirements.txt
- 如果国内安装第三方库比较慢，可以使用以下指令进行清华源加速 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

## 使用教程
--------------------

1. 安装谷歌浏览器及谷歌驱动，两者版本要一致(这里给的是87.0.4280.88版本的)，谷歌不是这个版本的需要自行下载对应版本[驱动](http://npm.taobao.org/mirrors/chromedriver/) 把安装的谷歌目录添加到环境变量中(path)。

2. 把chromdriver分别添加到浏览器的安装目录，python安装目录Scripts文件夹中,重启电脑。


3. 打开命令提示符(菜单+R,输入cmd即可打开)，在命令运行中输入以下命令会弹出谷歌浏览器界面：
```python
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
```
4. 在新弹出谷歌浏览器框里打开快手网址，登入。
5. 搜索下载：输入搜索条件，手动下拉到底部。运行`快手搜索下载视频.py`![在这里插入图片描述](https://img-blog.csdnimg.cn/20210312145533284.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lleWVkZXdlbg==,size_16,color_FFFFFF,t_70)
6. 用户下载：打开用户界面，手动下拉到底部。运行`快手用户视频下载.py`
![在这里插入图片描述](https://img-blog.csdnimg.cn/202103121503015.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lleWVkZXdlbg==,size_16,color_FFFFFF,t_70)
