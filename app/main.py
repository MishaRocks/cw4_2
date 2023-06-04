from src.api import HeadHunterAPI, SuperJobAPI
from src.jsonsaver import JSONSaver

hh = HeadHunterAPI()
sj = SuperJobAPI()
js = JSONSaver()


def user_interface():
    choose_data = input("Введите платформу, с которой хотите получить вакансии (HeadHunter или Superjob):\n").lower()
    top_n = int(input("Введите количество вакансий, которое хотите получить (от 1 до 100):\n"))
    keyword = input("Введите ключевое слово для поиска вакансий:\n")

    vac_data = []
    if 'headhunter' in choose_data and 'superjob' in choose_data:
        for v in hh.host_to_api(top_n, keyword):
            vac_data.append(v)
        for v in sj.host_to_api(top_n, keyword):
            vac_data.append(v)
    elif 'headhunter' == choose_data:
        for v in hh.host_to_api(top_n, keyword):
            vac_data.append(v)
    elif 'superjob' == choose_data:
        for v in sj.host_to_api(top_n, keyword):
            vac_data.append(v)
    else:
        raise FileNotFoundError('Такой базы не существует')

    js.form_json(vac_data)
    print(js.get_vacancies_list())


if __name__ == '__main__':

    user_interface()
