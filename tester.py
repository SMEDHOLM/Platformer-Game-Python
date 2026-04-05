import unittest
# Test whether each level file contains both a player and a door.
class TestLevels(unittest.TestCase):
    def test_LEVEL1(self):
        self.assertEqual(self.seacrh_word("LEVELS/LEVEL1", "P", "D"), True)
    def test_LEVEL2(self):
        self.assertEqual(self.seacrh_word("LEVELS/LEVEL2", "P", "D"), True)
    def test_LEVEL3(self):
        self.assertEqual(self.seacrh_word("LEVELS/LEVEL3", "P", "D"), True)

    def seacrh_word(self, file, word, word2):
        with open(file) as file:
            contents = file.read()
            if word and word2 in contents:
                return True
            else:
                return False

if __name__ == '__main__':
    unittest.main()
