from unittest import TestCase
# from person_service import person_service
from person_service import *

class PersonServiceTestCase(TestCase):
    """ Person Service Test"""

    def test_get_person_from_db(self):
        """ get person from db"""
        p = Person("jim","uk",20,True)
        person_service = PersonService([p])
        self.assertEqual(p,person_service.get_person(1))

    def test_count_people_in_db(self):
        """ count people from db"""
        p = Person("jim","uk",20,True)
        u = Person("lad","us",40,True)
        m = Person("kim","nk",60,False)
        person_service = PersonService([p,u,m])
        self.assertEqual(3,person_service.get_total_count())

    def test_add_person_to_db(self):
        """ add  person to db"""
        p = Person("jim", "uk", 20, True)
        person_service = PersonService([])
        person_service.add_person(p)
        self.assertEqual(p, person_service.get_person(1))

    def test_ok(self):
        """ add  person to db"""
        p = Person("jim", "uk", 20, True)
        h = Person("mike", "us", 30, True)
        person_service1 = PersonService([])
        person_service2 = PersonService([])
        person_service1.add_person(p)
        person_service2.add_person(h)
        self.assertEqual(p, person_service1.get_person(1))
        self.assertEqual(h, person_service2.get_person(1))

    def test_search_person_by_name_from_db(self):
        """ search person by name from db"""
        p = Person("jim", "uk", 20, True)
        d = Person("jimmy", "uk", 20, True)
        q = Person("lary", "us", 14, False)
        r = Person("eli", "us", 80, False)
        person_service = PersonService([p,d,q,r])
        self.assertEqual([q], person_service.search_person_by_name("lary"))

    def test_search_people_by_employment_from_db(self):
        """ search people by employment from db"""
        p = Person("jim", "uk", 20, True)
        d = Person("jimmy", "uk", 20, True)
        q = Person("lary", "us", 14, False)
        r = Person("eli", "us", 80, False)
        person_service = PersonService([p, d, q, r])
        self.assertEqual([q,r], person_service.search_people_by_employment(False))