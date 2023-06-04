from src.api import HeadHunterAPI, SuperJobAPI
from src.jsonsaver import JSONSaver

hh = HeadHunterAPI()
sj = SuperJobAPI()
js = JSONSaver()

if __name__ == '__main__':

    joblist = ['superjob', 'headhunter']
    print(js.form_json(joblist))


