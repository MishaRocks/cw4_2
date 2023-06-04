import json

from app.src.api import HeadHunterAPI, SuperJobAPI


class JSONSaver:

    def __init__(self):
        self.__data = "data/vacancies.json"

    @property
    def data(self):
        return self.__data

    def form_json(self, vac_data):

        with open(self.data, 'w', encoding='utf8') as file:
            json.dump(vac_data, file, ensure_ascii=False, indent=4)

    def get_vacancies_list(self):
        with open(self.data, 'r', encoding='utf8') as file:
            vacancies_data = json.load(file)
        return vacancies_data

    def get_vacancy(self, vid):

        with open(self.data, 'r', encoding='utf8') as file:
            vacancies_data = json.load(file)

            for v in vacancies_data:
                if v['id'] == vid:
                    return v
                else:
                    raise FileNotFoundError('Вакансия не найдена')


