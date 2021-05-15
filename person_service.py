
class Person:
    def __init__(self,name,country,age,is_employed):
        self.name = name
        self.country = country
        self.age = age
        self.is_employed = is_employed

class PersonService:
    def __init__(self,db):
        self.db = db
    def get_person(self,id):
        return self.db[0]
    def add_person(self,person):
        self.db.append(person)
    def get_total_count(self):
        return len(self.db)
    def search_person_by_name(self,name):
        return list(filter(lambda p:p.name == name,self.db))
    def search_people_by_employment(self, is_employed):
        return list(filter(lambda q: q.is_employed == is_employed, self.db))

# person_service = PersonService([])