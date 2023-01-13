# Первая задача

import requests

class super_hero_AIP:

    base_host = 'https://akabab.github.io/superhero-api/api'

    def get_dict_hero(self):
        uri = '/all.json'
        request_url = self.base_host + uri
        response = requests.get(request_url)
        return response.json()

    def search_iq_hero(self, list_hero_name=["Hulk", "Captain America", "Thanos"]):
        iq_dict = {}
        hero_dict = self.get_dict_hero()

        for elem in hero_dict:
            if elem["name"] in list_hero_name:
                iq_dict[elem["name"]] = elem["powerstats"]["intelligence"]

        return iq_dict

    def search_max_iq(self, list_hero_name=["Hulk", "Captain America", "Thanos"]):
        list_hero = self.search_iq_hero(list_hero_name)
        return max(list_hero)

if __name__ == '__main__':
    Hero = super_hero_AIP()
    print(Hero.search_max_iq())


#Вторая задача

class YaUploader:
    def __init__(self, _token: str):
        self.token = _token

    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")
        responce = requests.put(href, data=open(file_path, 'rb'))
        responce.raise_for_status()
        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    # Получаем путь к загружаемому файлу и токен от пользователя
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
