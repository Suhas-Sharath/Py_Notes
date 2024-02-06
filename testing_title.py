import unittest
import title

class TestTitle(unittest.TestCase):
    def test_one(self):
        text = 'shadow'
        result = title.title_text(text)
        self.assertEqual(result,'Shadow')

    def test_two(self):
        text = 'hello world'
        result = title.title_text(text)
        self.assertEqual(result,'Hello World')
    
    def test_three(self):
        text = '12 street'
        result = title.title_text(text)
        self.assertEqual(result,'12 Street')

if __name__ == '__main__':
    unittest.main()