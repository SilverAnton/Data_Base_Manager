import requests
import json


class HeadHunterApi:
    def __init__(self):
        self.__url = "http://api.hh.ru/employers/"
        self.__param = {"text": '', "per_page": 10, "sort_by": "by_vacancies_open"}

        self.employers = []
        self.vacancies = []
        self.result = {}

    def add_employers(self, keyword):
        """Метод добавляет список словарей с информацией о работодателях, по ключевому слову в атрибут employers"""
        self.__param['text'] = keyword
        response = requests.get(self.__url, self.__param)
        self.employers.append(response.json()["items"])

    def add_vacancy(self):
        employers = self.employers[0]
        del self.__param['text']
        del self.__param["sort_by"]
        self.__param['per_page'] = 100
        for employer in employers:
            response = requests.get(employer['vacancies_url'], self.__param)
            self.vacancies.append(response.json()['items'])

    def save_as_json_employers(self):
        with open('employers.json', 'w', encoding="UTF8") as file:
            json.dump(self.employers, file, ensure_ascii=False, indent=4)

    def save_as_json_vacancies(self):
        with open('vacancies.json', 'w', encoding="UTF8") as file:
            json.dump(self.vacancies, file, ensure_ascii=False, indent=4)
