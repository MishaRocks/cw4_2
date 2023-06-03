from api import HeadHunterAPI, SuperJobAPI


class Vacancies:

    def __init__(self, id, title, payment, date, description, candidat, URL):
        self.id = id
        self.title = title
        self.payment = payment
        self.date = date
        self.description = description
        self.candidat = candidat
        self.URL = URL




