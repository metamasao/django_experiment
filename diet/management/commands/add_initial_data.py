import logging
from django.core.management import BaseCommand

from diet.models import Diet

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):

        initial_username = "testuser"
        for i in range(10):
            diet_data = 60.0 + i
            logger.info("start creating initial data\nauthor: %s diet_data: %s", initial_username, diet_data)
            # Diet.objects.create(
            #     author=initial_username,
            #     diet_data=diet_data
            # )
