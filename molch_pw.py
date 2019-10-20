import requests
import urllib3

# этот пример сейчас не работает из за особенностей api vk

TOKEN = 'c14030f0695f47d7557a897c771ffd7e703111482537966163dc56473531c1de7769b227881a7bf0463b4'
GROUP_ID = '-150144298'
BASE = 'https://api.vk.com/method/wall.get'


def write_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main(date_x):

    offset = 0
    all_posts = []

    while True:

        r = requests.get(
            BASE,
            params={
                'access_token' : TOKEN,
                'owner_id': GROUP_ID,
                'count': 99,
                'offset': 0,
                'v': 5.101
                },
            verify = False #  отключение ssl
            )


if __name__ == '__main__':

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # убираем ошибку
    date_x = 1567005261

    try:
        #write_json(get_group_data(group_id, token), 'pw_data_3.json')
        write_json(main(date_x), 'pw_data_4.json')

    except VkException as err:
        print(' ERROR : {}'.format(err))


# https://api.vk.com/method/wall.get?user_id=210700286&v=5.52
# 150144298