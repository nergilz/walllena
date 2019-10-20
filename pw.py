
# задача 
# нужна статистика пользователь, 
# которые оставили больше всего комментариев и лайкнули наибольшее количество постов.

# 1. с юмором все ок, комментарий, который лайкнали. 
# 2. это количество комментариев за сутки. 
# 3. Это сколько пользователь лайков поставил.


import vk
import getpass
import json
from vk.exceptions import VkException
from time import sleep

TOKEN = 'c14030f0695f47d7557a897c771ffd7e703111482537966163dc56473531c1de7769b227881a7bf0463b4'
GROUP_ID = '-150144298'
# APP_ID = 6421852


def write_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def calculation_date():
    pass

def get_data_from_post(post): # from Molchanov tutorial
    pass


def main(date_x): # from Molchanov tutorial

    offset = 0
    all_posts = []

    while True:
        sleep(1)

        session = vk.AuthSession(access_token = TOKEN)
        api     = vk.API(session)
        data    = api.wall.get(owner_id=GROUP_ID, count=1, offset=offset, extended=1, v=5.101)

        posts   = data['items']
        all_posts.extend(posts)
        oldest_post_date = posts[-1]['date']

        if oldest_post_date < date_x:
            break

        offset += 1

    return all_posts # {'items': all_posts}
 

if __name__ == '__main__':

    date_x_week = 1567338147
    date_x_day  = 1567770147

    try:
        write_json(main(date_x_week), 'pw_data_7.json')

    except VkException as err:
        print(' ERROR : {}'.format(err))


'''
def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends_online = api.users.get(
        user_ids=api.friends.getOnline(v=5.73),
        v=5.73
    )
    return friends_online

def get_group_data():

    session = vk.AuthSession(access_token = TOKEN)
    api     = vk.API(session)
    data    = api.wall.get(owner_id=GROUP_ID, count=100, offset=0, v=5.101)
    return data


# https://oauth.vk.com/authorize?client_id={ID приложения}&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos ,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token


'''