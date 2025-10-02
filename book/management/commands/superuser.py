from django.core.management.base import BaseCommand
from djanfo.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()

class Command(BaseCommand):
    def handle(self,*args,**options):
        if not User.objects.filter(username='your_name').exists():
            User.objects.create_superuser(
                username='hibari',
                email=''
                password='aaa'
            )