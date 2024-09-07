import unittest
from main import send_motivation, send_random_photo

class TestBotFunctions(unittest.TestCase):
   def test_send_motivation(self):
       quote = send_motivation()
       self.assertIsInstance(quote, str)
       self.assertIn("-", quote)  # Проверяем, что строка содержит разделитель (обычно между цитатой и автором)

class TestPhotoFunction(unittest.TestCase):
   def test_send_random_photo(self):
       photo_url = send_random_photo()
       self.assertTrue(photo_url.startswith("http"))  # Проверяем, что результат начинается с http, предполагая, что это URL

if __name__ == '__main__':
   unittest.main()



