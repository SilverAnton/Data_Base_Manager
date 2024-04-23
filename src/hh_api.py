import requests


class HeadHunterApi:
    def __init__(self):
        self.__url = "http://api.hh.ru/employers/"
        self.__param = {'text': '', "per_page": 10, "sort_by": "by_vacancies_open"}

        self.employers = []
        self.vacancies = []
        self.result = {}


    def add_employers(self, keyword):
        """Метод добавляет список словарей с информацией о работодателях, по ключевому слову в атрибут employers"""
        self.__param['text'] = keyword
        response = requests.get(self.__url, self.__param)
        self.employers.append(response.json().get("items"))



    def add_vacancy(self, keyword):
        employers = self.employers[0]
        self.__param['text'] = keyword
        self.__param['per_page'] = 20
        for employer in employers:
            response = requests.get(employer['vacancies_url'], self.__param)
            self.vacancies.append(response.json()['items'])





obj = HeadHunterApi()
obj.add_employers('develop')
obj.add_vacancy('python')
#print(len(obj.vacancies))
print(obj.employers[0])

