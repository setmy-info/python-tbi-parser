import unittest

from info.setmy.tbi.tbi_parser import parse_tbi


class ITExample(unittest.TestCase):

    def setUp(self):
        pass

    def test_example(self):
        tbi = parse_tbi("./test/resources/tbi-376bdfaa-1195-11ee-be56-0242ac120002.yaml")
        self.assertEqual(tbi['name'], "TBI name")
        self.assertEqual(tbi['description'], "TBI description")
        self.assertEqual(tbi['authors'][0], "Imre Tabur <imre.tabur@mail.ee>")
        self.assertEqual(tbi['materials'][0], "example.doc")


if __name__ == '__main__':
    unittest.main()