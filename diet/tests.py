from django.test import TestCase


class TestDietView(TestCase):

    def test_home_view(self):
        # preparing, execution
        response = self.client.get("/diet/")

        # verification
        self.assertEqual(response.status_code, 200)
