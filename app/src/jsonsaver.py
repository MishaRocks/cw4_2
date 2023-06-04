import json

from app.src.api import HeadHunterAPI, SuperJobAPI


class JSONSaver:

    def __init__(self):
        self.__data = "data/vacancies.json"

    @property
    def data(self):
        return self.__data

    def form_json(self, choose_data: list):

        sj = SuperJobAPI()
        hh = HeadHunterAPI()

        vac_data = []
        if 'headhunter' in choose_data and 'superjob' in choose_data:
            for v in hh.list_for_json():
                vac_data.append(v)
            for v in sj.list_for_json():
                vac_data.append(v)
        elif 'headhunter' in choose_data:
            for v in hh.list_for_json():
                vac_data.append(v)
        elif 'superjob' in choose_data:
            for v in sj.list_for_json():
                vac_data.append(v)
        else:
            raise FileNotFoundError('Такой базы не существует')

        open(self.data, "w").close()

        with open(self.data, 'w', encoding='utf8') as file:
            json.dump(vac_data, file, ensure_ascii=False, indent=4)
