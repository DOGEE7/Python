import unittest
from practice import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'Janis Joplin')


unittest.main()
