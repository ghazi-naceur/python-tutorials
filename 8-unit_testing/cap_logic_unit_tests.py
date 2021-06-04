import unittest
import cap_logic

class TextCap(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = cap_logic.cap_text(text)
        self.assertEqual(result, "Python")


    def test_multiple_words(self):
        text = "isaac netero"
        result = cap_logic.cap_text(text)
        self.assertEqual(result, "Isaac Netero")


if __name__ == '__main__':
    unittest.main()