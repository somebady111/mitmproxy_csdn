import csv
import json
# import pymongo

# client = pymongo.MongoClient('10.0.0.106')
# db = client['csdn']
# collection = db['artical_list']

def response(flow):
    # global collection
    url = 'https://gw.csdn.net/cms-app/v1/home_page/may_login/list_recomment_articles'
    if flow.request.url.startswith(url):
        text = flow.response.text
        datas = json.loads(text)
        details = datas.get('data').get('articles')
        for detail in details:

            # result = {
            #     'url':detail.get('url'),
            #     'created_at':detail.get('created_at'),
            #     'title':detail.get('title'),
            #     'summary':detail.get('summary'),
            #     'nickname':detail.get('nickname'),
            #     'views':detail.get('views'),
            #     'comments':detail.get('comments'),
            # }
            # collection.insert(result)

            url = detail.get('url')
            created_at = detail.get('created_at')
            title = detail.get('title')
            summary = detail.get('summary')
            nickname = detail.get('nickname')
            views = detail.get('views'),
            comments = detail.get('comments')

            with open('article_list.csv','a+') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['url','created_at','title','summary','nickname','views','comments'])
                writer.writerow([url,created_at,title,summary,nickname,views,comments])
