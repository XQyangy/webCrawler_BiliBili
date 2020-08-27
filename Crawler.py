import requests

import re

import json

import  pandas as pd


headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"

}

num = 100

data = pd.DataFrame(columns=('senddate', 'title', 'video_id', 'video_review', 'duration', 'favorites', 'author', 'author_id', 'play'))

for i in range(num):

    url = 'https://s.search.bilibili.com/cate/search?callback=jqueryCallback_bili_&main_ver=v3&' \
          'search_type=video&view_type=hot_rank&order=click&' \
          'copy_right=-1&cate_id=201&page=' + str(i) + '&pagesize=20&jsonp=jsonp&' \
          'time_from=2020819&time_to=20200826'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        # text = re.findall(re.compile(r'[(](.*?)[)]', re.S), response.text)

        # text = text[0].encode('utf-8').decode('unicode_escape')

        text = response.text.replace("jqueryCallback_bili_", "")

        text = text[1:len(text) - 1]

        text = json.loads(text)

        result = text['result']

        for x in range(len(result)):

            print(result[x]['author'])

            lst = pd.Series({'senddate':result[x]['senddate'], 'title':result[x]['title'], 'video_id':result[x]['id'],
                             'video_review':result[x]['video_review'], 'duration':result[x]['duration'],
                             'favorites':result[x]['favorites'], 'author':result[x]['author'], 'author_id':result[x]['mid'],
                             'play':result[x]['play']})

            data = data.append(lst, ignore_index=True)

    else:

        pass

print(data)

data.to_excel('favorites_rank_videos.xls')


