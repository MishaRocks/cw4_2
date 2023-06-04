from abc import ABC, abstractmethod
import requests


class API(ABC):

    @abstractmethod
    def host_to_api(self, top_n, keyword):
        ...


class HeadHunterAPI(API):

    def host_to_api(self, top_n: int = 10, keyword=None) -> list:
        """
        Отправляем запрос к Апи HeadHunter
        :return: ответ от сервера
        """
        params = {
            'text': f'NAME:{keyword}',  # Текст фильтра.
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва(1)
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': int(top_n)  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.json()

        hh_to_json = []

        for v in data["items"]:
            hh_dict = {
                'id': v['id'],
                'title': v["name"],
                'payment': v["salary"]["from"] if v["salary"] else None,
                'date': v["published_at"],
                'description': v["snippet"]["responsibility"],
                'candidate': v["snippet"]["requirement"],
                'url': v["alternate_url"]
            }
            hh_to_json.append(hh_dict)

        return hh_to_json


class SuperJobAPI(API):

    _id = 2511
    _secret_key = 'v3.r.12992770.9da9256ef42ebec4990e486239bd9681525bbdf4.8bf82f42278c10eee6820196cc20289b607cc2a2'

    def host_to_api(self, top_n: int = 10, keyword=None) -> list:
        """
        Отправляем запрос к Апи HeadHunter
        :return: ответ от сервера
        """
        params = {
            'keyword': keyword,
            'payment_from': 0,
            'count': int(top_n),
            'page': 0
        }

        req = requests.get('https://api.superjob.ru/2.0/vacancies/',
                           headers={"X-Api-App-Id": self._secret_key},
                           params=params)
        data = req.json()

        sj_to_json = []

        for v in data["objects"]:
            sj_dict = {
                'id': v['id'],
                'title': v["profession"],
                'payment': v["payment_from"],
                'date': v["date_published"],
                'description': v["work"],
                'candidate': v["candidat"],
                'url': v["link"]
            }
            sj_to_json.append(sj_dict)

        return sj_to_json
