#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
from urllib import parse, request


# processCode=PROC-5FYJPUKV-0QZ38C5I36DEU88X7HCM3-PARDRNTJ-E&dirId=169b2c4d7461abc811a3d68424d8417f

def getToken():
    appkey = 'dingye2q9buvbuyhpxvz'
    appsecret = 'v2eoOjGtEfL0EDZLB3d__Y2OjOO0YG0SWvIZ_OSDFon6wIRkpVDn7IK53AonRPs3'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }
    url = 'https://oapi.dingtalk.com/gettoken?appkey=%s&appsecret=%s' % (appkey, appsecret)
    req = urllib.request.Request(url, headers=headers)
    result = urllib.request.urlopen(req)
    access_token = json.loads(result.read())
    print(access_token)
    return access_token['access_token']


def postApproval(storyListStr, bugListStr):
    access_token = getToken()
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }
    url = 'https://oapi.dingtalk.com/topapi/processinstance/create?access_token=%s' % (access_token)

    data = {
        'process_code': 'PROC-5FYJPUKV-0QZ38C5I36DEU88X7HCM3-PARDRNTJ-E',
        'originator_user_id': '1415050452960922',
        'dept_id': '25450641',
        'approvers': '1415050452960922',
        'form_component_values': [{'name': '发布需求', 'value': storyListStr}, {'name': '发布缺陷', 'value': bugListStr}]
    }

    data1 = json.dumps(data).encode(encoding='UTF8')

    # req = urllib.request.Request(url, headers=headers, data=data1)
    # result = urllib.request.urlopen(req)
    # list = json.loads(result.read())

    req = request.Request(url=url, data=data1, headers=headers)
    res = request.urlopen(req)
    list = json.loads(res.read())

    print(list)

#
# if __name__ == '__main__':
#     postApproval = postApproval()
#     print(postApproval)
