from src.api import HeadHunterAPI, SuperJobAPI


if __name__ == '__main__':

    hh = HeadHunterAPI()
    sj = SuperJobAPI()
    print(sj.save_json())


