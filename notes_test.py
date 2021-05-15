"""
Test cases
"""

# !coding: utf-8

from unittest import TestCase
from Calculator import add

from Calculator import multiply
from notes import get
def add_note(strings,string):
    strings.append(string)
    return strings

class NotesTestCase(TestCase):
    """ Notes Test"""
    def test_get_note_from_list(self):
        """ get note from list """
        notes = ["a" , "b" , "c"]
        id = 1
        expected_output = "b"
        self.assertEqual(expected_output, get(notes,id))

    def test_get_first_note_from_list(self):
            """ get first note from list """
            notes = ["a", "b", "c"]
            id = 0
            expected_output = "a"
            self.assertEqual(expected_output,get(notes,id))
    def test_add_note_to_list(self):
        """ add note to list """
        initial_notes = ["a" , "b" , "c"]
        notes = add_note(initial_notes,"d")
        id = 3
        expected_output = "d"
        self.assertEqual(expected_output, get(notes,id))