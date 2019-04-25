import time
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, date, timedelta

host = 'http://172.23.0.131:8088'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
data = {
    'account': 'tianlei',
    'password': '669fe228883354abb53f9973dce0b7c3',
    'keepLogin%5B%5D': 'on',
    'referer': 'http%3A%2F%2F172.23.0.131%3A8088%2Fzentao%2Fproductplan-browse-1.html'
        }
s = requests.session()
r = s.post(host + '/zentao/user-login.html',data=data)

def get_path():#获取最新计划请求路径和日期
    html = s.get(host + "/zentao/productplan-browse-1.html",headers=header).content
    soup1 = BeautifulSoup(html,'lxml')
    #获取最新计划单路径两种方法
    #path = (soup1.find_all('a',href=re.compile("/zentao/productplan-view-(.*?).html"))[0]).get('href')
    a = []
    try:
        #riqi = (soup1.find_all('a',href=re.compile("/zentao/productplan-view-(.*?).html"))[0]).string.split("发")[0]
        riqi = re.findall('.html">(.*?)发布计划</a>',str(soup1))
        date = []
        for i in riqi:
            if '.' or '/' in i:
                i = i.replace('.', '-').replace('/', '-').strip()
            date.append(i)
        a.append(date)
    except:
        return ("没有获取到计划")
    try:
        path = re.findall(r'<a href="(/zentao/productplan-view-.*?)">', str(soup1))
        #print(path)
        a.append(path)
    except:
        return ("没有获取到计划")
    return a
def get_info(a):#获取bug或者需求内容信息
    i = 0
    j = 1
    content = ""
    while i < len(a):
        xuhao = (re.findall(r"view-(.*?).html", a[i])[0])
        title = (a[i + 1].split(">")[1])
        str = ("%d: %s %s" % (j,title, xuhao))
        content += str + "\n"
        i += 2
        j += 1
    return content
def panduan(a):
    if a == 0:#判断今天是否在发布计划日期中以来确定有无发布计划
        now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if now in get_path()[0]:
            i = get_path()[0].index(now)
            return int(i)
        else:
            return False
    else:#判断昨天是否有发布计划
        yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
        if yesterday in get_path()[0]:
            i = get_path()[0].index(yesterday)
            return int(i)
        else:
            return False
def start():
    if type(panduan(0)) is int:
        html2 = s.get(host + get_path()[1][panduan(0)], headers=header).content
        soup2 = BeautifulSoup(html2, 'lxml')
        bug = re.findall(r'<a href="(/zentao/bug-view.*?)</a>', str(soup2))
        xuqiu = re.findall(r'<a href="(/zentao/story-view.*?)</a>', str(soup2))
        #print(bug)
        #print(xuqiu)
        storyListStr = get_info(xuqiu)
        bugListStr = get_info(bug)
        return storyListStr, bugListStr

def get_info2(a):#需求或ｂｕｇ的字典
    i = 0
    content = {}
    while i < len(a):
        xuhao = (re.findall(r"view-(.*?).html", a[i])[0])
        title = (a[i + 1].split(">")[1])
        content[xuhao] = title
        i += 2
    return content
def get_sorb(tp):#入参1得到需求，其他bug
    if type(panduan(2)) is int:
        html2 = s.get(host + get_path()[1][panduan(2)], headers=header).content
        soup2 = BeautifulSoup(html2, 'lxml')
        xuqiu = re.findall(r'<a href="(/zentao/story-view.*?)</a>', str(soup2))
        bug = re.findall(r'<a href="(/zentao/bug-view.*?)</a>', str(soup2))
        if tp == 1:
            a = xuqiu
            return get_info2(a)
        else:
            a = bug
            return get_info2(a)
    else:
        return {}
#print(get_sorb(1))