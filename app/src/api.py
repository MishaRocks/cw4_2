from abc import ABC, abstractmethod
import requests
import json


class API(ABC):

    @abstractmethod
    def host_to_api(self):
        ...

    @abstractmethod
    def save_json(self):
        ...


class HeadHunterAPI(API):

    _data = 'data/hh.json'

    def host_to_api(self) -> dict:
        """
        Отправляем запрос к Апи HeadHunter
        :return: ответ от сервера
        """
        params = {
            'text': 'NAME:стажер',  # Текст фильтра.
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва(1)
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.json()
        return data

    def dict_for_json(self):
        """
        Формируем словать с выбранными полями
        :return:
        """

        hh_to_json = []

        for v in self.host_to_api()["items"]:
            hh_dict = {
                'id': v['id'],
                'title': v["name"],
                'payment': v["salary"],
                'date': v["published_at"],
                'description': v["snippet"]["responsibility"],
                'candidat': v["snippet"]["requirement"],
                'URL': v["alternate_url"]
            }
            hh_to_json.append(hh_dict)

        with open(self._data, 'w', encoding='utf8') as file:
            json.dump(hh_to_json, file, ensure_ascii=False, indent=4)


class SuperJobAPI(API):

    _id = 2511
    _secret_key = 'v3.r.12992770.9da9256ef42ebec4990e486239bd9681525bbdf4.8bf82f42278c10eee6820196cc20289b607cc2a2'
    _data = 'data/sj.json'

    def host_to_api(self) -> dict:
        params = {
            'keyword': 'Аналитик данных',
            'payment_from': 0,
            'count': 100,
            'page': 0
        }

        req = requests.get('https://api.superjob.ru/2.0/vacancies/',
                           headers={"X-Api-App-Id": self._secret_key},
                           params=params)
        data = req.json()
        return data

    def save_json(self):

        sj_to_json = []

        for v in self.host_to_api()["objects"]:
            sj_dict = {
                'id': v['id'],
                'title': v["profession"],
                'payment': v["payment_from"],
                'date': v["date_published"],
                'description': v["work"],
                'candidat': v["candidat"],
                'URL': v["link"]
            }
            sj_to_json.append(sj_dict)

        with open(self._data, 'w', encoding='utf8') as file:
            json.dump(sj_to_json, file, ensure_ascii=False, indent=4)
