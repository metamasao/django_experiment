from decimal import Decimal
from django.test import TestCase

from diet.models import Diet


class DietModelTest(TestCase):

    def test_diet_model_field(self):
        # preparing
        Diet.objects.create(
            author="testuser",
            diet_data=60.1
        )

        diet_instance = Diet.objects.get(pk=1)

        # validation
        self.assertEqual(diet_instance.diet_data, Decimal("60.1"))
        self.assertEqual(diet_instance.author, "testuser")
