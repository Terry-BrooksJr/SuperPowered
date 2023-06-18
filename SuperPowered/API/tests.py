from rest_framework.test import APITestCase
from API.models import Hero
from icecream import install

install()


# Create your tests here.
class HeroCreateTesCase(APITestCase):
    def test_create_hero(self):
        inital_hero = Hero.objects.count()
        hero_details = {
            "name": "test hero",
            "gender": "X",
            "eye_color": "test",
            "hair_color": "test",
            "skin_color": "test",
            "weight": 200,
            "height": 4590,
        }
        response = self.client.post("http://127.0.0.1:8000/api/hero/new", hero_details)
        self.assertEqual(response.status_code, 201)
        if response.status_code == 201:
            ic(response.data)
        ic(
            self.assertEqual(
                Hero.objects.count(),
                inital_hero + 1,
            )
        )
        for key, value in hero_details.items():
            self.assertEqual(response.data[key], value)

    def test_get_hero(self):
        inital_hero_count = Hero.objects.count()
        ic(inital_hero_count)
        response = self.client.get("http://127.0.0.1:8000/api/hero/")
        if response.status_code == 200:
            ic(response.data)
