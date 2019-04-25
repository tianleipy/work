from chenhuan.dingtalk import postApproval
from chenhuan.grab3 import start

if __name__ == '__main__':
    try:
        storyListStr, bugListStr = start()
        postApproval(storyListStr, bugListStr)
    except:
        print("未找到发布计划")