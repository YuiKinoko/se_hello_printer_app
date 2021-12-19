from hello_world.formater import plain_text_upper_case, plain_text_lower_case
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "eeemsg")

        self.assertEqual("EEEMSG WWWW", r)

    def test_plain_text_lower_case(self):
        r = plain_text_lower_case("WWWW", "EEEMSG")

        self.assertEqual("eeemsg wwww", r)
