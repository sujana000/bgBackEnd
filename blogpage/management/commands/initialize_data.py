from django.core.management.base import BaseCommand
from blogpage.models import Category, Author

class Command(BaseCommand):
    help = 'Initialize data by creating categories and authors'

    def handle(self, *args, **kwargs):
        # Create categories
        category1 = Category.objects.create(name='Technology')
        category2 = Category.objects.create(name='Science')

        # Create authors
        author1 = Author.objects.create(name='John Doe')
        author2 = Author.objects.create(name='Jane Smith')

        self.stdout.write(self.style.SUCCESS('Data initialized successfully!'))