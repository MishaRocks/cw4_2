from api import HeadHunterAPI, SuperJobAPI
from vacancies import Vacancies


class JSONSaver:

    def form_json(self):
        open("data/vacancies.json", "w").close()

    with open(self._data, 'w', encoding='utf8') as file:
        json.dump(hh_to_json, file, ensure_ascii=False, indent=4)