import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):
    def test_website_connection(self):
        url = "https://atg.worldsfsf"
        print("Attempting to connect to:", url)
        try:
            response = requests.get(url)
            print("Response status code:", response.status_code)
            self.assertEqual(response.status_code, 200)
            print("Website loaded successfully!")
        except requests.exceptions.RequestException as e:
            print("Error connecting to the website:", e)
            self.fail("Website failed to load")

if __name__ == '__main__':
    unittest.main()
