# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import requests
import os

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'} #模拟的浏览器头文件
        r = requests.get(url,headers=kv) #模拟浏览器访问
        r.raise_for_status() #如果状态非200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return  len(r.text)
    except:
        return "产生异常"
#百度搜索提交关键字
def baidu():
    keyword = "Python"
    try:
        kv = {'wd','keyword'}
        r = requests.get("http://www.baidu.com/s",params=kv)#params：字典或字节序列,作为参数增加到url中
        print(r.request.url)
        r.raise_for_status() #如果状态非200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return  len(r.text)
    except:
        return "产生异常"
#爬取图片
def Get_pic(url):
    root = "D://pics//"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("保存成功")
        else:
            print("文件存在")
    except:
        print("爬取失败！")
#爬取视频 直接合并
def Get_vod(url):
    root = "D://Vods//"
    path = root + url.split('/')[-3]+".ts"
    kv = {'user-agent': 'Mozilla/5.0'}
    i=0
    try:
        with open(path,'ab') as f:
            for i in range(0,200):
                i=i+1
                url1 =url+str(i)+".ts"
                r = requests.get(url1,headers=kv)
                r.raise_for_status() #如果状态非200，引发HTTPError异常
                f.write(r.content)
                print(url1)
            f.close()
    except:
        if i in (0,1):
            print("无此资源！")
            os.remove(path)
        else:
            print("下载完毕！")

def Get_src(url):
    root = "D://Vods//"+ url.split('/')[-3] +"//"

    kv = {'user-agent': 'Mozilla/5.0'}
    i,f=0,0
    try:
        for i in range(0,3000):
            i=i+1
            f=i
            url1 =url+str(i)+".ts"
            path = root +url.split('/')[-3]+str(i).zfill(3) +".ts"
            if not os.path.exists(path):
                r = requests.get(url1, headers=kv)
                r.raise_for_status()  # 如果状态非200，引发HTTPError异常
                if not os.path.exists(root):
                    os.mkdir(root)
                else:
                    with open(path,'wb') as f:
                        print(url1)
                        f.write(r.content)
                        f.close()
    except:
        if f in (0,1):
            print("无此资源！")
        else:
            print("下载完毕！")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url0 = "https://x.1spcdn.com/play/"
    for t in range(122328,122500):
        t=t+1
        url=url0+str(t)+"/720/play"
        print(url)
        Get_src(url)
 #   print(getHTMLText(url))
 #   print(Len("https://x.1spcdn.com/play/122043/720/play"))
 #   Get_vod(url0)
 #   url = "https://x.1spcdn.com/play/122043/720/play.m3u8"





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
