
class Vacancies:

    def __init__(self, vid: int, title: str, payment: int, date, description: str, candidate: str, url):
        self.vid = vid
        self.title = title
        self.payment = payment
        self.date = date
        self.description = description
        self.candidate = candidate
        self.url = url

    def __repr__(self):
        return f'self.title'

    def __gt__(self, other):
        if isinstance(self, other):
            return self.payment > other.payment
