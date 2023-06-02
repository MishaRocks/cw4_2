from abc import ABC, abstractmethod
import requests
import json
import time


class API(ABC):

    @abstractmethod
    def host_to_api(self):
        ...

    @abstractmethod
    def get_vacancies(self):
        ...

    @abstractmethod
    def save_json(self):
        ...


class HeadHunterAPI(API):

    def host_to_api(self):
        params = {
            'text': 'NAME:python',  # Текст фильтра.
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            # 'page': page,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()

        return data

    def get_vacancies(self):
        ...

    def save_json(self):
        ...


class SuperJobAPI(API):

    _id = 2511
    _secret_key = 'v3.r.12992770.9da9256ef42ebec4990e486239bd9681525bbdf4.8bf82f42278c10eee6820196cc20289b607cc2a2'

    def host_to_api(self):
        ...

    def get_vacancies(self):
        ...

    def save_json(self):
        ...
