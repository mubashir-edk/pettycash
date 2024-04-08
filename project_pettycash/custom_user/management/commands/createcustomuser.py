from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a custom user with superuser status'

    def handle(self, *args, **options):
        User = get_user_model()
        username = input("Enter username: ")
        password = input("Enter password: ")
        is_staff = input("Is this user need an admin interface access? If no, press enter key. (yes/no): ").lower() == 'yes'

        user = User.objects.create_user(username=username, password=password, is_superuser=True, is_staff=is_staff, is_active=True)
        self.stdout.write(self.style.SUCCESS(f"User '{user.username}' created successfully!"))
