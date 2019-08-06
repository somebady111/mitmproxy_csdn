import csv
import json

def response(flow):
    # 通过打印判断出是否是需求的内容或者是检查请求的response查看年请求到的内容
    # 如果打印，会出现让人承载不下的结果导致无法确定目标url或者按键q退出，检查请求
    url = 'https://gw.csdn.net/cms-app/v1/blog_details/may_login/get_article_details_info_html?from=home&bloggerUserName=qq_43431158'
    if flow.request.url.startswith(url):
        text = flow.response.text
        print(text)
