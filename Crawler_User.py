# -*- coding: utf-8 -*-
import requests

import json

import time

import pandas as pd



def get_basicInformation(lst):

    web = 'https://space.bilibili.com/'

    data = pd.DataFrame(columns=('mid', 'name', 'website', 'title', 'sex'))

    for mid in lst:

        url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(mid) + '&jsonp=jsonp'

        response = requests.get(url)

        if response.status_code == 200:

            text = response.text

            result = json.loads(text)['data']

            lst = pd.Series({'mid': result['mid'], 'name': result['name'], 'website': web + str(result['mid']),
                              'title': result['official']['title'], 'sex': result['sex']})

            data = data.append(lst, ignore_index=True)

        else:

            pass

        time.sleep(0.5)

    return data


def get_userFollow(lst):

    data = pd.DataFrame(columns=( 'following', 'follower'))

    for mid in lst:

        url = 'https://api.bilibili.com/x/relation/stat?vmid=' + str(mid) + '&jsonp=jsonp'

        response = requests.get(url)

        if response.status_code == 200:

            text = response.text

            result = json.loads(text)['data']

            lst = pd.Series({'following': result['following'], 'follower': result['follower']})

            data = data.append(lst, ignore_index=True)

        else:

            pass

        time.sleep(0.5)

    return data


def get_userView(lst):

    cookie = '_uuid=785AE5E9-2472-4446-8C9C-76DD9FD4F98C90883infoc; buvid3=8D4CC2B0-A49E-407C-ACD4-9C9AD4B3C6CE138368infoc; PVID=1; sid=4yk8bgri; DedeUserID=18355093; DedeUserID__ckMd5=4244e6a65bac0eea; SESSDATA=72e5c8a4%2C1614000102%2C982be*81; bili_jct=cc6f99fb7a2c638261141e9e3e79c858; bfe_id=0c3a1998eda2972db3dbce4811a80de6'

    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6814.400 QQBrowser/10.3.3005.400",
        #    'Connection': 'keep-alive',
        #    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #    'referer': 'https://space.bilibili.com/7428971',
        'Cookie': cookie

    }

    data = pd.DataFrame(columns=('view', 'article_view', 'likes'))

    for mid in lst:

        url = 'https://api.bilibili.com/x/space/upstat?mid=' + str(mid) + '&jsonp=jsonp'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            text = response.text

            result = json.loads(text)['data']

            lst = pd.Series({'view': result['archive']['view'], 'article_view': result['article']['view'], 'likes': result['likes']})

            data = data.append(lst, ignore_index=True)

        else:

            pass

        time.sleep(0.5)

        print(mid)

    return data


if __name__ == '__main__':

    data1 = pd.read_excel('favorites_rank_videos.xls', headers=0)

    lst = list(set(data1['author_id'].tolist()))

    lst.remove(319458128)

    data1 = get_basicInformation(lst)

    data2 = get_userFollow(lst)

    data3 = get_userView(lst)

    data = pd.concat([data1, data2, data3], axis=0)

    print(data)

    data.to_excel('user_information.xls')









# web = 'https://space.bilibili.com/'
#
# data1 = pd.read_excel('favorites_rank_videos.xls',headers=0)
#
# lst = list(set(data1['author_id'].tolist()))
#
# lst.remove(319458128)
#
# data = pd.DataFrame(columns=('mid', 'name', 'website', 'title', 'sex', 'following', 'follower', 'view', 'article_view', 'likes'))
#
# for mid in lst:
#
#     print(mid)
#
#     url1 = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(mid) + '&jsonp=jsonp'
#
#     url2 = 'https://api.bilibili.com/x/relation/stat?vmid=' + str(mid) + '&jsonp=jsonp'
#
#     url3 = 'https://api.bilibili.com/x/space/upstat?mid=' + str(mid) + '&jsonp=jsonp'
#
#     response1 = requests.get(url1, headers=headers)
#
#     response2 = requests.post(url2, headers=headers)
#
#     response3 = requests.get(url3, headers=headers)
#
#     # 第一个网页
#
#     if response1.status_code == 200:
#
#         text1 = response1.text
#
#         print(text1)
#
#         result1 = json.loads(text1)['data']
#
#         lst1 = pd.Series({'mid': result1['mid'], 'name': result1['name'], 'website': web + str(result1['mid']),
#                         'title': result1['official']['title'], 'sex': result1['sex']})
#
#     # 第二个网页
#
#     if response2.status_code == 200:
#
#         text2 = response2.text
#
#         print(text2)
#
#         result2 = json.loads(text2)['data']
#
#         lst2 = pd.Series({'following': result2['following'], 'follower': result2['follower']})
#
#     # 第三个网页
#
#     if response3.status_code == 200:
#
#         text3 = response3.text
#
#         result3 = json.loads(text3)['data']
#
#         lst3 = pd.Series({'view': result3['archive']['view'], 'article_view': result3['article']['view'], 'likes': result3['likes']})
#
#     else:
#
#         pass
#
#     lst = pd.concat([lst1, lst3], axis=0)
#
#     data = data.append(lst, ignore_index=True)
#
#
#
# print(data)
#
# data.to_excel('user_information.xls')






