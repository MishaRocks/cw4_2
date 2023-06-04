from app.src.utils import form_vac_class, vacancy_data
from src.api import HeadHunterAPI, SuperJobAPI
from src.jsonsaver import JSONSaver

hh = HeadHunterAPI()
sj = SuperJobAPI()
js = JSONSaver()


def user_interface():
    choose_data = input("Введите платформу, с которой хотите получить вакансии (HeadHunter или Superjob):\n").lower()
    top_n = int(input("Введите количество вакансий, которое хотите получить (от 1 до 100):\n"))
    keyword = input("Введите ключевое слово для поиска вакансий:\n")

    vac_data = vacancy_data(choose_data, top_n, keyword)
    show_data = form_vac_class(choose_data, top_n, keyword)

    js.form_json(vac_data)

    for v in show_data:
        print(v)


if __name__ == '__main__':
    user_interface()
